from src.main.dao.CiudadDAO import CiudadDao

ciudad = CiudadDao()
# Operaciones CRUD
## Leer todos
lista_ciudades = ciudad.listarTodos()
print(lista_ciudades)

## Leer por id
ciudadFound = ciudad.getById(1)
print(ciudadFound)

## Agregar
#ciudad.agregar('Fernando de la Mora')

## Modificar
#ciudad.modificar(3, 'San Lorenzo')

## Eliminar
#ciudad.eliminar(3)