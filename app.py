import os

import pymysql
from flask import Flask, jsonify, request

app = Flask(__name__)


class Config:
    DB_HOST = os.getenv("DB_HOST", "servidor-bd-ejemplo")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASS = os.getenv("DB_PASS", "")
    DB_NAME = os.getenv("DB_NAME", "legacydb")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    PORT = int(os.getenv("PORT", 5050))


@app.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            database=Config.DB_NAME,
        )
        conn.close()
        return "<h1>API Legacy TechNova - Funcionando</h1>"
    except Exception as e:
        app.logger.error("Error de conexión a BD: %s", e)
        return "<h1>Sistema Caído</h1><p>No se pudo conectar a la base de datos.</p>", 500


@app.route("/buscar")
def buscar_usuario():
    usuario_id = request.args.get("id", "1")
    query_segura = "SELECT * FROM usuarios WHERE id = %s"
    return jsonify({"query": query_segura, "parametros": [usuario_id]})


@app.route("/health")
def health_check():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.PORT, debug=Config.DEBUG)  # nosec B104 - bind en contenedor
