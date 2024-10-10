from pathlib import Path
import sys 
sys.path.append (str(Path(__file__).parent.parent))
from Config.wsgi import *
from app.models import *



#Creación de test con base de datos
#---------------------------------------------------------------- CLASE EMPLEADO --------------------------------------------
# 1. Crear un nuevo cliente
# def crear_cliente():
#     cliente = Cliente(
#         nombre="Juan",
#         apellido="Perez",
#         cedula="1234567890",
#         fecha_n=datetime(1990, 5, 15).date(),
#         sexo="male",
#         correo="juan.perez@example.com",
#         direccion="Calle Principal 123"
#     )
#     cliente.save()
#     print("Cliente creado:", cliente)


#Crear una Ubicacion
# u = Ubicacion(id=1,Departamento="Boyaca",Ciudad="Sogamoso").save()
# query = Ubicacion.objects.all()
# print(query)


# 2. Listar todos los clientes
# def listar_clientes():
#     clientes = Cliente.objects.all()
#     for cliente in clientes:
#         print(cliente)


# 3. Actualizar un cliente existente
# def actualizar_cliente(id_cliente, nuevo_nombre):
#     cliente = Cliente.objects.get(id=id_cliente)
#     cliente.nombre = nuevo_nombre
#     cliente.save()
#     print("Cliente actualizado:", cliente)


# 4. Eliminar un cliente
# def eliminar_cliente(id_cliente):
#     cliente = Cliente.objects.get(id=id_cliente)
#     cliente.delete()
#     print("Cliente eliminado:", cliente)


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
    
# data_productos = ['Arroz', 'Leche', 'Helado', 'Lenteja', 'Soya']

# # Obtener la primera categoría existente (puedes ajustar esto según tus necesidades)
# categoria_default = Categoria.objects.first()

# Crear productos y guardarlos en la base de datos
# for nombre_producto in data_productos:
#     producto = Producto(nombre=nombre_producto, categ=categoria_default)
#     producto.save()
#     print(f'Producto "{producto.nombre}" creado con éxito.')

# print('Todos los productos han sido creados.')


# Eliminar todos los productos y confirmar la eliminación
# productos = Producto.objects.all()
# for producto in productos:
#     print(f'Eliminando producto "{producto.nombre}"...')
#     producto.delete()
#     print(f'Producto "{producto.nombre}" eliminado con éxito.')

# print('Todos los productos han sido eliminados.')

# departamento = Departamentos.objects.get(id=9)
# print(departamento.municipios.all())