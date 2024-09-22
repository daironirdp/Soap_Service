
from spyne import Application, rpc, ServiceBase, Float, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Definir la clase que representa el servicio
class CelsiusAFahrenheit(ServiceBase):

    @rpc(Float, _returns=Float)
    def celsius_a_fahrenheit(ctx, celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    
class FahrenheitACelsius(ServiceBase):

    @rpc(Float, _returns=Float)
    def fahrenheit_a_celsius(ctx, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    

class Hola(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def di_hola(self, name):
        return f"Hola, {name}!"



# Crear una aplicación SOAP
soap_app = Application(
    [CelsiusAFahrenheit, Hola, FahrenheitACelsius],
    tns='http://localhost:8000/',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)
