from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

ID_DEPARTAMENTO = "gd_departamento.id_departamento"
ID_USUARIO = "gd_usuarios.documento_usuario"
ID_DOCUMENTO = "gd_documentos.id_documento"
ID_ROLES = "gd_roles.id_rol"
ID_AREAS = "gd_area.id_area"
ID_CIUDAD = "gd_ciudad.id_ciudad"
ID_DEPARTAMENTO = "gd_departamento.id_departamento"
ID_ARCHIVOS = "gd_archivos.id_archivo"
ID_ESTADOS = "gd_estados.id_estado"


class gd_roles(db.Model):
    __tablename__ = "gd_roles"
    id_rol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), nullable=False)
    usuario = db.relationship("gd_usuarios")

    def __init__(self, nombre_rol):
        self.nombre_rol = nombre_rol


class gd_roles_schema(ma.Schema):
    class Meta:
        fields = ("id_rol", "nombre_rol")


class gd_usuarios(db.Model):
    __tablename__ = "gd_usuarios"
    documento_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50))
    apellido_usuario = db.Column(db.String(50))
    correo_usuario = db.Column(db.String(50))
    celular_usuario = db.Column(db.String(50))
    ciudad_usuario = db.Column(db.Integer, db.ForeignKey(ID_CIUDAD))
    departamento_usuario = db.Column(db.Integer, db.ForeignKey(ID_DEPARTAMENTO))
    area_usuario = db.Column(db.Integer, db.ForeignKey(ID_AREAS))
    rol_usuario = db.Column(db.Integer, db.ForeignKey(ID_ROLES))
    documentos = db.relationship("gd_documentos")
    comentarios_documentos = db.relationship("gd_comentarios_documentos")
    contraseña = db.relationship("gd_usuarios_login")
    documentos_asignados = db.relationship("gd_documentos_user_asignados")

    def __init__(
        self,
        documento_usuario,
        nombre_usuario,
        apellido_usuario,
        correo_usuario,
        celular_usuario,
        ciudad_usuario,
        departamento_usuario,
        area_usuario,
        rol_usuario,
    ):
        self.documento_usuario = documento_usuario
        self.nombre_usuario = nombre_usuario
        self.apellido_usuario = apellido_usuario
        self.correo_usuario = correo_usuario
        self.celular_usuario = celular_usuario
        self.ciudad_usuario = ciudad_usuario
        self.departamento_usuario = departamento_usuario
        self.area_usuario = area_usuario
        self.rol_usuario = rol_usuario


class gd_usuarios_schema(ma.Schema):
    class Meta:
        fields = (
            "documento_usuario",
            "nombre_usuario",
            "apellido_usuario",
            "correo_usuario",
            "celular_usuario",
            "ciudad_usuario",
            "departamento_usuario",
            "rol_usuario",
        )


class gd_usuarios_login(db.Model):
    __tablename__ = "gd_usuarios_login"
    id_usuario_login = db.Column(db.Integer, primary_key=True)
    password_usuario = db.Column(db.String(50))
    usuario_rel = db.Column(db.Integer, db.ForeignKey(ID_USUARIO))

    def __init__(self, password_usuario, usuario_rel):
        self.password_usuario = password_usuario
        self.usuario_rel = usuario_rel


class gd_usuarios_login_schema(ma.Schema):
    class Meta:
        fields = ("id_usuario_login", "password_usuario", "usuario_rel")


class gd_documentos(db.Model):
    __tablename__ = "gd_documentos"
    id_documento = db.Column(db.Integer, primary_key=True)
    nombre_documento = db.Column(db.String(50), nullable=False)
    estado_documento = db.Column(db.Integer, db.ForeignKey(ID_ESTADOS))
    ciudad_documento = db.Column(db.Integer, db.ForeignKey(ID_CIUDAD))
    departamento_documento = db.Column(db.Integer, db.ForeignKey(ID_DEPARTAMENTO))
    usuario_radicado = db.Column(db.Integer, db.ForeignKey(ID_USUARIO))
    timestamp = db.Column(db.DateTime)
    archivos = db.relationship("gd_archivos")
    comentarios_documentos = db.relationship("gd_comentarios_documentos")
    gd_usuarios_documentos = db.relationship("gd_documentos_user_asignados")

    def __init__(
        self,
        id_documento,
        nombre_documento,
        estado_documento,
        ciudad_documento,
        departamento_documento,
        usuario_radicado,
        timestamp,
    ):
        self.id_documento = id_documento
        self.nombre_documento = nombre_documento
        self.estado_documento = estado_documento
        self.ciudad_documento = ciudad_documento
        self.departamento_documento = departamento_documento
        self.usuario_radicado = usuario_radicado
        self.timestamp = timestamp


class gd_documentos_schema(ma.Schema):
    class Meta:
        fields = (
            "id_documento",
            "nombre_documento",
            "estado_documento",
            "ciudad_documento",
            "departamento_documento",
            "usuario_radicado",
            "timestamp",
        )


class gd_estados(db.Model):
    __tablename__ = "gd_estados"
    id_estado = db.Column(db.Integer, primary_key=True)
    nombre_estado = db.Column(db.String(50), nullable=False)
    documentos = db.relationship("gd_documentos")

    def __init__(self, nombre_estado):
        self.nombre_estado = nombre_estado


class gd_estados_schema(ma.Schema):
    class Meta:
        fields = ("id_estado", "nombre_estado")


class gd_ciudad(db.Model):
    __tablename__ = "gd_ciudad"
    id_ciudad = db.Column(db.Integer, primary_key=True)
    nombre_ciudad = db.Column(db.String(50), nullable=False)
    departamento_ciudad = db.Column(db.Integer, db.ForeignKey(ID_DEPARTAMENTO))
    usuarios = db.relationship("gd_usuarios")
    documentos = db.relationship("gd_documentos")

    def __init__(self, nombre_ciudad, departamento_ciudad):
        self.nombre_ciudad = nombre_ciudad
        self.departamento_ciudad = departamento_ciudad


class gd_ciudad_schema(ma.Schema):
    class Meta:
        fields = ("id_ciudad", "nombre_ciudad", "departamento_ciudad")


class gd_departamento(db.Model):
    __tablename__ = "gd_departamento"
    id_departamento = db.Column(db.Integer, primary_key=True)
    nombre_departamento = db.Column(db.String(50), nullable=False)
    usuarios = db.relationship("gd_usuarios")
    documentos = db.relationship("gd_documentos")

    def __init__(self, nombre_departamento):
        self.nombre_departamento = nombre_departamento


class gd_departamento_schema(ma.Schema):
    class Meta:
        fields = ("id_departamento", "nombre_departamento")


class gd_area(db.Model):
    __tablename__ = "gd_area"
    id_area = db.Column(db.Integer, primary_key=True)
    nombre_area = db.Column(db.String(50), nullable=False)
    usuario = db.relationship("gd_usuarios")

    def __init__(self, nombre_area):
        self.nombre_area = nombre_area


class gd_area_schema(ma.Schema):
    class Meta:
        fields = ("id_area", "nombre_area")


class gd_comentarios_documentos(db.Model):
    __tablename__ = "gd_comentarios_documentos"
    id_comentario = db.Column(db.Integer, primary_key=True)
    comentario_documento = db.Column(db.String(50), nullable=False)
    documento_comentario = db.Column(db.Integer, db.ForeignKey(ID_DOCUMENTO))
    usuario_comentario = db.Column(db.Integer, db.ForeignKey(ID_USUARIO))
    timestamp = db.Column(db.DateTime)

    def __init__(
        self, comentario_documento, documento_comentario, usuario_comentario, timestamp
    ):
        self.comentario_documento = comentario_documento
        self.documento_comentario = documento_comentario
        self.usuario_comentario = usuario_comentario
        self.timestamp = timestamp


class gd_comentarios_documentos_schema(ma.Schema):
    class Meta:
        fields = (
            "id_comentario",
            "comentario_documento",
            "documento_comentario",
            "usuario_comentario",
        )


class gd_archivos(db.Model):
    __tablename__ = "gd_archivos"
    id_archivo = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    path_archivo = db.Column(db.String(200))
    file_64 = db.Column(db.Text())
    type_file = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime)
    documento_relacionado = db.Column(db.BigInteger, db.ForeignKey(ID_DOCUMENTO))

    def __init__(
        self,
        path_archivo,
        file_64,
        type_file,
        documento_relacionado,
        nh_user,
        nh_name,
        timestamp,
    ):
        self.path_archivo = path_archivo
        self.file_64 = file_64
        self.type_file = type_file
        self.documento_relacionado = documento_relacionado
        self.nh_name = nh_name
        self.nh_user = nh_user
        self.timestamp = timestamp


class gd_archivos_schema(ma.Schema):
    class Meta:
        fields = (
            "id_archivo",
            "path_archivo",
            "file_64",
            "type_file",
            "documento_relacionado",
            "timestamp",
        )


class gd_documentos_user_asignados(db.Model):
    __tablename__ = "gd_documentos_user_asignados"
    id_asignacion = db.Column(db.Integer, primary_key=True)
    documento_asignado = db.Column(db.Integer, db.ForeignKey(ID_DOCUMENTO))
    id_usuario = db.Column(db.Integer, db.ForeignKey(ID_USUARIO))
    timestamp = db.Column(db.DateTime)

    def __init__(self, documento_asignado, id_usuario):
        self.documento_asignado = documento_asignado
        self.id_usuario = id_usuario


class gd_documentos_user_asignados_schema(ma.Schema):
    class Meta:
        fields = ("id_asignacion", "documento_asignado", "id_usuario")
