from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import json
from config import usuario, clave, headers 

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

@app.route("/")
def listaredificios():
    r = requests.get("http://localhost:8000/api/edificios/",
                     auth=(usuario, clave))
    datos = json.loads(r.content)
    edificios = datos['results']
    numero_edificios = datos['count']
    return render_template("listaredificios.html", edificios=edificios,
                           numero_edificios=numero_edificios)

@app.route("/listardepartamentos")
def listardepartamentos():
    r = requests.get("http://localhost:8000/api/departamentos/", headers=headers)
    datos = json.loads(r.content)
    departamentos = datos['results']
    numero_departamentos = datos['count']
    return render_template("listardepartamentos.html", departamentos=departamentos,
                           numero_departamentos=numero_departamentos)

@app.route("/crear/edificio", methods=['GET', 'POST'])
def crear_edificio():
    """
    Crear un edificio
    """
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']

        data = {
            "nombre": nombre,
            "tipo": tipo,
            "direccion": direccion,
            "ciudad": ciudad
        }
        r = requests.post("http://localhost:8000/api/edificios/",
                          json=data,
                          headers=headers)
        
        nuevo_edificio = json.loads(r.content)
        flash(f"Edificio '{nuevo_edificio['nombre']}' creado exitosamente!", 'success')
        return redirect(url_for('listaredificios'))
            
    return render_template("crearedificios.html")

@app.route("/crear/departamento", methods=['GET', 'POST'])
def crear_departamento():
    r_edificios = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    edificios = json.loads(r_edificios.content)['results']
    if request.method == 'POST':
        nombre_propietario_form = request.form['nombre_propietario']
        costo_form = request.form['costo']
        cuartos_form = request.form['numero_cuartos']
        edificio_form = request.form['edificio_id']

        data = {
            "nombre_propietario": nombre_propietario_form,
            "costo": costo_form,
            "numero_cuartos": cuartos_form,
            "edificio": edificio_form
        }
        
        r = requests.post("http://localhost:8000/api/departamentos/",
                          json=data,
                          headers=headers)
        print(f"Status Code (Crear Número): {r.status_code}")
        nuevo_departamento = json.loads(r.content)
        flash(f"Departamento para '{nuevo_departamento['nombre_propietario']}' creado exitosamente!", 'success')
        return redirect(url_for('listardepartamentos'))    
    return render_template("creardepartamentos.html", edificios=edificios)


if __name__ == "__main__":
    app.run(debug=True)