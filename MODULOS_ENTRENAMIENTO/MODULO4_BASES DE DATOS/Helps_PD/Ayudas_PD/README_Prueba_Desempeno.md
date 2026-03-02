# 📌 Nombre del Proyecto

API REST desarrollada con Node.js y Express conectada a PostgreSQL.
Permite gestionar entidades mediante operaciones CRUD, incluyendo
validaciones, manejo de errores y consultas avanzadas.

------------------------------------------------------------------------

# 🎯 Objetivo de la Prueba

Este proyecto tiene como objetivo demostrar:

-   Diseño de base de datos (DER + normalización)
-   Creación de scripts SQL (DDL/DML)
-   Migración de datos desde Excel
-   Desarrollo de API REST con Express
-   Buenas prácticas (estructura, validaciones, manejo de errores)
-   Documentación clara

------------------------------------------------------------------------

# 🏗️ Arquitectura del Proyecto

    project-root/
    │
    ├── database/
    │   ├── ddl.sql
    │   ├── seed.sql
    │   └── queries.sql
    │
    ├── src/
    │   ├── config/
    │   │   └── db.js
    │   ├── routes/
    │   ├── controllers/
    │   ├── models/ (opcional)
    │   └── app.js
    │
    ├── .env
    ├── package.json
    └── README.md

**Descripción:**

-   `database/` → Scripts SQL (creación, inserción y consultas).
-   `src/config/` → Configuración de conexión a base de datos.
-   `routes/` → Definición de endpoints.
-   `controllers/` → Lógica de negocio.
-   `models/` → Acceso a datos (opcional).
-   `app.js` → Configuración principal del servidor.

------------------------------------------------------------------------

# 🗄️ Base de Datos

## Motor utilizado

-   PostgreSQL

## Diseño

-   Modelo entidad--relación normalizado hasta 3FN.
-   Uso de Primary Keys, Foreign Keys y constraints (`NOT NULL`,
    `UNIQUE`, `CHECK`).
-   Índices cuando es necesario.

## Scripts incluidos

-   `ddl.sql` → creación de tablas.
-   `seed.sql` → inserción de datos.
-   `queries.sql` → consultas requeridas.

------------------------------------------------------------------------

# 🚀 Instalación y Ejecución

## 1. Clonar repositorio

``` bash
git clone <repo-url>
cd <project-name>
```

## 2. Instalar dependencias

``` bash
npm install
```

## 3. Configurar variables de entorno

Crear archivo `.env`:

    PORT=3000
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=tu_password
    DB_NAME=nombre_base_datos

## 4. Ejecutar scripts SQL

Desde DBeaver o psql:

1.  Ejecutar `ddl.sql`
2.  Ejecutar `seed.sql`

## 5. Iniciar servidor

``` bash
npm run dev
```

Servidor disponible en:

    http://localhost:3000

------------------------------------------------------------------------

# 📡 Endpoints de la API

## Entidad: \[NombreEntidad\]

  Método   Endpoint             Descripción
  -------- -------------------- ----------------
  GET      /api/entidades       Obtener todos
  GET      /api/entidades/:id   Obtener por ID
  POST     /api/entidades       Crear registro
  PUT      /api/entidades/:id   Actualizar
  DELETE   /api/entidades/:id   Eliminar

Ejemplo de request:

``` json
POST /api/entidades
{
  "campo1": "valor",
  "campo2": 123
}
```

------------------------------------------------------------------------

# ✅ Validaciones y Manejo de Errores

-   Validación de datos de entrada.
-   Respuestas HTTP correctas:
    -   200 OK
    -   201 Created
    -   400 Bad Request
    -   404 Not Found
    -   500 Internal Server Error
-   Manejo centralizado de errores.

------------------------------------------------------------------------

# 🧪 Pruebas

Endpoints probados con Postman o Thunder Client.

Casos cubiertos: - Creación válida - Datos inválidos - Registro
inexistente - Eliminación exitosa

------------------------------------------------------------------------

# 📊 Decisiones Técnicas

-   Elección del driver de conexión (`pg` o `sequelize`).
-   Decisiones de modelado.
-   Estrategia de normalización.
-   Manejo de relaciones.
-   Uso de índices cuando aplica.

------------------------------------------------------------------------

# 🔒 Consideraciones

-   Uso de variables de entorno para credenciales.
-   Separación de capas (routes → controllers → db).
-   Código modular y organizado.

------------------------------------------------------------------------

# 👨‍💻 Autor

Nombre\
Fecha\
Prueba Técnica
