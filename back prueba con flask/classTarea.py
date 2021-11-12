class Tarea:
    def __init__(self, idTarea, nombre):
        self.__idTarea = idTarea
        self.__nombre = nombre

    def getIdTarea(self):
        return self.__idTarea

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre

