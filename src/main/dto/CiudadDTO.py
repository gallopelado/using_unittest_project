class CiudadDTO:
    def __init__(self, ciu_id, ciu_descripcion):
        self.__ciu_id = ciu_id
        self.__ciu_descripcion = ciu_descripcion
        
    @property
    def ciu_id(self):
        return self.__ciu_id
    
    @ciu_id.setter
    def ciu_id(self, ciu_id):
        self.__ciu_id = ciu_id
        
    @property
    def ciu_descripcion(self):
        return self.__ciu_descripcion
    
    @ciu_descripcion.setter
    def ciu_descripcion(self, ciu_descripcion):
        self.__ciu_descripcion = ciu_descripcion
        
    def __str__(self) -> str:
        return str(dict(ciu_id=self.__ciu_id, ciu_descripcion=self.__ciu_descripcion))