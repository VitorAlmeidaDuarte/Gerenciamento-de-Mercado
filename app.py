
from config import app_config, app_active
from flask import Flask, request
from Models.Produtos import procurar_produto_setor
from Models.Metas_do_mes import mostrar_metas_do_mes
from flask_sqlalchemy import SQLAlchemy

config = app_config[app_active]



def create_app(condig_name):
    app = Flask(__name__, template_folder="templates")

    app.secret_key = config.SECRET
    app.config.from_object(app_config[condig_name])
    app.config.from_pyfile("config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db = SQLAlchemy(config.APP)
    db.init_app(app)

    

    @app.route('/produtos/mostrar-dados', methods=['GET'])
    def dados_de_produtos():
        setor_body = request.get_json()

        produtos_ou_error = procurar_produto_setor(setor_body['setor'])
        
        if produtos_ou_error == []:
            return {'Error': 'setor não encontrado'}

        else:
            return {'produtos': produtos_ou_error}


    @app.route('/metas-do-mês', methods=['GET'])
    def metas_do_mes():
        setor_body = request.get_json()

        resultado_das_metas_mes = mostrar_metas_do_mes(setor_body['setor'])

        if resultado_das_metas_mes == []:
            return {'Error': 'setor não econtrado' }

        else:
            return resultado_das_metas_mes
    return app
