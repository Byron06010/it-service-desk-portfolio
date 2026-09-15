-- ==========================================================
-- SCRIPT DE CREACIÓN DE BASE DE DATOS: db_soporte_it
-- Proyecto: Sistema de Monitoreo de Incidencias IT (Service Desk)
-- ==========================================================

-- 1. Eliminar tablas si ya existen (para evitar conflictos al reiniciar)
DROP TABLE IF EXISTS tickets CASCADE;
DROP TABLE IF EXISTS usuarios CASCADE;

-- 2. Crear tabla de Usuarios
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    rol VARCHAR(50) NOT NULL
);

-- 3. Crear tabla de Tickets / Incidencias
CREATE TABLE tickets (
    id_ticket SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT NOT NULL,
    estado VARCHAR(30) NOT NULL DEFAULT 'Abierto',
    prioridad VARCHAR(20) NOT NULL,
    id_usuario_reporta INT REFERENCES usuarios(id_usuario) ON DELETE SET NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_resolucion TIMESTAMP
);

-- ==========================================================
-- INSERCIÓN DE DATOS DE PRUEBA (Opcional para poblar el Power BI)
-- ==========================================================

-- Insertar usuarios de prueba
INSERT INTO usuarios (nombre, rol) VALUES 
('Alejandro Guerrero', 'IT Engineer'),
('Yohana Garcés', 'Administrativo'),
('Carlos Pérez', 'Soporte Nivel 1'),
('Ana López', 'Recursos Humanos');

-- Insertar tickets de prueba iniciales
INSERT INTO tickets (titulo, descripcion, estado, prioridad, id_usuario_reporta, fecha_creacion, fecha_resolucion) VALUES 
('Fallo de conexión a la VPN', 'No es posible conectar a la VPN corporativa desde la red externa.', 'Abierto', 'Alta', 2, '2026-05-10 08:30:00', NULL),
('Impresora del piso 2 sin tóner', 'La impresora principal marca error de cartucho agotado.', 'En Proceso', 'Media', 3, '2026-05-10 09:15:00', NULL),
('Telefono sin señal', 'El teléfono IP de recepción no tiene tono de marcado.', 'Resuelto', 'Baja', 4, '2026-05-09 14:00:00', '2026-05-09 16:30:00'),
('Actualización de software contable', 'Se requiere instalar la nueva versión del parche fiscal en equipos de administración.', 'Abierto', 'Alta', 2, '2026-05-11 10:00:00', NULL),
('Lentitud general en equipo', 'El equipo portátil presenta cuelgues constantes al abrir IDEs de programación.', 'En Proceso', 'Media', 1, '2026-05-11 11:20:00', NULL);