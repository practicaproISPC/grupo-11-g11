import classTipoDeEmpleado
class Empleado:
    def __init__(self, idEmpleado, idTipoEmpleado, nombre, apellido,
                 fechaNacimiento, dni, sexo, telefono, direccion, localidad,
                 provincia, grupoSanguineo, email, fechaIngreso, usuario,
                 contrasenia, observaciones):
        self.__idEmpleado = idEmpleado
        self.__idTipoEmpleado = TipoDeEmpleado.idTipoEmpleado
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
        self.__dni = dni
        self.__sexo = sexo
        self.__telefono = telefono
        self.__direccion = direccion
        self.__localidad = localidad
        self.__provincia = provincia
        self.__grupoSanguineo = grupoSanguineo
        self.__email = email
        self.__fechaIngreso = fechaIngreso
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.__observaciones = observaciones

        def __init__(self, idEmpleado, idTipoEmpleado, nombre, apellido,
                 fechaNacimiento, dni, sexo, telefono, direccion, localidad,
                 provincia, grupoSanguineo, email, fechaIngreso, usuario,
                 contrasenia):
        self.__idEmpleado = idEmpleado
        self.__idTipoEmpleado = TipoDeEmpleado.idTipoEmpleado
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
        self.__dni = dni
        self.__sexo = sexo
        self.__telefono = telefono
        self.__direccion = direccion
        self.__localidad = localidad
        self.__provincia = provincia
        self.__grupoSanguineo = grupoSanguineo
        self.__email = email
        self.__fechaIngreso = fechaIngreso
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def getIdEmpleado(self):
        return self.__idPersona

    def getIdTipoEmpleado(self):
        return self.TipoDeEmpleado.__idTipoEmpleado.name

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido
    def setApellido(self,apellido):
        self.__apellido = apellido

    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    def setFechaNacimiento(self,fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

    def getDni(self):
        return self.__dni
    def setDni(self,dni):
        self.__dni = dni

    def getSexo(self):
        return self.__sexo
    def setSexo(self,sexo):
        self.__sexo = sexo

    def getTelefono(self):
        return self.__telefono
    def setTelefono(self,telefono):
        self.__telefono = telefono

    def getDireccion(self):
        return self.__direccion
    def setDireccion(self,direccion):
        self.__direccion = direccion

    def getLocalidad(self):
        return self.__localidad
    def setLocalidad(self,localidad):
        self.__localidad = localidad

    def getProvincia(self):
        return self.__provincia
    def setProvincia(self,provincia):
        self.__provincia = provincia

    def getGrupoSanguineo(self):
        return self.__grupoSanguineo
    def setGrupoSanguineo(self,grupoSanguineo):
        self.__grupoSanguineo = grupoSanguineo

    def getEmail(self):
        return self.__email
    def setEmail(self,email):
        self.__email = email

    def getFechaIngreso(self):
        return self.__fechaIngreso
    def setFechaIngreso(self,fechaIngreso):
        self.__fechaIngreso = fechaIngreso

    def getUsuario(self):
        return self.__usuario
    def setUsuario(self,usuario):
        self.__usuario = usuario

    def getContrasenia(self):
        return self.__contrasenia
    def setContrasenia(self,contrasenia):
        self.__contrasenia = contrasenia

    def getObservaciones(self):
        return self.__observaciones
    def setObservaciones(self,observaciones):
        self.__observaciones = observaciones
