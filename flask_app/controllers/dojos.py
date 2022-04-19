from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def landing():
    return redirect('/dojo')

@app.route('/dojo')
def dojo_landing():
    dojos = Dojo.get_all()
    return render_template('dojo.html', dojos=dojos)
    
@app.route('/new_dojo', methods=['post'])
def new_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect('/dojo')

@app.route('/dojo_show/<int:id>')
def dojo_show(id):
    dojo=Dojo.get_dojo_with_ninjas(id)
    return render_template('dojo_show.html', dojo=dojo.ninjas)

@app.route('/create_ninja')
def create_ninja():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos=dojos)

@app.route('/new_ninja', methods=['post'])
def new_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/dojo_show/' + data['dojo_id'])
