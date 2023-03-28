from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "database.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreComida = db.Column(db.String(250), nullable=False)
    descripcion = db.Column(db.String(250),nullable=False)
    precio = db.Column(db.Float, nullable=False)
    activo = db.Column(db.Boolean, default = True)

    def __init__(self, nombreComida, descripcion, precio):
        self.nombreComida = nombreComida
        self.descripcion = descripcion
        self.precio = precio

def admin_Rellenar():
    plato1 = Menu("Rape", "Rape a la parrilla", 15.00)
    plato2 = Menu("Rodaballo", "Rodaballo a la parrilla",30.00)
    plato3 = Menu("Merluza", "Merluza con apionabo y menier", 25.00)
    plato4 = Menu("Entrecot", "Entroct de Vacuno madurado", 28.00)
    plato5 = Menu("Solomillo", "Solomillo a la parilla berenjena ahumada y patata soufflé", 45.00)
    plato6 = Menu("Txuleta", "Txuleta de vacuno Premium, Selección Txogitxu, maduración mínima de 40 días", 78.00) 
    plato7 = Menu("Carrillera", "Carrillera de vaca estofada con clorifor e Idiazabal",24.00)
    
    db.session.add(plato1)
    db.session.add(plato2)
    db.session.add(plato3)
    db.session.add(plato4)
    db.session.add(plato5)
    db.session.add(plato6)
    db.session.add(plato7)
    
    db.session.commit()



@app.route("/")
def menus():
    lista_menus = Menu.query.all()
    return render_template("index.html", menus = lista_menus)

if __name__ == "__main__":
    # with app.app_context():
    #     # db.drop_all()
    #     # db.create_all()
    #     admin_Rellenar()
    app.run()
