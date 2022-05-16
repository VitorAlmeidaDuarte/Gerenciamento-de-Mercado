from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active
from Models.Produtos import Produto

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Metas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setor = db.Column(db.String())
    qtn_de_produtos_no_setor = db.Column(db.Integer())
    metas = db.Column(db.Float())



def mostrar_metas_do_mes(setor):
    valores_dos_produtos = Produto.query.filter_by(setor=setor).all()
    metas_do_setor = Metas.query.filter_by(setor=setor).first()

    valor_total_de_vendas = 0

    for valores in valores_dos_produtos:
        valor_total_de_vendas += valores.valor_em_vendas

    if valor_total_de_vendas > metas_do_setor.metas:
        return {'Meta atingida': valor_total_de_vendas}
    else:
        valor_para_bater_meta = valor_total_de_vendas - metas_do_setor.metas
        return {'Quanto falta para bater a meta': valor_para_bater_meta} 



