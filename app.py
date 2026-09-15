import streamlit as st
import psycopg2
import pandas as pd

# Configuración de la conexión a PostgreSQL
def init_connection():
    return psycopg2.connect(
        host="localhost",
        database="yourdatabase",
        user="postgres",
        password="yourpassword",
        port="5432"
    )

conn = init_connection()

st.title("🛠️ Sistema de Monitoreo de Incidencias IT - Service Desk")

menu = st.sidebar.selectbox("Menú", ["Ver Tickets", "Crear Nuevo Ticket"])

def cargar_datos():
    query = """
        SELECT t.id_ticket, t.titulo, t.descripcion, t.estado, t.prioridad, 
               u.nombre AS usuario_reporta, t.fecha_creacion, t.fecha_resolucion
        FROM tickets t
        JOIN usuarios u ON t.id_usuario_reporta = u.id_usuario
        ORDER BY t.fecha_creacion DESC;
    """
    return pd.read_sql(query, conn)

if menu == "Ver Tickets":
    st.subheader("📋 Listado de Incidencias Actuales")
    try:
        df_tickets = cargar_datos()
        st.dataframe(df_tickets, width='stretch')
        
        st.divider()
        st.subheader("🔄 Actualizar Estado de un Ticket")
        
        if not df_tickets.empty:
            # Crear lista desplegable con los tickets existentes
            opciones_tickets = {
                f"ID {row['id_ticket']} - {row['titulo']} (Estado actual: {row['estado']})": row['id_ticket']
                for _, row in df_tickets.iterrows()
            }
            
            ticket_seleccionado_label = st.selectbox("Selecciona el ticket a modificar:", list(opciones_tickets.keys()))
            id_ticket_sel = opciones_tickets[ticket_seleccionado_label]
            
            nuevo_estado = st.selectbox("Nuevo Estado", ["Abierto", "En Proceso", "Resuelto", "Cerrado"])
            
            if st.button("Actualizar Estado", key="btn_actualizar_estado"):
                cursor = conn.cursor()
                # Si pasa a Resuelto o Cerrado, registramos la fecha de resolución actual (NOW())
                if nuevo_estado in ["Resuelto", "Cerrado"]:
                    cursor.execute("""
                        UPDATE tickets 
                        SET estado = %s, fecha_resolucion = NOW()
                        WHERE id_ticket = %s
                    """, (nuevo_estado, id_ticket_sel))
                else:
                    cursor.execute("""
                        UPDATE tickets 
                        SET estado = %s, fecha_resolucion = NULL
                        WHERE id_ticket = %s
                    """, (nuevo_estado, id_ticket_sel))
                
                conn.commit()
                st.success(f"¡El ticket ID {id_ticket_sel} ha sido actualizado a '{nuevo_estado}'!")
                st.rerun() # Refresca la página automáticamente para ver el cambio en la tabla
        else:
            st.info("No hay tickets registrados aún.")
            
    except Exception as e:
        st.error(f"Error al cargar o actualizar los datos: {e}")

elif menu == "Crear Nuevo Ticket":
    st.subheader("➕ Registrar Nueva Incidencia")
    
    with st.form("form_ticket"):
        titulo = st.text_input("Título del Ticket")
        descripcion = st.text_area("Descripción del Problema")
        prioridad = st.selectbox("Prioridad", ["Baja", "Media", "Alta", "Crítica"])
        
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, nombre FROM usuarios WHERE rol = 'Usuario Final'")
        usuarios = cursor.fetchall()
        usuario_dict = {nombre: id_u for id_u, nombre in usuarios}
        
        usuario_seleccionado = st.selectbox("Reportado por", list(usuario_dict.keys()))
        
        submitted = st.form_submit_button("Guardar Ticket", key="btn_guardar_ticket")
        
        if submitted:
            if titulo and descripcion:
                id_u = usuario_dict[usuario_seleccionado]
                cursor.execute("""
                    INSERT INTO tickets (titulo, descripcion, estado, prioridad, id_usuario_reporta)
                    VALUES (%s, %s, 'Abierto', %s, %s)
                """, (titulo, descripcion, prioridad, id_u))
                conn.commit()
                st.success("¡Ticket creado con éxito en PostgreSQL!")
            else:
                st.warning("Por favor completa los campos obligatorios.")