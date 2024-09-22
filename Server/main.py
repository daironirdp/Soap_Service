from soap_service import wsgi_app
from wsgiref.simple_server import make_server




if __name__ == '__main__':
    

    # Definir el servidor que escuchará en el puerto 8000
    server = make_server('127.0.0.1', 8000, wsgi_app)

    print("Servidor SOAP corriendo en http://127.0.0.1:8000")
    server.serve_forever()
