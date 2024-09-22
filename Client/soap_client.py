from zeep import Client

# Asegúrate de usar la URL correcta del WSDL
wsdl = 'http://127.0.0.1:8000/?wsdl'
client = Client(wsdl)

# Llamar al método celsius_to_fahrenheit
response = client.service.celsius_a_fahrenheit(25)

response2 = client.service.di_hola("Juan")

response3 = client.service.fahrenheit_a_celsius(77)

print(response)
print(response2)
print(response3)

