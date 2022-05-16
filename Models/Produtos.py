from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.APP)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_produto = db.Column(db.Integer())
    nome_produto = db.Column(db.String(20))
    valor = db.Column(db.Float)
    qtn_em_estoque = db.Column(db.Integer())
    valor_em_vendas = db.Column(db.Float())
    setor = db.Column(db.String())


def to_json(object):
    json_produto = {
        'Nome Produto': object.nome_produto,
        'Valor': object.valor,
        'Quantidade em estoque': object.qtn_em_estoque,
        'Valor de vendas': object.valor_em_vendas,
        "setor": object.setor,
        "codigo_produto": object.codigo_produto
    }

    return json_produto


def procurar_produto_setor(setor):
    produtos = Produto.query.filter_by(setor=setor).all()
    lista_de_produtos = []


    for objects_produtos in produtos:
        produtos_convertidos_em_json = to_json(objects_produtos)
        lista_de_produtos.append(produtos_convertidos_em_json)

    return lista_de_produtos


    

