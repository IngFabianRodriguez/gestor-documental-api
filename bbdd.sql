-- Adminer 4.8.1 PostgreSQL 14.2 (Debian 14.2-1.pgdg110+1) dump

DROP TABLE IF EXISTS "gd_archivos";
DROP SEQUENCE IF EXISTS gd_archivos_id_archivo_seq;
CREATE SEQUENCE gd_archivos_id_archivo_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1;

CREATE TABLE "public"."gd_archivos" (
    "id_archivo" bigint DEFAULT nextval('gd_archivos_id_archivo_seq') NOT NULL,
    "path_archivo" character varying(200),
    "file_64" text,
    "type_file" character varying(200),
    "timestamp" timestamp,
    "documento_relacionado" bigint,
    CONSTRAINT "gd_archivos_pkey" PRIMARY KEY ("id_archivo")
) WITH (oids = false);


DROP TABLE IF EXISTS "gd_area";
DROP SEQUENCE IF EXISTS gd_area_id_area_seq;
CREATE SEQUENCE gd_area_id_area_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_area" (
    "id_area" integer DEFAULT nextval('gd_area_id_area_seq') NOT NULL,
    "nombre_area" character varying(50) NOT NULL,
    CONSTRAINT "gd_area_pkey" PRIMARY KEY ("id_area")
) WITH (oids = false);

INSERT INTO "gd_area" ("id_area", "nombre_area") VALUES
(1,	'admin');

DROP TABLE IF EXISTS "gd_ciudad";
DROP SEQUENCE IF EXISTS gd_ciudad_id_ciudad_seq;
CREATE SEQUENCE gd_ciudad_id_ciudad_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_ciudad" (
    "id_ciudad" integer DEFAULT nextval('gd_ciudad_id_ciudad_seq') NOT NULL,
    "nombre_ciudad" character varying(50) NOT NULL,
    "departamento_ciudad" integer,
    CONSTRAINT "gd_ciudad_pkey" PRIMARY KEY ("id_ciudad")
) WITH (oids = false);

INSERT INTO "gd_ciudad" ("id_ciudad", "nombre_ciudad", "departamento_ciudad") VALUES
(1,	'Bogota',	1);

DROP TABLE IF EXISTS "gd_comentarios_documentos";
DROP SEQUENCE IF EXISTS gd_comentarios_documentos_id_comentario_seq;
CREATE SEQUENCE gd_comentarios_documentos_id_comentario_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_comentarios_documentos" (
    "id_comentario" integer DEFAULT nextval('gd_comentarios_documentos_id_comentario_seq') NOT NULL,
    "comentario_documento" character varying(50) NOT NULL,
    "documento_comentario" integer,
    "usuario_comentario" integer,
    "timestamp" timestamp,
    CONSTRAINT "gd_comentarios_documentos_pkey" PRIMARY KEY ("id_comentario")
) WITH (oids = false);


DROP TABLE IF EXISTS "gd_departamento";
DROP SEQUENCE IF EXISTS gd_departamento_id_departamento_seq;
CREATE SEQUENCE gd_departamento_id_departamento_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_departamento" (
    "id_departamento" integer DEFAULT nextval('gd_departamento_id_departamento_seq') NOT NULL,
    "nombre_departamento" character varying(50) NOT NULL,
    CONSTRAINT "gd_departamento_pkey" PRIMARY KEY ("id_departamento")
) WITH (oids = false);

INSERT INTO "gd_departamento" ("id_departamento", "nombre_departamento") VALUES
(1,	'cundinamarca');

DROP TABLE IF EXISTS "gd_documentos";
DROP SEQUENCE IF EXISTS gd_documentos_id_documento_seq;
CREATE SEQUENCE gd_documentos_id_documento_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_documentos" (
    "id_documento" integer DEFAULT nextval('gd_documentos_id_documento_seq') NOT NULL,
    "nombre_documento" character varying(50) NOT NULL,
    "estado_documento" integer,
    "ciudad_documento" integer,
    "departamento_documento" integer,
    "usuario_radicado" integer,
    "timestamp" timestamp,
    CONSTRAINT "gd_documentos_pkey" PRIMARY KEY ("id_documento")
) WITH (oids = false);


DROP TABLE IF EXISTS "gd_documentos_user_asignados";
DROP SEQUENCE IF EXISTS gd_documentos_user_asignados_id_asignacion_seq;
CREATE SEQUENCE gd_documentos_user_asignados_id_asignacion_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_documentos_user_asignados" (
    "id_asignacion" integer DEFAULT nextval('gd_documentos_user_asignados_id_asignacion_seq') NOT NULL,
    "documento_asignado" integer,
    "id_usuario" integer,
    "timestamp" timestamp,
    CONSTRAINT "gd_documentos_user_asignados_pkey" PRIMARY KEY ("id_asignacion")
) WITH (oids = false);


DROP TABLE IF EXISTS "gd_estados";
DROP SEQUENCE IF EXISTS gd_estados_id_estado_seq;
CREATE SEQUENCE gd_estados_id_estado_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_estados" (
    "id_estado" integer DEFAULT nextval('gd_estados_id_estado_seq') NOT NULL,
    "nombre_estado" character varying(50) NOT NULL,
    CONSTRAINT "gd_estados_pkey" PRIMARY KEY ("id_estado")
) WITH (oids = false);


DROP TABLE IF EXISTS "gd_roles";
DROP SEQUENCE IF EXISTS gd_roles_id_rol_seq;
CREATE SEQUENCE gd_roles_id_rol_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_roles" (
    "id_rol" integer DEFAULT nextval('gd_roles_id_rol_seq') NOT NULL,
    "nombre_rol" character varying(50) NOT NULL,
    CONSTRAINT "gd_roles_pkey" PRIMARY KEY ("id_rol")
) WITH (oids = false);

INSERT INTO "gd_roles" ("id_rol", "nombre_rol") VALUES
(1,	'radicador'),
(2,	'gestion'),
(3,	'administrador');

DROP TABLE IF EXISTS "gd_usuarios";
DROP SEQUENCE IF EXISTS gd_usuarios_documento_usuario_seq;
CREATE SEQUENCE gd_usuarios_documento_usuario_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_usuarios" (
    "documento_usuario" integer DEFAULT nextval('gd_usuarios_documento_usuario_seq') NOT NULL,
    "nombre_usuario" character varying(50),
    "apellido_usuario" character varying(50),
    "correo_usuario" character varying(50),
    "celular_usuario" character varying(50),
    "ciudad_usuario" integer,
    "departamento_usuario" integer,
    "area_usuario" integer,
    "rol_usuario" integer,
    CONSTRAINT "gd_usuarios_pkey" PRIMARY KEY ("documento_usuario")
) WITH (oids = false);

INSERT INTO "gd_usuarios" ("documento_usuario", "nombre_usuario", "apellido_usuario", "correo_usuario", "celular_usuario", "ciudad_usuario", "departamento_usuario", "area_usuario", "rol_usuario") VALUES
(1032485299,	'Hector Fabian',	'Rodriguez Acosta',	'mccracflow@gmail.com',	'3182019761',	1,	1,	1,	1),
(321321,	'Juan',	'Montaño',	'juan@montaño.com',	'314444111',	1,	1,	1,	1),
(3213211,	'Manuel',	'Cabulla',	'manuel@cabulla.com',	'314444112',	1,	1,	1,	2),
(3213212,	'Oscar',	'Capera',	'oscar@capera.com',	'314444113',	1,	1,	1,	3);

DROP TABLE IF EXISTS "gd_usuarios_login";
DROP SEQUENCE IF EXISTS gd_usuarios_login_id_usuario_login_seq;
CREATE SEQUENCE gd_usuarios_login_id_usuario_login_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."gd_usuarios_login" (
    "id_usuario_login" integer DEFAULT nextval('gd_usuarios_login_id_usuario_login_seq') NOT NULL,
    "password_usuario" character varying(50),
    "usuario_rel" integer,
    CONSTRAINT "gd_usuarios_login_pkey" PRIMARY KEY ("id_usuario_login")
) WITH (oids = false);

INSERT INTO "gd_usuarios_login" ("id_usuario_login", "password_usuario", "usuario_rel") VALUES
(1,	'fabian17+',	1032485299),
(2,	'321321',	321321),
(3,	'3213211',	3213211),
(4,	'3213212',	3213212);

ALTER TABLE ONLY "public"."gd_archivos" ADD CONSTRAINT "gd_archivos_documento_relacionado_fkey" FOREIGN KEY (documento_relacionado) REFERENCES gd_documentos(id_documento) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."gd_ciudad" ADD CONSTRAINT "gd_ciudad_departamento_ciudad_fkey" FOREIGN KEY (departamento_ciudad) REFERENCES gd_departamento(id_departamento) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."gd_comentarios_documentos" ADD CONSTRAINT "gd_comentarios_documentos_documento_comentario_fkey" FOREIGN KEY (documento_comentario) REFERENCES gd_documentos(id_documento) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_comentarios_documentos" ADD CONSTRAINT "gd_comentarios_documentos_usuario_comentario_fkey" FOREIGN KEY (usuario_comentario) REFERENCES gd_usuarios(documento_usuario) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."gd_documentos" ADD CONSTRAINT "gd_documentos_ciudad_documento_fkey" FOREIGN KEY (ciudad_documento) REFERENCES gd_ciudad(id_ciudad) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_documentos" ADD CONSTRAINT "gd_documentos_departamento_documento_fkey" FOREIGN KEY (departamento_documento) REFERENCES gd_departamento(id_departamento) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_documentos" ADD CONSTRAINT "gd_documentos_estado_documento_fkey" FOREIGN KEY (estado_documento) REFERENCES gd_estados(id_estado) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_documentos" ADD CONSTRAINT "gd_documentos_usuario_radicado_fkey" FOREIGN KEY (usuario_radicado) REFERENCES gd_usuarios(documento_usuario) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."gd_documentos_user_asignados" ADD CONSTRAINT "gd_documentos_user_asignados_documento_asignado_fkey" FOREIGN KEY (documento_asignado) REFERENCES gd_documentos(id_documento) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_documentos_user_asignados" ADD CONSTRAINT "gd_documentos_user_asignados_id_usuario_fkey" FOREIGN KEY (id_usuario) REFERENCES gd_usuarios(documento_usuario) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."gd_usuarios" ADD CONSTRAINT "gd_usuarios_area_usuario_fkey" FOREIGN KEY (area_usuario) REFERENCES gd_area(id_area) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_usuarios" ADD CONSTRAINT "gd_usuarios_ciudad_usuario_fkey" FOREIGN KEY (ciudad_usuario) REFERENCES gd_ciudad(id_ciudad) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_usuarios" ADD CONSTRAINT "gd_usuarios_departamento_usuario_fkey" FOREIGN KEY (departamento_usuario) REFERENCES gd_departamento(id_departamento) NOT DEFERRABLE;
ALTER TABLE ONLY "public"."gd_usuarios" ADD CONSTRAINT "gd_usuarios_rol_usuario_fkey" FOREIGN KEY (rol_usuario) REFERENCES gd_roles(id_rol) NOT DEFERRABLE;

ALTER TABLE ONLY "public"."gd_usuarios_login" ADD CONSTRAINT "gd_usuarios_login_usuario_rel_fkey" FOREIGN KEY (usuario_rel) REFERENCES gd_usuarios(documento_usuario) NOT DEFERRABLE;

-- 2022-04-22 23:47:25.828733+00