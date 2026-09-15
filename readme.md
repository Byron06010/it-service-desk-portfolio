# 🛠️ Sistema de Monitoreo de Incidencias IT (Service Desk)

Proyecto Full-Stack de Service Desk desarrollado como parte del portafolio técnico. Este sistema permite la gestión completa de tickets de soporte técnico mediante una aplicación web interactiva, respaldada por una base de datos relacional y un tablero analítico para la toma de decisiones.

---

## 🚀 Tecnologías y Stack Utilizado

* **Base de Datos:** PostgreSQL (`db_soporte_it`)
* **Backend / Frontend Web:** Python (Streamlit)
* **Inteligencia de Negocios (BI):** Power BI Desktop
* **Control de Versiones:** Git & GitHub

---

## ⚙️ Arquitectura del Proyecto

1. **Capa de Datos:** Una base de datos relacional en PostgreSQL compuesta por dos tablas principales:
   * `usuarios`: Almacena la información del personal y sus roles.
   * `tickets`: Registra las incidencias con su título, descripción, prioridad, estado y fechas clave.
2. **Capa de Aplicación (Streamlit):** Permite realizar operaciones CRUD completas. Los usuarios pueden reportar nuevos incidentes, visualizar el listado de tickets y actualizar los estados en tiempo real (de *Abierto* a *En Proceso*, *Resuelto* o *Cerrado*), gestionando automáticamente las marcas de tiempo (`fecha_resolucion`).
3. **Capa de Analítica (Power BI):** Conectada en vivo a PostgreSQL para medir métricas clave de desempeño (KPIs), distribución de incidencias por estado y volúmenes de carga según la prioridad.

---

## 📊 Visualización del Panel (Power BI)

*(Aquí puedes colocar las capturas de pantalla de tu Power BI)*

![Dashboard General de Service Desk](assets/dashboard_powerbi.png)

* **Indicadores Clave (KPIs):** Conteo total de tickets y seguimiento de resolución.
* **Gráficos Analíticos:** Distribución porcentual por estados y segmentación por niveles de prioridad (*Alta*, *Media*, *Baja*).

---

## 💻 Aplicación Web (Streamlit)

El sistema cuenta con una interfaz intuitiva para el equipo de soporte e ingeniería:
* **Módulo de Creación:** Registro rápido de nuevas fallas técnicas asociadas a un usuario.
* **Módulo de Gestión:** Tabla interactiva con opción de actualización de estados de forma dinámica.

---

## ⚙️ Cómo ejecutar el proyecto localmente

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/it-service-desk-portfolio.git](https://github.com/TU_USUARIO/it-service-desk-portfolio.git)
   cd it-service-desk-portfolio

