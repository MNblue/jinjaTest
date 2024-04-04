from src.database.db_mysql import get_connection;
from src.models.clienteModels import cliente;
from flask import Flask, render_template;

class clienteServices():



    @classmethod
    def get_client(cls):
        try:
            connection = get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM cliente')
                result = cursor.fetchall()
                print(result)
       
            connection.close()

            print(result)
            return result
           
           
        except Exception as ex:
            print(ex)
    

    @classmethod
    def post_client(cls, client:cliente):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                idCliente = client.idCliente
                nameClient = client.nombre
                postreFav = client.postreFavorito


                cursor.execute("INSERT INTO cliente (idCliente,nombre,postreFavorito )"+
                           "VALUES ('{0}','{1}','{2}')".format(idCliente,nameClient,postreFav))
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def update_client(cls, client:cliente):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                idCliente = client.idCliente
                nameClient = client.nombre
                postreFav = client.postreFavorito 


                cursor.execute("UPDATE cliente SET nombre='{1}', postreFavorito='{2}' WHERE idCliente = {0}".format(idCliente,nameClient,postreFav))                           
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)


    @classmethod
    def delete_Client(cls, client:cliente):
        try:
            connection = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                idCliente = client.idCliente
                
                cursor.execute("DELETE FROM cliente WHERE idCliente = {0}".format(idCliente))                           
                connection.commit()

            connection.close()
            return 0
        except Exception as ex:
            print(ex)

           