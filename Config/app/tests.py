from django.test import TestCase
from pathlib import Path
import sys 
sys.path.append (str(Path(__file__).parent.parent))
from Config.wsgi import*
from app.models import*
# Create your tests here.

# #Listar 
# query = Tipo.objects.all()
# print (query)

#Insertar 
# t=Tipo (nombre='Prueba').save()

# #Editar 
           
# try:
#      t=Tipo.objects.get(id=1)
#      print(t.nombre)
#      t.nombre='Admin2'
#      t.save()
# except Exception as e:
#     print(e)
    
    
# #Eliminar
# t= Tipo.objects.get(id=1)
# t.delete() 
 

# #Listar Con Filter 

# obj = Tipo.objects.filter(nombre='ven').query #consulta like en base de Datos 

# print(obj)

# obj = Empleado.objects.filter()

# for i in Empleado.objects.filter():
#     print(i.nombre)
    
# data = ['Arroz','Confeti','Arepa','Lenteja','soya']
    
# for i in data:
#     cat = Categoria(nombre=i)
#     cat.save()
#     print ('Guardado Resgistro N {}'.format(cat.id))
    
data_productos = ['Arroz', 'Leche', 'Helado', 'Lenteja', 'Soya']

# Obtener la primera categoría existente (puedes ajustar esto según tus necesidades)
categoria_default = Categoria.objects.first()

# Crear productos y guardarlos en la base de datos
for nombre_producto in data_productos:
    producto = Producto(nombre=nombre_producto, categ=categoria_default)
    producto.save()
    print(f'Producto "{producto.nombre}" creado con éxito.')

print('Todos los productos han sido creados.')
    
