from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

from models import db
from models import (
    gd_roles,
    gd_roles_schema,
    gd_usuarios,
    gd_usuarios_schema,
    gd_usuarios_login,
    gd_usuarios_login_schema,
    gd_documentos,
    gd_documentos_schema,
    gd_estados,
    gd_estados_schema,
    gd_ciudad,
    gd_ciudad_schema,
    gd_departamento,
    gd_departamento_schema,
    gd_area,
    gd_area_schema,
    gd_comentarios_documentos,
    gd_comentarios_documentos_schema,
    gd_archivos,
    gd_archivos_schema,
    gd_documentos_user_asignados,
    gd_documentos_user_asignados_schema,
)

from config import DevelopmentConfig

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

app.config.from_object(DevelopmentConfig)

try:
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.remove()
except RuntimeError:
    raise RuntimeError("Error: Database already exists")


CORS(app, resourses={r"/*": {"origins": "*", "send_wildcard": "False"}})

gd_roles_only = gd_roles_schema()
gd_usuarios_only = gd_usuarios_schema()
gd_usuarios_login_only = gd_usuarios_login_schema()
gd_documentos_only = gd_documentos_schema()
gd_estados_only = gd_estados_schema()
gd_ciudad_only = gd_ciudad_schema()
gd_departamento_only = gd_departamento_schema()
gd_area_only = gd_area_schema()
gd_comentarios_documento_only = gd_comentarios_documentos_schema()
gd_archivos_only = gd_archivos_schema()
gd_documentos_user_asignados_only = gd_documentos_user_asignados_schema()

gd_roles_many = gd_roles_schema(many=True)
gd_usuarios_many = gd_usuarios_schema(many=True)
gd_usuarios_login_many = gd_usuarios_login_schema(many=True)
gd_documentos_many = gd_documentos_schema(many=True)
gd_estados_many = gd_estados_schema(many=True)
gd_ciudad_many = gd_ciudad_schema(many=True)
gd_departamento_many = gd_departamento_schema(many=True)
gd_area_many = gd_area_schema(many=True)
gd_comentarios_documento_many = gd_comentarios_documentos_schema(many=True)
gd_archivos_many = gd_archivos_schema(many=True)
gd_documentos_user_asignados_many = gd_documentos_user_asignados_schema(many=True)


@app.route("/api/roles", methods=["GET"])
def get_roles():
    try:
        all_items = gd_roles.query.all()
        if all_items:
            result = gd_roles_many.dump(all_items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No hay roles registrados"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/rol/<int:id>", methods=["GET"])
def get_rol_by_id(id):
    try:
        item = gd_roles.query.get(id)
        if item:
            result = gd_roles_only.dump(item)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontró el rol"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/rol/<int:id>", methods=["DELETE"])
def delete_role_by_id(id):
    try:
        item = gd_roles.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Rol eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el rol a borrar"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/new_rol", methods=["POST"])
def create_role():
    try:
        data = request.get_json()
        if data:
            new_item = gd_roles(
                nombre_rol=data["nombre_rol"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_roles_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el rol"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_rol/<int:id>", methods=["PUT"])
def update_rol_by_id(id):
    try:
        data = request.get_json()
        if data:
            item = gd_roles.query.get(id)
            if item:
                item.nombre_rol = data["nombre_rol"]
                db.session.commit()
                return gd_roles_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró el rol a"}), 404
        else:
            return jsonify({"message": "No se recibió el rol"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/usuarios", methods=["GET"])
def get_usuarios():
    try:
        all_users = gd_usuarios.query.all()
        if all_users:
            result = gd_usuarios_many.dump(all_users)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No hay usuarios registrados"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/usuario/<int:documento_usuario>", methods=["GET"])
def get_usuario_by_documento(documento_usuario):
    try:
        item = gd_usuarios.query.filter_by(documento_usuario=documento_usuario).first()
        if item:
            result = gd_usuarios_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify(
                    {
                        "message": "No se encontró el usuario {}".format(
                            documento_usuario
                        )
                    }
                ),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/usuario/<int:documento_usuario>", methods=["DELETE"])
def delete_usuario_by_documento(documento_usuario):
    try:
        item = gd_usuarios.query.filter_by(documento_usuario=documento_usuario).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Usuario eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el usuario a borrar"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/new_usuario", methods=["POST"])
def create_usuario():
    try:
        data = request.get_json()
        if data:
            new_item = gd_usuarios(
                documento_usuario=data["documento_usuario"],
                nombre_usuario=data["nombre_usuario"],
                apellido_usuario=data["apellido_usuario"],
                correo_usuario=data["correo_usuario"],
                celular_usuario=data["celular_usuario"],
                ciudad_usuario=data["ciudad_usuario"],
                departamento_usuario=data["departamento_usuario"],
                area_usuario=data["area_usuario"],
                rol_usuario=data["rol_usuario"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_usuarios_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el usuario solcitado"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_usuario/<int:documento_usuario>", methods=["PUT"])
def update_user_by_documento(documento_usuario):
    try:
        data = request.get_json()
        if data:
            item = gd_usuarios.query.filter_by(
                documento_usuario=documento_usuario
            ).first()
            if item:
                item.nombre_usuario = data["nombre_usuario"]
                item.apellido_usuario = data["apellido_usuario"]
                item.correo_usuario = data["correo_usuario"]
                item.celular_usuario = data["celular_usuario"]
                item.ciudad_usuario = data["ciudad_usuario"]
                item.departamento_usuario = data["departamento_usuario"]
                item.area_usuario = data["area_usuario"]
                item.rol_id = data["rol_id"]
                db.session.commit()
                return gd_usuarios_only.jsonify(item), 200
            else:
                return (
                    jsonify(
                        {
                            "message": "No se encontró el usuario {}".format(
                                documento_usuario
                            )
                        }
                    ),
                    404,
                )
        else:
            return jsonify({"message": "No se recibió el usuario a actualizar"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/usuario_login", methods=["POST"])
def login_usuario():
    try:
        data = request.get_json()
        if data:
            item = gd_usuarios_login.query.filter_by(
                usuario_rel=data["documento_usuario"]
            ).first()
            if item:
                if item.password_usuario == data["password_usuario"]:
                    return jsonify({"message": "Login realizado"}), 200
                else:
                    return jsonify({"message": "Contraseña incorrecta"}), 404
            else:
                return jsonify({"message": "No se encontró el usuario"}), 404
        else:
            return jsonify({"message": "No se recibió el login"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_password", methods=["PUT"])
def update_password():
    try:
        data = request.get_json()
        if data:
            item = gd_usuarios.query.filter_by(
                documento_usuario=data["documento_usuario"]
            ).first()
            if item:
                if item.password_usuario == data["password_usuario"]:
                    item.password_usuario = data["new_password"]
                    db.session.commit()
                    return jsonify({"message": "Contraseña actualizada"}), 200
                else:
                    return jsonify({"message": "Contraseña incorrecta"}), 404
            else:
                return jsonify({"message": "No se encontró el usuario"}), 404
        else:
            return jsonify({"message": "No se recibió el usuario"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_credencial", methods=["POST"])
def create_login():
    try:
        data = request.get_json()
        if data:
            new_item = gd_usuarios_login(
                usuario_rel=data["documento_usuario"],
                password_usuario=data["password_usuario"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_usuarios_login_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el usuario"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/estados", methods=["GET"])
def get_estados():
    try:
        items = gd_estados.query.all()
        if items:
            result = gd_estados_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron estados"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/estado/<int:id_estado>", methods=["GET"])
def get_estado_by_id(id_estado):
    try:
        item = gd_estados.query.filter_by(id_estado=id_estado).first()
        if item:
            result = gd_estados_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify({"message": "No se encontró el estado {}".format(id_estado)}),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_estado", methods=["POST"])
def create_estado():
    try:
        data = request.get_json()
        if data:
            new_item = gd_estados(
                nombre_estado=data["nombre_estado"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_estados_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el estado"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_estado/<int:id_estado>", methods=["PUT"])
def update_estado_by_id(id_estado):
    try:
        data = request.get_json()
        if data:
            item = gd_estados.query.filter_by(id_estado=id_estado).first()
            if item:
                item.nombre_estado = data["nombre_estado"]
                db.session.commit()
                return gd_estados_only.jsonify(item), 200
            else:
                return (
                    jsonify(
                        {"message": "No se encontró el estado {}".format(id_estado)}
                    ),
                    404,
                )
        else:
            return jsonify({"message": "No se recibió el estado"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/delete_estado/<int:id_estado>", methods=["DELETE"])
def delete_estado_by_id(id_estado):
    try:
        item = gd_estados.query.filter_by(id_estado=id_estado).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Estado eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el estado"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/ciudades", methods=["GET"])
def get_ciudades():
    try:
        items = gd_ciudad.query.all()
        if items:
            result = gd_ciudad_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron ciudades"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/ciudad/<int:id_ciudad>", methods=["GET"])
def get_ciudad_by_id(id_ciudad):
    try:
        item = gd_ciudad.query.filter_by(id_ciudad=id_ciudad).first()
        if item:
            result = gd_ciudad_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify({"message": "No se encontró la ciudad {}".format(id_ciudad)}),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_ciudad", methods=["POST"])
def create_ciudad():
    try:
        data = request.get_json()
        if data:
            new_item = gd_ciudad(
                nombre_ciudad=data["nombre_ciudad"],
                departamento_ciudad=data["departamento_ciudad"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_ciudad_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió la ciudad"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_ciudad/<int:id_ciudad>", methods=["PUT"])
def update_ciudad_by_id(id_ciudad):
    try:
        data = request.get_json()
        if data:
            item = gd_ciudad.query.filter_by(id_ciudad=id_ciudad).first()
            if item:
                item.nombre_ciudad = data["nombre_ciudad"]
                item.departamento_ciudad = data["departamento_ciudad"]
                db.session.commit()
                return gd_ciudad_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró la ciudad"}), 404
        else:
            return jsonify({"message": "No se recibió la ciudad"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/delete_ciudad/<int:id_ciudad>", methods=["DELETE"])
def delete_ciudad_by_id(id_ciudad):
    try:
        item = gd_ciudad.query.filter_by(id_ciudad=id_ciudad).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Ciudad eliminada"}), 200
        else:
            return jsonify({"message": "No se encontró la ciudad"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/departamentos", methods=["GET"])
def get_departamentos():
    try:
        items = gd_departamento.query.all()
        if items:
            result = gd_departamento_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron departamentos"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/departamento/<int:id_departamento>", methods=["GET"])
def get_departamento_by_id(id_departamento):
    try:
        item = gd_departamento.query.filter_by(id_departamento=id_departamento).first()
        if item:
            result = gd_departamento_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify(
                    {
                        "message": "No se encontró el departamento {}".format(
                            id_departamento
                        )
                    }
                ),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_departamento", methods=["POST"])
def create_departamento():
    try:
        data = request.get_json()
        if data:
            new_item = gd_departamento(
                nombre_departamento=data["nombre_departamento"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_departamento_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el departamento"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_departamento/<int:id_departamento>", methods=["PUT"])
def update_departamento_by_id(id_departamento):
    try:
        data = request.get_json()
        if data:
            item = gd_departamento.query.filter_by(
                id_departamento=id_departamento
            ).first()
            if item:
                item.nombre_departamento = data["nombre_departamento"]
                db.session.commit()
                return gd_departamento_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró el departamento"}), 404
        else:
            return jsonify({"message": "No se recibió el departamento"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/delete_departamento/<int:id_departamento>", methods=["DELETE"])
def delete_departamento_by_id(id_departamento):
    try:
        item = gd_departamento.query.filter_by(id_departamento=id_departamento).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Departamento eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el departamento"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/areas", methods=["GET"])
def get_areas():
    try:
        items = gd_area.query.all()
        if items:
            result = gd_area_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron areas"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/area/<int:id_area>", methods=["GET"])
def get_area_by_id(id_area):
    try:
        item = gd_area.query.filter_by(id_area=id_area).first()
        if item:
            result = gd_area_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify({"message": "No se encontró el area {}".format(id_area)}),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_area", methods=["POST"])
def create_area():
    try:
        data = request.get_json()
        if data:
            new_item = gd_area(
                nombre_area=data["nombre_area"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_area_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el area"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_area/<int:id_area>", methods=["PUT"])
def update_area_by_id(id_area):
    try:
        data = request.get_json()
        if data:
            item = gd_area.query.filter_by(id_area=id_area).first()
            if item:
                item.nombre_area = data["nombre_area"]
                db.session.commit()
                return gd_area_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró el area"}), 404
        else:
            return jsonify({"message": "No se recibió el area"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/delete_area/<int:id_area>", methods=["DELETE"])
def delete_area_by_id(id_area):
    try:
        item = gd_area.query.filter_by(id_area=id_area).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Area eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el area"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/documentos", methods=["GET"])
def get_documentos():
    try:
        items = gd_documentos.query.all()
        if items:
            result = gd_documentos_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron documentos"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/documento/<int:id_documento>", methods=["GET"])
def get_documento_by_id(id_documento):
    try:
        item = gd_documentos.query.filter_by(id_documento=id_documento).first()
        if item:
            result = gd_documentos_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify(
                    {"message": "No se encontró el documento {}".format(id_documento)}
                ),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_documento", methods=["POST"])
def create_documento():
    try:
        data = request.get_json()
        if data:
            new_item = gd_documentos(
                id_documento=data["id_documento"],
                nombre_documento=data["nombre_documento"],
                estado_documento=data["estado_documento"],
                ciudad_documento=data["ciudad_documento"],
                departamento_documento=data["departamento_documento"],
                usuario_radicado=data["usuario_radicado"],
                timestamp=datetime.now(),
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_documentos_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el documento"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_documento/<int:id_documento>", methods=["PUT"])
def update_documento_by_id(id_documento):
    try:
        data = request.get_json()
        if data:
            item = gd_documentos.query.filter_by(id_documento=id_documento).first()
            if item:
                item.id_documento = data["id_documento"]
                item.nombre_documento = data["nombre_documento"]
                item.estado_documento = data["estado_documento"]
                item.ciudad_documento = data["ciudad_documento"]
                item.departamento_documento = data["departamento_documento"]
                db.session.commit()
                return gd_documentos_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró el documento"}), 404
        else:
            return jsonify({"message": "No se recibió el documento"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/delete_documento/<int:id_documento>", methods=["DELETE"])
def delete_documento_by_id(id_documento):
    try:
        item = gd_documentos.query.filter_by(id_documento=id_documento).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Documento eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el documento"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/comentarios_documentos", methods=["GET"])
def get_comentarios_documento():
    try:
        items = gd_comentarios_documentos.query.all()
        if items:
            result = gd_comentarios_documento_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron comentarios"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/comentario_documento/<int:id_comentario_documento>", methods=["GET"])
def get_comentario_documento_by_id(id_comentario_documento):
    try:
        item = gd_comentarios_documentos.query.filter_by(
            id_comentario_documento=id_comentario_documento
        ).first()
        if item:
            result = gd_comentarios_documento_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify(
                    {
                        "message": "No se encontró el comentario {}".format(
                            id_comentario_documento
                        )
                    }
                ),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_comentario_documento", methods=["POST"])
def create_comentario_documento():
    try:
        data = request.get_json()
        if data:
            new_item = gd_comentarios_documentos(
                comentario_documento=data["comentario_documento"],
                documento_comentario=data["documento_comentario"],
                usuario_comentario=data["usuario_comentario"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_comentarios_documento_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el comentario"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route(
    "/api/update_comentario_documento/<int:id_comentario_documento>", methods=["PUT"]
)
def update_comentario_documento_by_id(id_comentario_documento):
    try:
        data = request.get_json()
        if data:
            item = gd_comentarios_documentos.query.filter_by(
                id_comentario_documento=id_comentario_documento
            ).first()
            if item:
                item.comentario_documento = data["comentario_documento"]
                item.documento_comentario = data["documento_comentario"]
                item.usuario_comentario = data["usuario_comentario"]
                db.session.commit()
                return gd_comentarios_documento_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró el comentario"}), 404
        else:
            return jsonify({"message": "No se recibió el comentario"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route(
    "/api/delete_comentario_documento/<int:id_comentario_documento>", methods=["DELETE"]
)
def delete_comentario_documento_by_id(id_comentario_documento):
    try:
        item = gd_comentarios_documentos.query.filter_by(
            id_comentario_documento=id_comentario_documento
        ).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Comentario eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el comentario"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/archivos", methods=["GET"])
def get_archivos():
    try:
        items = gd_archivos.query.all()
        if items:
            result = gd_archivos_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron archivos"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/archivo/<int:id_archivo>", methods=["GET"])
def get_archivo_by_id(id_archivo):
    try:
        item = gd_archivos.query.filter_by(id_archivo=id_archivo).first()
        if item:
            result = gd_archivos_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify({"message": "No se encontró el archivo {}".format(id_archivo)}),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/create_archivo", methods=["POST"])
def create_archivo():
    try:
        data = request.get_json()
        if data:
            new_item = gd_archivos(
                path_archivo=data["path_archivo"],
                file_64=data["file_64"],
                type_file=data["type_file"],
                timestamp=datetime.now(),
                documento_relacionado=data["documento_relacionado"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_archivos_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el archivo"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/update_archivo/<int:id_archivo>", methods=["PUT"])
def update_archivo_by_id(id_archivo):
    try:
        data = request.get_json()
        if data:
            item = gd_archivos.query.filter_by(id_archivo=id_archivo).first()
            if item:
                item.path_archivo = data["path_archivo"]
                item.file_64 = data["file_64"]
                item.type_file = data["type_file"]
                item.timestamp = datetime.now()
                item.documento_relacionado = data["documento_relacionado"]
                db.session.commit()
                return gd_archivos_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró el archivo"}), 404
        else:
            return jsonify({"message": "No se recibió el archivo"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/delete_archivo/<int:id_archivo>", methods=["DELETE"])
def delete_archivo_by_id(id_archivo):
    try:
        item = gd_archivos.query.filter_by(id_archivo=id_archivo).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({"message": "Archivo eliminado"}), 200
        else:
            return jsonify({"message": "No se encontró el archivo"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/asignacion-documentos", methods=["GET"])
def get_usuarios_documentos():
    try:
        items = gd_documentos_user_asignados.query.all()
        if items:
            result = gd_documentos_user_asignados_many.dump(items)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraron documentos"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/asignacion-documento/<int:id_usuario>", methods=["GET"])
def get_asingnacion_documento_by_id_usuario(id_usuario):
    try:
        item = gd_documentos_user_asignados.query.filter_by(
            id_usuario=id_usuario
        ).first()
        if item:
            result = gd_documentos_user_asignados_only.dump(item)
            return jsonify(result), 200
        else:
            return (
                jsonify({"message": "No se encontraron documentos para el usuario"}),
                404,
            )
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/asignacion-documento/<int:documento_asignado>", methods=["GET"])
def get_asingnacion_documento_by_id_documento(documento_asignado):
    try:
        item = gd_documentos_user_asignados.query.filter_by(
            documento_asignado=documento_asignado
        ).first()
        if item:
            result = gd_documentos_user_asignados_only.dump(item)
            return jsonify(result), 200
        else:
            return jsonify({"message": "No se encontraro el documento"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route("/api/asignacion-documento/create-asignacion", methods=["POST"])
def create_asignacion_documento():
    try:
        data = request.get_json()
        if data:
            new_item = gd_documentos_user_asignados(
                id_usuario=data["id_usuario"],
                documento_asignado=data["documento_asignado"],
                timestamp=data["timestamp"],
            )
            db.session.add(new_item)
            db.session.commit()
            return gd_documentos_user_asignados_only.jsonify(new_item), 201
        else:
            return jsonify({"message": "No se recibió el documento"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route(
    "/api/documento/<documento_asignado>/update-usuario",
    methods=["PUT"],
)
def update_asignacion_documento_by_id_usuario(documento_asignado):
    try:
        data = request.get_json()
        if data:
            item = gd_documentos_user_asignados.query.filter_by(
                documento_asignado=documento_asignado
            ).first()
            if item:
                item.id_usuario = data["id_usuario"]
                db.session.commit()
                return gd_documentos_user_asignados_only.jsonify(item), 200
            else:
                return jsonify({"message": "No se encontró el documento"}), 404
        else:
            return jsonify({"message": "No se recibió el documento"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
