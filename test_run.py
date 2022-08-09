import unittest
from src.main.dao.CiudadDAO import CiudadDao

ciudad = CiudadDao()

class TestRun(unittest.TestCase):
    
    def test_leer_ciudades(self):
        lista_ciudades = ciudad.listarTodos()
        #lista_ciudades=[]
        self.assertIsNotNone(lista_ciudades, 'La colección es nula')
        self.assertGreater(len(lista_ciudades), 0, 'la coleccion está vacía')
        
    def test_insertar_ciudad(self):
        is_inserted = ciudad.agregar('Fernando de la Mora')
        self.assertTrue(is_inserted, 'No se ha insertado')
        
    def test_modificar_ciudad(self):
        is_modified = ciudad.modificar(4, 'San Lorenzo')
        self.assertTrue(is_modified, 'No se ha modificado')
        
    def test_eliminar_ciudad(self):
        is_deleted = ciudad.eliminar(4)
        self.assertTrue(is_deleted, 'No se ha eliminado')
        
if __name__ == '__main__':
    unittest.main()