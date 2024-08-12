from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired
import os
from models import db, Marca, Modelo, Fabricante, Caracteristica, Stock, Proveedor, Accesorio, Equipo

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecretkey')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/celulares'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

#FORMUARIO
class EquipoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    costo = FloatField('Costo', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    categoria = StringField('Categoría', validators=[DataRequired()])
    caracteristica = StringField('Características', validators=[DataRequired()])
    stock = StringField('Stock', validators=[DataRequired()])
    proveedor = StringField('Proveedor', validators=[DataRequired()])
    accesorio = StringField('Accesorio', validators=[DataRequired()])
    submit = SubmitField('Guardar')

# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listado_celulares')
def listado_celulares():
    try:
        equipos = Equipo.query.all()
        return render_template('listado_celulares.html', equipos=equipos)
    except Exception as e:
        return f"Ocurrió un error al cargar el listado de celulares: {e}"

@app.route('/add_equipo', methods=['GET', 'POST'])
def add_equipo():
    form = EquipoForm()
    if form.validate_on_submit():
        try:
            equipo = Equipo(
                nombre=form.nombre.data,
                costo=form.costo.data,
                modelo=form.modelo.data,
                marca=form.marca.data,
                categoria=form.categoria.data,
                caracteristica=form.caracteristica.data,
                stock=form.stock.data,
                proveedor=form.proveedor.data,
                accesorio=form.accesorio.data
            )
            db.session.add(equipo)
            db.session.commit()
            return redirect(url_for('listado_celulares'))
        except Exception as e:
            return f"Ocurrió un error al guardar el producto: {e}"
    return render_template('add_equipo.html', form=form)



@app.route('/edit_equipo/<int:id>', methods=['GET', 'POST'])
def edit_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    form = EquipoForm(obj=equipo)
    if form.validate_on_submit():
        equipo.nombre = form.nombre.data
        equipo.costo = form.costo.data
        equipo.modelo = form.modelo.data
        equipo.marca = form.marca.data
        equipo.categoria = form.categoria.data
        equipo.caracteristica = form.caracteristica.data
        equipo.stock = form.stock.data
        equipo.proveedor = form.proveedor.data
        equipo.accesorio = form.accesorio.data
        db.session.commit()
        return redirect(url_for('listado_celulares'))
    return render_template('add_equipo.html', form=form, title='Editar Celular')

@app.route('/delete_equipo/<int:id>')
def delete_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('listado_celulares'))



if __name__ == '__main__':
    app.run(debug=True)
