
set search_path to gestion_academica_universidad;


-- TASK 1

create table estudiantes (
	id_estudiante bigint generated always as identity primary key,
	nombre_completo varchar(150) not null,
	correo_electronico varchar(150) not null unique,
	genero varchar(20) check (genero in ('Masculino', 'Femenino', 'Otro')),
	identificacion varchar(20) not null unique,
	carrera varchar(100) not null,
	fecha_nacimiento date not null,
	fecha_ingreso date not null,
	created_at timestamptz not null default current_timestamp
);	

create table docentes(
	id_docente bigint generated always as identity primary key,
	nombre_completo varchar(150) not null,
	correo_institucional varchar(150) not null unique,
	departamento_academico varchar(100) not null,
	anios_experiencia integer not null check (anios_experiencia >= 0),
	created_at timestamptz not null default current_timestamp
);

create table cursos(
	id_curso bigint generated always as identity primary key,
	id_docente bigint not null,
	nombre varchar(150) not null,
	codigo varchar(20) not null unique,
	creditos integer not null check (creditos > 0),
	semestre integer not null check (semestre > 0),
	created_at timestamptz not null default current_timestamp,
	
	constraint fk_curso_docente
		foreign key (id_docente)
		references docentes (id_docente)
		on delete restrict
		on update cascade
);

create table inscripciones(
	id_inscripcion bigint generated always as identity primary key,
	id_estudiante bigint not null,
	id_curso bigint not null,
	fecha_inscripcion date not null default current_date,
	calificacion_final numeric(2,1) check (calificacion_final between 0 and 5),
	created_at timestamptz not null default current_timestamp,
	
	constraint fk_inscripcion_estudiante
		foreign key (id_estudiante)
		references estudiantes (id_estudiante)
		on delete cascade
		on update cascade,
	
	constraint fk_inscripcion_curso
		foreign key (id_curso)
		references cursos (id_curso)
		on delete cascade
		on update cascade,
		
	constraint unique_inscripcion 
		unique (id_estudiante, id_curso)
);


-- TASK 2

insert into estudiantes (nombre_completo, correo_electronico, genero, identificacion, carrera, fecha_nacimiento, fecha_ingreso) values
('Sebastián Mejía Pareja', 'sebastian.mejia@gmail.com', 'Masculino', '1001001001', 'Ingeniería de Datos', '2003-03-03', '2023-01-15'),
('Camila Rodríguez Pérez', 'camila.rodriguez@gmail.com', 'Femenino', '1001001002', 'Ingeniería de Software', '2002-11-20', '2022-07-20'),
('Mateo Giraldo Sánchez', 'mateo.giraldo@gmail.com', 'Masculino', '1001001003', 'Ingeniería de Sistemas', '2001-03-08', '2021-01-18'),
('Isabella Moreno Vargas', 'isabella.moreno@gmail.com', 'Femenino', '1001001004', 'Administración de Empresas', '2000-09-12', '2019-07-22'),
('Juan Esteban Castaño', 'juan.castano@gmail.com', 'Masculino', '1001001005', 'Contaduría Pública', '2002-02-27', '2022-01-17'),
('Valeria Jiménez Ospina', 'valeria.jimenez@gmail.com', 'Femenino', '1001001006', 'Ingeniería de Datos', '2003-07-30', '2023-01-15'),
('Daniel Quintero Ríos', 'daniel.quintero@gmail.com', 'Masculino', '1001001007', 'Ingeniería de Software', '2001-12-05', '2021-07-19'),
('Sofía Arango Londoño', 'sofia.arango@gmail.com', 'Femenino', '1001001008', 'Negocios Digitales', '2002-06-10', '2022-07-20'),
('Alejandro Vásquez Ruiz', 'alejandro.vasquez@gmail.com', 'Masculino', '1001001009', 'Ingeniería de Sistemas', '2000-01-25', '2019-01-21'),
('Luciana Fernández Castro', 'luciana.fernandez@gmail.com', 'Femenino', '1001001010', 'Psicología Organizacional', '2003-04-18', '2023-07-24'),
('Kevin Andrés Salazar', 'kevin.salazar@gmail.com', 'Masculino', '1001001011', 'Ingeniería de Datos', '2004-02-11', '2024-01-16'),
('Mariana Patiño Ruiz', 'mariana.patino@gmail.com', 'Femenino', '1001001012', 'Ingeniería de Software', '2003-08-19', '2023-07-18'),
('Esteban Morales Cano', 'esteban.morales@gmail.com', 'Masculino', '1001001013', 'Ingeniería de Sistemas', '2002-03-21', '2022-01-17'),
('Paula Andrea Vélez', 'paula.velez@gmail.com', 'Femenino', '1001001014', 'Administración de Empresas', '2001-10-09', '2021-07-21'),
('Cristian David Henao', 'cristian.henao@gmail.com', 'Masculino', '1001001015', 'Contaduría Pública', '2003-01-30', '2023-01-16'),
('Laura Sofía Cárdenas', 'laura.cardenas@gmail.com', 'Femenino', '1001001016', 'Ingeniería de Datos', '2004-06-25', '2024-07-22'),
('Miguel Ángel Bustamante', 'miguel.bustamante@gmail.com', 'Masculino', '1001001017', 'Ingeniería de Software', '2002-12-14', '2022-07-19'),
('Sara Valentina Osorio', 'sara.osorio@gmail.com', 'Femenino', '1001001018', 'Negocios Digitales', '2003-03-03', '2023-01-16'),
('David Felipe Navarro', 'david.navarro@gmail.com', 'Masculino', '1001001019', 'Ingeniería de Sistemas', '2001-05-28', '2021-01-18'),
('Juliana Rojas Montoya', 'juliana.rojas@gmail.com', 'Femenino', '1001001020', 'Psicología Organizacional', '2004-09-07', '2024-01-16'),
('Andrés Camilo Franco', 'andres.franco@gmail.com', 'Masculino', '1001001021', 'Ingeniería de Datos', '2003-11-15', '2023-07-18'),
('Natalia Gómez Londoño', 'natalia.gomez@gmail.com', 'Femenino', '1001001022', 'Ingeniería de Software', '2002-04-10', '2022-01-17'),
('Juan José Bermúdez', 'juan.bermudez@gmail.com', 'Masculino', '1001001023', 'Ingeniería de Sistemas', '2000-08-22', '2019-07-22'),
('Valentina Duque Restrepo', 'valentina.duque@gmail.com', 'Femenino', '1001001024', 'Administración de Empresas', '2003-02-17', '2023-01-16'),
('Felipe Giraldo Herrera', 'felipe.giraldo@gmail.com', 'Masculino', '1001001025', 'Contaduría Pública', '2002-06-01', '2022-07-19'),
('María Paula Escobar', 'maria.escobar@gmail.com', 'Femenino', '1001001026', 'Ingeniería de Datos', '2004-04-29', '2024-01-16'),
('Sebastián Ocampo Ruiz', 'sebastian.ocampo@gmail.com', 'Masculino', '1001001027', 'Ingeniería de Software', '2001-09-18', '2021-07-21'),
('Daniela Castro Álvarez', 'daniela.castro@gmail.com', 'Femenino', '1001001028', 'Negocios Digitales', '2003-12-02', '2023-07-18'),
('Tomás Echavarría López', 'tomas.echavarria@gmail.com', 'Masculino', '1001001029', 'Ingeniería de Sistemas', '2002-07-13', '2022-01-17'),
('Gabriela Martínez Salas', 'gabriela.martinez@gmail.com', 'Femenino', '1001001030', 'Psicología Organizacional', '2004-05-05', '2024-07-22');


insert into docentes (nombre_completo, correo_institucional, departamento_academico, anios_experiencia) values
('Carlos Andrés Gómez', 'carlos.gomez@universidad.edu.co', 'Departamento de Ingeniería y Tecnología', 8),
('Laura Martínez Ríos', 'laura.martinez@universidad.edu.co', 'Departamento de Ingeniería y Tecnología', 5),
('Santiago Restrepo Díaz', 'santiago.restrepo@universidad.edu.co', 'Departamento de Ingeniería y Tecnología', 10),
('Valentina Torres Mejía', 'valentina.torres@universidad.edu.co', 'Departamento de Ciencias Empresariales', 7),
('Juan Pablo Herrera', 'juan.herrera@universidad.edu.co', 'Departamento de Ciencias Empresariales', 12),
('María Fernanda López', 'maria.lopez@universidad.edu.co', 'Departamento de Ciencias Básicas', 9),
('Andrés Felipe Ruiz', 'andres.ruiz@universidad.edu.co', 'Departamento de Ciencias Básicas', 6),
('Natalia Cardona Vélez', 'natalia.cardona@universidad.edu.co', 'Departamento de Humanidades y Comunicación', 4),
('Daniela Ramírez Soto', 'daniela.ramirez@universidad.edu.co', 'Departamento de Humanidades y Comunicación', 3),
('Felipe Álvarez Castro', 'felipe.alvarez@universidad.edu.co', 'Departamento de Ingeniería y Tecnología', 15);



insert into cursos (id_docente, nombre, codigo, creditos, semestre) values
-- Ingeniería de Datos
(1, 'Fundamentos de Programación en Python', 'ID101', 3, 1),
(1, 'Bases de Datos Relacionales', 'ID202', 3, 2),
(2, 'SQL Avanzado', 'ID303', 3, 3),
(3, 'ETL y Procesamiento de Datos', 'ID404', 4, 4),
(10, 'Big Data', 'ID505', 4, 5),
(10, 'Visualización de Datos', 'ID506', 3, 6),

-- Ingeniería de Software
(2, 'Programación Orientada a Objetos', 'IS201', 3, 2),
(3, 'Desarrollo Web con JavaScript', 'IS302', 3, 3),+
(10, 'Arquitectura de Software', 'IS403', 4, 4),
(1, 'Pruebas de Software', 'IS404', 3, 5),

-- Ingeniería de Sistemas
(3, 'Sistemas Operativos', 'SI201', 3, 2),
(2, 'Redes de Computadores', 'SI302', 3, 3),
(10, 'Computación en la Nube', 'SI403', 4, 4),

-- Ciencias Empresariales
(4, 'Fundamentos de Administración', 'CE101', 3, 1),
(4, 'Gestión de Proyectos', 'CE202', 3, 2),
(5, 'Contabilidad Financiera', 'CE203', 3, 2),
(5, 'Análisis Financiero', 'CE304', 3, 3),

-- Ciencias Básicas
(6, 'Cálculo Diferencial', 'CB101', 4, 1),
(6, 'Álgebra Lineal', 'CB102', 4, 1),
(7, 'Probabilidad y Estadística', 'CB203', 3, 2),

-- Humanidades
(8, 'Comunicación Organizacional', 'CH101', 2, 1),
(9, 'Ética y Responsabilidad Profesional', 'CH102', 2, 1);


insert into inscripciones (id_estudiante, id_curso, fecha_inscripcion, calificacion_final) values

-- ingeniería de datos

(1, 1, '2023-01-20', 4.2),
(1, 2, '2023-07-18', 4.4),
(1, 3, '2024-01-22', 4.0),

(6, 1, '2023-01-20', 3.5),
(6, 2, '2023-07-18', 3.8),
(6, 4, '2024-01-22', 4.3),

(11, 1, '2024-01-18', 4.6),
(11, 2, '2024-07-20', 4.1),

(16, 1, '2024-07-22', 3.9),

(21, 2, '2023-07-20', 4.3),
(21, 3, '2024-01-25', 4.7),

(26, 1, '2024-01-18', 4.4),

-- ingeniería de software

(2, 7, '2022-07-25', 4.1),
(2, 8, '2023-01-20', 4.5),
(2, 9, '2023-07-21', 4.0),

(7, 7, '2021-07-25', 3.6),
(7, 8, '2022-01-20', 3.9),

(12, 7, '2023-07-25', 4.2),

(17, 7, '2022-07-25', 3.2),
(17, 8, '2023-01-20', 3.8),

(22, 7, '2022-01-20', 4.6),

(27, 7, '2021-07-25', 3.5),
(27, 10, '2022-01-20', 4.0),

-- ingeniería de sistemas

(3, 11, '2021-01-22', 3.9),
(3, 12, '2021-07-20', 3.4),

(9, 11, '2019-01-25', 2.8),
(9, 12, '2019-07-22', 3.3),

(13, 11, '2022-01-22', 4.2),

(19, 11, '2021-01-22', 3.8),

(23, 11, '2019-07-22', 4.5),

(29, 12, '2022-01-22', 4.0),

-- ciencias empresariales

(4, 14, '2019-07-25', 4.6),
(4, 15, '2020-01-20', 4.2),

(14, 14, '2021-07-25', 3.9),

(24, 15, '2023-01-20', 4.3),

(5, 16, '2022-01-20', 3.0),
(5, 17, '2022-07-19', 3.6),

(15, 16, '2023-01-20', 3.8),

(25, 17, '2022-07-19', 4.1),

-- ciencias básicas

(1, 18, '2023-01-20', 4.5),

(2, 18, '2022-07-25', 3.9),

(3, 19, '2021-01-22', 3.4),

(11, 20, '2024-01-18', 4.8),

-- humanidades

(8, 21, '2022-07-25', 4.3),

(28, 21, '2023-07-20', 4.0),

(10, 22, '2023-07-24', 4.9),

(30, 22, '2024-07-22', 4.6);



-- TASK 3

-- 1. Listar todos los estudiantes con sus inscripciones y cursos (JOIN).
select 
	e.id_estudiante,
	e.nombre_completo as estudiante,
	e.carrera,
	c.nombre as curso,
	c.codigo as codigo_curso,
	i.fecha_inscripcion,
	i.calificacion_final 
from estudiantes e
left join inscripciones i on e.id_estudiante = i.id_estudiante 
left join cursos c on c.id_curso = i.id_curso
order by e.id_estudiante;


-- 2. Listar cursos dictados por docentes con > 5 años de experiencia.
select 
    c.id_curso,
    c.nombre as curso,
    c.codigo,
    d.nombre_completo as docente,
    d.anios_experiencia
from cursos c
join docentes d on c.id_docente = d.id_docente
where d.anios_experiencia > 5
order by d.anios_experiencia desc;


-- 3. Obtener promedio de calificaciones por curso (GROUP BY + AVG).
select 
	c.id_curso,
	c.nombre as curso,
	c.codigo,
	count(i.id_inscripcion) as total_inscritos,
	min(i.calificacion_final) as calificacion_minima,
	max(i.calificacion_final) as calificacion_maxima,
	round(avg(i.calificacion_final), 1) as promedio
from cursos c 
left join inscripciones i on i.id_curso = c.id_curso 
group by c.id_curso, c.nombre, c.codigo 
order by promedio desc; 


-- 4. Mostrar estudiantes inscritos en más de un curso (HAVING COUNT(*) > 1).
select 
	e.id_estudiante,
	e.nombre_completo as estudiante,
	count(i.id_curso) as total_cursos
from estudiantes e 
left join inscripciones i on e.id_estudiante = i.id_estudiante
group by e.id_estudiante, e.nombre_completo 
having count(i.id_curso ) > 1
order by total_cursos desc;


-- 5. ALTER TABLE: agregar columna estado_academico a estudiantes.
alter table estudiantes 
add column estado_academico varchar(20)
check (estado_academico in('Activo', 'Inactivo', 'Graduado', 'Retirado'))
default 'Activo';


-- 6. Eliminar un docente y observar el efecto en cursos (revisar ON DELETE en la FK).
-- La Fk en la tabla cursos está definida como "on delete restrict" lo que sigmifica que no se puede eliminar un docente si tiene cursos asignados.


-- 7. Consultar cursos con más de 2 estudiantes inscritos (GROUP BY + COUNT + HAVING).
select 
	c.id_curso,
	c.nombre as curso,
	count(i.id_estudiante) as total_estudiantes
from cursos c  
join inscripciones i on i.id_curso = c.id_curso
group by c.id_curso, c.nombre
having count(i.id_estudiante) > 2
order by total_estudiantes desc;


-- TASK 4

-- 1. Estudiantes cuya calificación promedio sea > promedio general (AVG() + subconsulta).
select  
    round(avg(calificacion_final), 1) as promedio_general
from inscripciones;

select 
    e.id_estudiante,
    e.nombre_completo,
    round(avg(i.calificacion_final), 1) as promedio_estudiante
from estudiantes e
join inscripciones i on e.id_estudiante = i.id_estudiante
group by e.id_estudiante, e.nombre_completo
having avg(i.calificacion_final) > (
    select avg(calificacion_final)
    from inscripciones
)
order by promedio_estudiante desc;


-- 2. Nombres de carreras con estudiantes inscritos en cursos del semestre ≥ 2 (IN o EXISTS).
select distinct e.carrera
from estudiantes e
where exists (
    select 1
    from inscripciones i
    join cursos c on i.id_curso = c.id_curso
    where i.id_estudiante = e.id_estudiante
    and c.semestre >= 2
);


-- 3. Usar ROUND, SUM, MAX, MIN, COUNT para obtener indicadores.

-- 3.1 Promedio general redondeado
select  
    round(avg(calificacion_final), 1) as promedio_general
from inscripciones;

-- 3.2 Total de estudiantes inscritos
select 
    count(distinct id_estudiante) as total_estudiantes_con_inscripcion
from inscripciones;

-- 3.3 Nota más alta y más baja
select  
    max(calificacion_final) as nota_maxima,
    min(calificacion_final) as nota_minima
from inscripciones;

-- 3.4 Total de inscripciones por carrera
select 
    e.carrera,
    COUNT(i.id_inscripcion) as total_inscripciones
from estudiantes e
join inscripciones i on e.id_estudiante = i.id_estudiante
group by e.carrera
order by total_inscripciones desc;

-- 3.5 Suma total de créditos cursados por estudiante
select 
    e.carrera,
    COUNT(i.id_inscripcion) as total_inscripciones
from estudiantes e
join inscripciones i on e.id_estudiante = i.id_estudiante
group by e.carrera
order by total_inscripciones desc;


-- TASK 5

-- Crea la vista vista_historial_academico que muestre: nombre del estudiante, 
-- nombre del curso, nombre del docente, semestre y calificación final.

create view vista_historial_academico as
select 
    e.nombre_completo as nombre_estudiante,
    c.nombre,
    d.id_docente,
    c.semestre,
    i.calificacion_final
from estudiantes e
join inscripciones i
    on e.id_estudiante = i.id_estudiante
join cursos c
    on i.id_curso = c.id_curso
join docentes d on c.id_docente = d.id_docente;

select * from vista_historial_academico;

-- TASK 6

-- 1. Otorga permisos de solo lectura a un rol revisor_academico sobre la vista (GRANT SELECT).

-- crear el rol si no existe
do $$
begin
   if not exists (
      select from pg_roles where rolname = 'revisor_academico'
   ) then
      create role revisor_academico;
   end if;
end
$$;

-- otorgar permiso de solo lectura sobre la vista
grant select on vista_historial_academico to revisor_academico;

-- 2. Revoca permisos de modificación de datos en inscripciones para ese rol (REVOKE).
revoke insert, update, delete
on inscripciones
from revisor_academico;

-- 3. Simula actualización de calificaciones usando BEGIN, SAVEPOINT, ROLLBACK y COMMIT.
begin;

-- primera actualización
update inscripciones
set calificacion_final = 4.5
where id_inscripcion = 1;

savepoint punto_seguridad_1;

-- segunda actualización
update inscripciones
set calificacion_final = 2.0
where id_inscripcion = 2;

-- simulamos que algo salió mal
rollback to savepoint punto_seguridad_1;

-- tercera actualización válida
update inscripciones
set calificacion_final = 4.8
where id_inscripcion = 3;

commit;
