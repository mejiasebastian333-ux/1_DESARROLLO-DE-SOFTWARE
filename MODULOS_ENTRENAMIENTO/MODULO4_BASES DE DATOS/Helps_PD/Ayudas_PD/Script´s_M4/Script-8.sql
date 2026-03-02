
set search_path to gestion_academica_universidad;

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
	calificacion_final numeric(5,2) check (calificacion_final between 0 and 100),
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




