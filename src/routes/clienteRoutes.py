from flask import Blueprint, request, render_template
from src.services.clienteServices import clienteServices
from src.models.clienteModels import cliente;

main = Blueprint('cliente_blueprint',__name__)
@main.route('/',methods=['GET','POST', 'PATCH','DELETE'])

def get_cliente():

    print(request)
    print(request.method)
  

    if request.method != 'GET':
        print("obtener datos del formulario")
        
        idCliente = ""   
        name = request.form["nombre"]
        postreFav = request.form["postre"]

        client = cliente(idCliente,name,postreFav)

    
    if request.method == 'GET':
        print("Método GET")
        get_client= clienteServices.get_client()
        # return render_template("index.html",datos = get_client)
        return render_template("index.html",datos = get_client)
    elif request.method == 'POST':
        print("Método POST")
        post_client = clienteServices.post_client(client)
        return("Cliente guardado")



main2 = Blueprint('cliente_blueprint2',__name__)
@main2.route('/',methods=['GET','POST', 'PATCH','DELETE'])

def procesar_method():
            
            print("estamos en procesar")
            print(request)
            print(request.method)

            texto1_value = request.form['texto1']

            return "el texto introducido es: "+texto1_value