#importar a instancia do banco 'db' criada no arquivo dabase.py
from database import db

#Definir a classe que ira realizar todos os mapeamentos da minha tabela
class Registro(db.Model):

    #Define o nome da minha tabela
    __tablename__ = 'registro'

id = db.Column(db.Integer, primary_key=true, autoincrement=true);
nome = db.Column(db.String(100),nullable=false)
info = db.Column(db.String(200),nullable=false)
valor = db.Column(db.Float,nullable=false)
status = db.Column(db.String(20),default='Pendente')
