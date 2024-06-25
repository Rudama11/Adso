from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from Prueba2.wsgi import *
from apl.models import *

# #Listar
# query = Categoria.objects.all()
# print(query)

#Insertar
# t = Categoria(id=1,nombre='Cereal').save()
# t = Categoria(id=2,nombre='Granos').save()
# t = Categoria(id=3,nombre='Lacteos').save()
# query = Categoria.objects.all()
# print(query)

# categoria = Categoria.objects.get(id=1)
# t = Producto(id=3,nombre='Cereal',categ=categoria,precio=2500).save()
# query = Producto.objects.all()
# print(query)

#Editar
# try:
#     t = Tipo.objects.get(id=1)
#     print(t.nombre)
#     t.nombre = 'Admin2'
#     t.save()
# except Exception as e:
#     print(e)

#Eliminar
#t = Categoria.objects.get(id=7).delete()

# #Listar con filtro
# obj = Tipo.objects.filter(nombre_contains='ven').query
# print(obj)
# obj = Empleado.objects.filter()

# data = ['arroz','confeti','arepa','lenteja','soya']

# for i in data:
#     cat = Categoria(nombre=i)
#     cat.save()
#     print('Guardado de registro N{}'.format(cat.id))