from bd import conexion
from flask import Flask
from flask import render_template, request
app = Flask(__name__)

tabla = ("""
    SET ANSI_NULLS ON

	SET QUOTED_IDENTIFIER ON

	CREATE TABLE [dbo].[Empleado](
	[Id_Persona] [int] IDENTITY(1,1) NOT NULL,
	[Id_Tipo_Empleado] [int] NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
	[Apellido] [varchar](50) NOT NULL,
	[Fecha_Nacimiento] [date] NOT NULL,
	[Dni] [varchar](10) NOT NULL,
	[Sexo] [varchar](10) NOT NULL,
	[Telefono] [varchar](50) NOT NULL,
	[Direccion] [varchar](50) NOT NULL,
	[Localidad] [varchar](50) NOT NULL,
	[Provincia] [varchar](50) NOT NULL,
	[Grupo_Sanguineo] [varchar](5) NOT NULL,
	[Email] [varchar](50) NOT NULL,
	[Fecha_Ingreso] [date] NOT NULL,
	[Usuario] [varchar](50) NOT NULL,
	[Contrasenia] [varchar](50) NOT NULL,
	[Observaciones] [varchar](50) NULL,
 	CONSTRAINT [PK_Operarios] PRIMARY KEY CLUSTERED
	(
	[Id_Persona] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

	/****** Object:  Table [dbo].[Tareas]    Script Date: 06/09/2021 17:53:37 ******/
	SET ANSI_NULLS ON

	SET QUOTED_IDENTIFIER ON

	CREATE TABLE [dbo].[Tareas](
	[Id_Tarea] [int] IDENTITY(1,1) NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
 	CONSTRAINT [PK_Tareas] PRIMARY KEY CLUSTERED
	(
	[Id_Tarea] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

	/****** Object:  Table [dbo].[Tipo_Empleado]    Script Date: 06/09/2021 17:53:37 ******/
	SET ANSI_NULLS ON

	SET QUOTED_IDENTIFIER ON

	CREATE TABLE [dbo].[Tipo_Empleado](
	[Id_Tipo_Empleado] [int] IDENTITY(1,1) NOT NULL,
	[Nombre] [varchar](50) NOT NULL,
 	CONSTRAINT [PK_Tipo_Empleado] PRIMARY KEY CLUSTERED
	(
	[Id_Tipo_Empleado] ASC
	)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]

	SET IDENTITY_INSERT [dbo].[Tipo_Empleado] ON

	INSERT [dbo].[Tipo_Empleado] ([Id_Tipo_Empleado], [Nombre]) VALUES (1, N'Administrador')

	INSERT [dbo].[Tipo_Empleado] ([Id_Tipo_Empleado], [Nombre]) VALUES (2, N'Operario')

	SET IDENTITY_INSERT [dbo].[Tipo_Empleado] OFF

	ALTER TABLE [dbo].[Empleado]  WITH CHECK ADD  CONSTRAINT [FK_Personal_Tipo_Empleado] FOREIGN KEY([Id_Tipo_Empleado])
	REFERENCES [dbo].[Tipo_Empleado] ([Id_Tipo_Empleado])

	ALTER TABLE [dbo].[Empleado] CHECK CONSTRAINT [FK_Personal_Tipo_Empleado]""")

def crearTabla(tabla):	
    cursor = conexion.cursor()
    cursor.execute(tabla)
    conexion.commit()
    conexion.close()
    
@app.route('/')
def index():	
    cursor = conexion.cursor()
    cursor.execute(tabla)
    conexion.commit()
    conexion.close()
    return render_template('index.html')

@app.route('/RegistroOperario')
def registrarOperario():
	return render_template('RegistroOperario')

@app.route('/almacenar', methods=['POST'])
def almacenar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    dni = request.form['dni']
    sexo = request.form['sexo']
    telefono = request.form['telefono']
    direccion = request.form['direccion']
    localidad = request.form['localidad']
    provincia = request.form['provincia']
    grupoSanguineo = request.form['grupoSanguineo']
    correo = request.form['correo']
    fechaIngreso = request.form['fechaIngreso']
    usuario = request.form['usuario']
    contrasenia = request.form['contrasenia']
    observaciones = request.form['observaciones']
    
    sql = ("""[dbo].[Empleado]([Id_Tipo_Empleado],[Nombre],[Apellido],[Fecha_Nacimiento],[Dni],[Sexo],
           [Telefono],[Direccion],[Localidad],[Provincia],[Grupo_Sanguineo],[Email],[Fecha_Ingreso],[Usuario],
           [Contrasenia],[Observaciones]) VALUES(<2,int,>,<%s,varchar(50),>,<%svarchar(50),>,<%s,date,>,
           <%s,varchar(10),>,<%s,varchar(10),>,<%s,varchar(50),>,<%s,varchar(50),>,<%s,varchar(50),>,
           <%s,varchar(50),>,<%s,varchar(5),>,<%s,varchar(50),>,<%s,date,>,<%s,varchar(50),>,<%s,varchar(50),>,
           <%s,varchar(50),>);""")
    
    datos = (nombre,apellido,edad,dni,sexo,telefono,direccion,localidad,provincia,
             grupoSanguineo,correo,fechaIngreso,usuario,contrasenia,observaciones)
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    conexion.close()
    return render_template('index.html')

def consultar():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM dbo.Empleado;")
    return cursor.fetchall()

crearTabla(tabla)


    
 
