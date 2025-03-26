# *¿Para qué usamos Clases en Python?* #

Las clases en Python permiten a los desarrolladores crear componentes re-utilizables para su código, facilitando su mantenimiento y modificación. En este artículo, exploraremos los fundamentos de las clases en Python y cómo utilizarlas eficazmente en tus proyectos.

## Principios Básicos de la Programación Orientada a Objetos ##

La programación orientada a objetos (POO) es un paradigma de programación que utiliza objetos y sus interacciones para diseñar aplicaciones. Python es un lenguaje de programación orientado a objetos que admite los siguientes conceptos de POO:




1. Encapsulamiento: El encapsulamiento es el mecanismo de agrupar datos (atributos) y métodos juntos dentro de una clase. Oculta los detalles internos de un objeto y proporciona interfaces públicas para interactuar con él. El encapsulamiento ayuda a lograr la abstracción de datos y la modularidad del código.



2. Herencia: La herencia permite que una clase (subclase) herede propiedades y métodos de otra clase (superclase). La subclase puede ampliar o modificar el comportamiento heredado mientras hereda las características comunes de la superclase. La herencia promueve la reutilización del código y soporta la relación de "es-un".




3. Polimorfismo: El polimorfismo permite que objetos de diferentes clases sean tratados como objetos de una superclase común. Habilita el uso de una única interfaz para representar diferentes tipos de objetos. El polimorfismo se logra a través de la sobrescritura de métodos y la sobrecarga de métodos.




4. Abstracción: La abstracción se centra en representar las características esenciales de un objeto mientras oculta los detalles innecesarios. Permite a los programadores crear clases y métodos abstractos que definen el comportamiento común, dejando los detalles de implementación a las subclases.



## ¿Qué es Una Clase en Python?##

En Python, una clase es un plano para crear objetos (también conocidos como instancias). Define un conjunto de atributos (variables) y métodos (funciones) que los objetos creados a partir de la clase tendrán. En otras palabras, una clase sirve como una plantilla o estructura para crear objetos con características y comportamientos predefinidos.

###Cómo Crear Una Clase en Python###

La palabra clave class se utiliza para crear una clase. Aquí hay un ejemplo de una clase Person simple:

    class Person:
    def __init__(self, name, age):
    self.name = name
    self.age = age
    
    def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    person = Person("John", 30)
    person.greet()
    
    # Output:
    # 
    # Hello, my name is John and I am 30 years old.

En este ejemplo, la clase Person tiene dos atributos name y age, y un método greet que imprime un mensaje de saludo. El método \__init__ es un constructor que inicializa los atributos del objeto. Para crear un objeto de la clase Person, usamos el constructor de la clase y pasamos los parámetros requeridos.

La herencia es un mecanismo que permite a una subclase heredar las propiedades (métodos y atributos) de su superclase. El polimorfismo permite que objetos de diferentes clases se traten como si fueran del mismo tipo.

##Ventajas de Utilizar Clases##

La clase Python es un plano para crear objetos que tienen un conjunto de atributos y métodos. Es un concepto fundamental en la programación orientada a objetos. Aquí hay algunos beneficios de utilizar clases:


- Organización del código: Las clases te permiten agrupar datos y funcionalidades relacionados juntos en un solo bloque de código. Esto mejora la legibilidad del código, reduce la duplicación y hace que sea más fácil mantener y actualizar tu código.


- Herencia: Las clases se pueden usar para crear nuevas clases que heredan propiedades y métodos de las existentes. Esto te permite reutilizar código y evitar escribir código redundante.      

 

    	class Employee:    
    		"""A class representing an employee."""
    
    		def __init__(self, name, salary):
    			self.name = name
    			self.salary = salary
    
    		def get_salary(self):  
				return self.salary
    
    		def set_salary(self, new_salary):
    			self.salary = new_salary
    
    	class Manager(Employee):
    		"""A class representing a manager, inheriting from Employee."""
    
    		def __init__(self, name, salary, bonus):
    			super().__init__(name, salary)
    			self.bonus = bonus
    
    		def get_salary(self):
    			return self.salary + self.bonus
    

## Definiendo Clases en Python ##


Crear una clase en Python se realiza utilizando la palabra clave class. Las clases en Python permiten la creación de objetos que tienen atributos y métodos.

El siguiente código define una clase simple llamada Car y crea una instancia de esa clase llamada my\_car:

### Ejemplo de Una Definición de Clase ###

    class Car:
    	def __init__(self, make, model, year):
    		self.make = make
    		self.model = model
    		self.year = year
    
    my_car = Car("Toyota", "Corolla", 2022)

En este ejemplo, el método \__init__ se utiliza para la inicialización de clase en Python. El parámetro self se refiere a la instancia del objeto que se está creando. Los parámetros make, model y year son atributos del objeto que pueden ser accedidos y modificados usando la notación de punto. Finalmente, se crea una instancia de la clase Car con la variable my\_car, a la cual se le pasan los argumentos Toyota, Corolla y 2022.

El siguiente ejemplo define una clase más compleja llamada BankAccount:

### Ejemplo de Una Clase Compleja ###

    class BankAccount:  
    def __init__(self, account_number, balance):  
    self.account_number = account_number  
    self.balance = balance  
    self.transactions = []
    
    def deposit(self, amount):
    self.balance += amount
    self.transactions.append(("deposit", amount))
    
    def withdraw(self, amount):
    if amount > self.balance:
    raise ValueError("Not enough funds")
    self.balance -= amount
    self.transactions.append(("withdrawal", amount))
    
    my_account = BankAccount("123456", 500)
    my_account.deposit(200)
    my_account.withdraw(50)

En este ejemplo, se define la clase BankAccount con un \__init__ que establece los atributos account\_number y balance. También se inicializa una lista de transactions, que llevará un registro de todas las transacciones en la cuenta. Los métodos deposit y withdraw pueden ser llamados en un objeto BankAccount para modificar el saldo de la cuenta y añadir una transacción. Finalmente, la variable my_account se crea como un objeto BankAccount con un saldo inicial de 500, y la cuenta se modifica con un deposit y un retiro.

Estos ejemplos ilustran los fundamentos de definir clases en Python, incluyendo el uso de la palabra clave class, el método \__init__ para inicializar objetos y la creación de métodos de instancia para modificar atributos de objetos.

## La Diferencia Entre Clases e Instancias ##

Las clases en Python son el plano para crear objetos. Un objeto es una instancia de una clase, y puede tener atributos (variables) y métodos (funciones).

Para crear una clase en Python, usamos la palabra clave class seguida del nombre de la clase. Aquí hay un ejemplo:

    class Dog:
    	def __init__(self, name, breed):
    		self.name = name
    		self.breed = breed
    
    	def bark(self):
      		print("Woof!")
    
    my_dog = Dog("Fido", "Labrador")
    
    print(my_dog.name) 
    
    print(my_dog.breed) 
    
    my_dog.bark() 


En este ejemplo, creamos una clase Dog con dos atributos (name y breed) y un método (bark). El método \__init__ es un método especial que se llama cuando creamos una nueva instancia de la clase.


Para crear una nueva instancia de una clase en Python, simplemente podemos llamar a la clase como una función y pasar los argumentos necesarios.

En este ejemplo, creamos una nueva instancia de la clase Dog y la asignamos a la variable my\_dog. Pasamos dos argumentos (Fido y Labrador) que se utilizaron para establecer los atributos name y breed del objeto.

Luego, podemos acceder a los atributos y métodos del objeto utilizando la notación de punto.

En resumen, las clases en Python nos permiten crear objetos con atributos y métodos, y las instancias de una clase se crean llamando a la clase como una función.


## Invocación de Métodos de Clase ##

En Python, los métodos de clase se definen utilizando el decorador @classmethod. Los métodos de clase pueden ser llamados por la clase o una instancia de la clase.

Para invocar un método de clase en Python, puedes usar la siguiente sintaxis:

    class MyClass:
    	def __init__(self, name):
    		self.name = name
    
    @classmethod
    def greet(cls):
    	print(f"Hello from {cls.__name__}!")
    
    def say_hello(self):
    	print(f"Hello, {self.name}!")
    
    # Invoking class method without creating an instance
    MyClass.greet()
    
    # Creating an instance and invoking instance method
    obj = MyClass("Alice")
    obj.say_hello()

En este ejemplo, tenemos una clase llamada MyClass con dos métodos: greet() y say\_hello().

El método greet() es un método de clase decorado con @classmethod. Toma el parámetro cls, que se refiere a la clase en sí. Imprime un mensaje de saludo junto con el nombre de la clase.

El método say\_hello() es un método de instancia. Toma el parámetro self, que se refiere a la instancia de la clase. Imprime un mensaje de saludo personalizado usando el atributo name de la instancia.

Para invocar un método de clase, puedes llamarlo directamente en la clase en sí, sin crear una instancia.

## Implementación de Árboles de Clases en Python ##

En la programación de Python, una clase es un plano para crear objetos con atributos y métodos comunes. Un árbol de clases representa una jerarquía de clases, donde cada clase hereda atributos y métodos de su clase padre o superclase.


### Ejemplo de Árbol de Clases ###

    class Animal:
    	def __init__(self, name, sound):
    		self.name = name
    		self.sound = sound
    
    	def make_sound(self):
    		return self.sound
    
    class Dog(Animal):
    	def __init__(self, name, sound):
    		Animal.__init__(self, name, sound)
    
    dog = Dog("Rufus", "Woof")
    print(dog.make_sound())   # Output: Woof

En este ejemplo, definimos dos clases, Animal y Dog. La clase Dog hereda de la clase Animal usando la sintaxis class Dog(Animal):. La clase Dog tiene su propio constructor (\__init\__) pero también llama al constructor de su clase padre (Animal.\__init\__(self, name, sound)).


### Ejemplo de Árbol de Clases Más Complejo ###


    class A:
    	def method(self):
    		print("Method of class A")
    
    class B:
    	def method(self):
    		print("Method of class B")
    
    class C(A, B):
    	pass
    
    c = C()
    c.method()  # Output: Method of class A

En este ejemplo, definimos tres clases A, B y C. La clase C hereda de ambas A y B usando la sintaxis class C(A, B):. Al llamar a la función method en el objeto C, se resuelve al método A porque A está listado primero en la cadena de herencia.

## La Esencia de la POO: Reutilización de Código ##

La programación orientada a objetos (POO) es un paradigma de programación de software popular que enfatiza la creación de componentes de código reutilizables. La programación POO es poderosa en Python debido a su capacidad para implementar dicho código reutilizable en la forma de clases y módulos.

### Una Importación de Clase en Python ###

Python es un lenguaje orientado a objetos, lo que significa que las clases juegan un papel central en su diseño. Para acceder a los métodos y atributos de clase desde otro módulo, la clase debe ser importada usando la declaración import: from module\_name import Class\_Name.

## Herencia ##

En Python, la herencia permite que una clase herede propiedades y métodos de otra clase. Esto ayuda en la reutilización de código, facilitando la creación de nuevas clases sin tener que reescribir el código desde cero.

### Cómo Heredar de Dos Clases ###

Python también permite que una clase herede de dos clases y lo llama una herencia de dos niveles. En este caso, la nueva clase hereda de una clase que ya ha heredado de otra clase.

    class A:
    	def hello(self):
    		print("Hello from A")
    
    class B(A):
    	pass
    
    class C(B):
    	pass
    
    obj = C()
    obj.hello() # Output: Hello from A


En el código anterior, la clase C hereda de la clase B, la cual ya hereda de la clase A, y por lo tanto, puede acceder a métodos de ambas clases.

### Cómo Heredar de Múltiples Clases en Python ###

Python permite que una clase herede de múltiples clases al mismo tiempo. Esto se conoce como herencia múltiple y permite que la nueva clase tenga las características de ambas clases.

    class A:
    	def hello(self):
    		print("Hello from A")
    
    class B:
    	def hi(self):
    		print("Hi from B")
    
    class C:
    	def greet(self):
    		print("Greet from C")
    
    class D:
    	def good_morning(self):
    		print("Good_morning from D")
    
    class E(A,B,C, D):
    	pass
    
    obj = E()
    obj.hello() # Output: Hello from A
    obj.hi() # Output : Hi from B
    obj.good_morning() # Output : Good_morning from D

En el código anterior, la clase E hereda de las clases A, B, C, D y puede acceder a los métodos de todas estas clases.



# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase? #



## El constructor o metodo \__init__ ##

Un constructor es un método especial al que el programa llama a partir de la creación de un objeto. El constructor se utiliza en la clase para inicializar los miembros de datos en el objeto. Con nuestro ejemplo de clase, puede usar un constructor para asignar características de perro a cada objeto. El método especial es el constructor de Python.dog Fox Terrier\__init__.

Con una comprensión de la programación orientada a objetos y las clases, veamos ahora cómo funciona el método dentro de un programa de Python.\__init__

### La importancia de los objetos en Python ###
No siempre lo vemos cuando escribimos un programa, pero los objetos son fundamentales para la forma en que funciona Python. Cuando declaramos una variable simple en Python, se crea un objeto en segundo plano.

Si ejecutamos el siguiente fragmento de código:


    breed = "Doberman"

Python usa la clase str que contiene propiedades y métodos, exactamente igual a los que crea en su propio código, excepto que todo sucede en segundo plano.

## ¿Cómo funciona el método __init__? ##

El método es el equivalente en Python del constructor de C++ en un enfoque orientado a objetos. La función se llama cada vez que se crea un objeto a partir de una clase. El método permite a la clase inicializar los atributos del objeto y no sirve para ningún otro propósito. Solo se usa dentro de las clases. \__init__

### Crear una clase ###

Comencemos creando una clase:


    class Dog:   
     
    def __init__(self,dogBreed,dogEyeColor):
      
    	self.breed = dogBreed   
    	self.eyeColor = dogEyeColor...

Primero, declaramos la clase Dog usando la palabra clave . Usamos la palabra clave para definir una función o método, como el método. Como puede ver, el método inicializa dos atributos: y . class def\__init__\__init\__breedeyeColor

Ahora veremos cómo pasar estos parámetros al declarar un objeto. Aquí es donde necesitamos la palabra clave self para vincular los atributos del objeto a los argumentos recibidos.

### Crear un objeto ###

A continuación, crearemos un objeto, o instancia, de la clase :Dog

	
    ...Tomita = Dog("Fox Terrier","brown")...

Cuando creamos el objeto (que es el nombre del perro), primero definimos la clase a partir de la cual se crea (Dog). A continuación pasamos los argumentos "Fox Terrier" y "brown", que corresponden a los parámetros respectivos del método de la clase .tomita\__init__Dog

El método utiliza la palabra clave para asignar los valores pasados como argumentos a los atributos del objeto y .\__init__self self.breed self.eyeColor

## El constructor de \__init__ predeterminado ##

En Python, un constructor no necesariamente necesita que se le pasen parámetros. Puede haber parámetros predeterminados. Un constructor sin parámetros obligatorios se denomina constructor predeterminado. Reescribamos nuestra clase con un constructor predeterminado:

    class Dog:
     
    def __init__(self, dogBreed="German Shepherd",dogEyeColor="Brown"): 
      
    	self.breed = dogBreed   
    	self.eyeColor = dogEyeColor

Si un usuario no introduce ningún valor, el constructor asignará "Pastor alemán" y "Marrón" como atributos.

Ahora podemos crear una instancia de Dog sin especificar ningún parámetro:

	
    tomita = Dog()

Dado que no hay argumentos para pasar, usamos paréntesis vacíos después del nombre de la clase. Todavía podemos mostrar los atributos del objeto:

    print("This dog is a",tomita.breed,"and its eyes are",tomita.eyeColor)

Esto nos da el siguiente resultado:

	

    This dog is a German Shepherd and its eyes are Brown
    


# *¿Cuáles son los tres verbos de API?* #

Los tres verbos principales de una API (Interfaz de Programación de Aplicaciones) son:


- GET: Se utiliza para solicitar datos del servidor. Es el método más común y se emplea para obtener información sin modificarla.



- POST: Se utiliza para enviar datos al servidor, generalmente para crear un nuevo recurso. Es común en situaciones donde se desea agregar información.



- PUT: Se utiliza para actualizar un recurso existente en el servidor. Este método reemplaza el recurso completo con la nueva representación enviada.

Además de estos, hay otros verbos como DELETE (para eliminar recursos) y PATCH (para realizar actualizaciones parciales), pero GET, POST y PUT son los más fundamentales en la mayoría de las interacciones con APIs REST.



# *¿Es MongoDB una base de datos SQL o NoSQL?* #

MongoDB es una base de datos NoSQL. A diferencia de las bases de datos SQL, que utilizan un modelo relacional y se basan en tablas y filas, MongoDB almacena datos en documentos en formato BSON (Binary JSON). Esto permite una mayor flexibilidad en la estructura de los datos, ya que los documentos pueden tener diferentes esquemas y pueden ser fácilmente anidados. MongoDB es especialmente útil para aplicaciones que requieren escalabilidad y manejo de grandes volúmenes de datos no estructurados.

## Lenguaje de consulta estructurado (SQL) ##

### ¿Qué es SQL? ###


SQL, que significa Structured Query Language, es un lenguaje de programación específico de dominio (por ejemplo, un lenguaje dirigido a una tarea o problema específico) que se usa comúnmente para tareas como insertar, actualizar, consultar y eliminar datos dentro de una base de datos. SQL también se emplea para crear y modificar esquemas de bases de datos (por ejemplo, reglas de formato de datos, estructura de tablas/índices), así como para definir el acceso a la base de datos y los parámetros de administración.

### ¿Qué son los datos estructurados? ###

Los datos estructurados son datos que se organizan en un formato coherente y predefinido y, a menudo, constan de caracteres alfanuméricos. Algunos ejemplos son las transacciones financieras, los registros de inventario o las listas de clientes, que a menudo se almacenan en bases de datos SQL (por ejemplo, bases de datos relacionales).

### ¿Qué es una base de datos SQL? ###

Cuando se utiliza el término " SQL database ", se refiere a un tipo de base de datos donde SQL es el lenguaje de programación principal utilizado para crear y administrar esa base de datos. Las interfaces de programación de aplicaciones (API) de SQL contienen grupos de funciones que permiten a los desarrolladores ejecutar y gestionar operaciones de base de datos sin tener que crear comandos SQL individuales una y otra vez.

Independientemente de si una base de datos SQL se utiliza para almacenar transacciones para un minorista o información financiera para una corporación, las bases de datos SQL se encuentran bajo un tipo de base de datos denominada bases de datos relacionales.

### Bases de datos relacionales ###

Las bases de datos relacionales o los sistemas de administración de bases de datos relacionales (RDBMS) almacenan datos dentro de filas y columnas que se utilizan para formar tablas. Se puede crear una relación entre las dos tablas (o más) empleando una clave externa. Estas claves foráneas (por ejemplo, identificadores únicos) mantienen relaciones predefinidas que existen entre las tablas.

Ejemplo: una base de datos relacional de comercio electrónico que contiene información de clientes, productos y pedidos

![Imagen](https://webimages.mongodb.com/_com_assets/cms/lxx97f48zv6zuvv4v-image2.png?ixlib=js-3.7.1&auto=format%2Ccompress&w=1247)

Es importante tener en cuenta que las bases de datos relacionales se crean y gestionan mediante un esquema fijo. Un esquema fijo significa que todos los datos ingeridos en la base de datos deben estar alineados con precisión con los estándares de formato predefinidos, lo que limita los tipos de estructuras de datos que las bases de datos relacionales pueden almacenar. Por ejemplo, las relational database no pueden procesar datos no estructurados (por ejemplo, información que es incoherente en formato y no está alineada con un modelo de datos preestablecido), pero son excelentes para respaldar información transaccional o financiera que incluye datos estructurados o tipos de datos semiestructurados (por ejemplo, datos que tienen un formato coherente y se alinean con un modelo de datos preestablecido).

## Ejemplos de bases de datos SQL ##

Hay una variedad de ejemplos diferentes de bases de datos SQL, entre los que se incluyen:



- **Oracle**: Oracle Database es un sistema de gestión de bases de datos relacionales (RDBMS) desarrollado y comercializado por Oracle Corporation y es uno de los sistemas de bases de datos empresariales más empleados en el mundo.


- **MySQL**: MySQL es un sistema de gestión de bases de datos relacionales de código abierto de uso común que se emplea para crear y gestionar bases de datos. Desarrollado y distribuido por Oracle Corporation, MySQL es conocido por su facilidad de uso, amplio soporte comunitario y confiabilidad.
	

> Nota: Una alternativa de código abierto a MySQL se llama MariaDB, que fue diseñada como un reemplazo para MySQL después de la adquisición de MySQL por Oracle Corporation.


- **PostgreSQL**: PostgreSQL es un sistema de gestión de bases de datos relacional de objetos de código abierto conocido por sus capacidades avanzadas y ricas en funciones que amplían las capacidades de SQL. Desarrollado como parte del proyecto POSTGRES de la Universidad de California en Berkeley, PostgreSQL ofrece la compatibilidad con 
ACID, Características que almacenan y escalan de forma segura cargas de trabajo de datos complicadas (PostgreSQL.org 2024).


- **MSSQL**: MSSQL, que significa Microsoft SQL Server, es un sistema de gestión de bases de datos relacionales desarrollado por Microsoft. Esta plataforma de base de datos se usa comúnmente en entornos empresariales grandes para admitir aplicaciones de procesamiento de transacciones de alto volumen, inteligencia empresarial y análisis.


- **SQLite**: A diferencia de otros ejemplos en esta lista, SQLite es en realidad una biblioteca de software que proporciona un RDBMS. A diferencia de los otros RDBMS de esta lista, SQLite no tiene servidor y es autónomo sin configuración. Esto se debe a que está incrustado dentro de la aplicación mediante SQLite y, como resultado, no necesita un servidor separado.

Es importante tener en cuenta que otros tipos de bases de datos también pueden establecer relaciones entre datos. En el caso de bases de datos tabulares estandarizadas (por ejemplo, SQL o bases de datos relacionales), estas relaciones se expresan mediante claves foráneas o tablas de intersección. En el caso de los sistemas de gestión de bases de datos (DBMS) como MongoDB (por ejemplo, una base de datos NoSQL), estas relaciones se establecen mediante la incrustación o referencia de datos.


## No solo lenguaje de consulta estructurado (NoSQL) ##

### ¿Qué es NoSQL? ###

NoSQL, que significa Not only SQL, es un enfoque de sistema de gestión de bases de datos que se emplea para ingerir, almacenar y recuperar datos no estructurados y semiestructurados dentro de una base de datos. Esto significa que los datos que no se pueden analizar o contar a través de bases de datos relacionales tradicionales (por ejemplo, SQL) pueden permanecer en su formato nativo y ser ingeridos en una base de datos NoSQL. La razón por la que se llama NoSQL es para enfatizar que estas bases de datos pueden manejar modelos de datos no tabulares y no relacionales, así como admitir lenguajes de consulta similares a SQL.

### ¿Qué son los datos no estructurados? ###

Los datos no estructurados son datos que no tienen un modelo de datos predefinido ni una organización coherente. Además, los datos no estructurados, como las publicaciones en las redes sociales, pueden actualizar y cambiar rápidamente, mientras que los datos estructurados, como las transacciones bancarias, tienen una tasa de cambio mucho menor. Algunos ejemplos de datos no estructurados son las imágenes, los archivos de audio, los videos y los mapas.

### ¿Qué es una base de datos NoSQL? ###

Las bases de datos NoSQL son bases de datos que emplean un esquema flexible que admite datos no estructurados y datos semiestructurados, al tiempo que emplean un método de almacenamiento de datos no tabular.

El uso de un esquema flexible permite a las bases de datos NoSQL ingerir datos no estructurados en su formato nativo (por ejemplo, .txt, .JPG, MP3), lo cual no es posible con bases de datos SQL debido al requisito de que todos los datos se alineen a un formato predefinido. Además, cuando las bases de datos NoSQL almacenan datos, se emplean modelos de datos flexibles para que los archivos de datos no estructurados puedan tener diferentes estructuras de datos y aún así almacenar dentro de la misma collection.



### Tipos de bases de datos NoSQL ###

Existen diferentes tipos de bases de datos NoSQL, entre las que se incluyen:


- Bases de datos de documentos: Las bases de datos de documentos, a veces denominadas bases de datos orientadas a objetos, almacenan datos en documentos similares a objetos JSON (JavaScript Object Notation), aunque no son almacenes JSON. Utilizan los controladores devueltos de objetos nativos al lenguaje de programación utilizado por el desarrollador sin necesidad de un mapeador relacional de objetos (ORM). Cada documento en sí se trata como un registro y puede contener valores que incluyen números, matrices, objetos, cadenas o incluso caracteres booleanos. Además, se pueden incluir pares clave-valor, documentos anidados u otros datos estructurados. Un proveedor popular de estas bases de datos NoSQL es 
MongoDB


- Bases de datos de clave-valor: Las bases de datos de clave-valor recopilan, recuperan y almacenan datos como agrupaciones de pares clave-valor. Esto significa que cada registro de datos está representado por una clave única y un valor asociado. La clave se emplea para recuperar el valor correspondiente de la base de datos. Por ejemplo, en una base de datos clave-valor de diseño de interiores, una clave podría ser " color " y el valor podría ser " púrpura. " Los proveedores más populares de estos sistemas de bases de datos NoSQL son AWS y ScyllaDB.

- Almacenes de familias de columnas: Las bases de datos de familias de columnas organizan los datos en columnas en lugar de filas, lo que resulta útil cuando se trabaja con conjuntos de datos amplios que son escasos en profundidad. De hecho, las tiendas familiares de columnas a veces se denominan "tiendas de columna ancha". En los almacenes de familias de columnas, cada fila tiene un conjunto diferente de columnas, y las columnas se agrupan en "familias". Estos modelos de datos son útiles cuando se trabaja con conjuntos de datos a gran escala que se benefician del escalado horizontal para optimizar el rendimiento. Los proveedores populares de estas bases de datos NoSQL incluyen Apache, Cassandra y HBase.

- Bases de datos de grafos : Las bases de datos de grafos almacenan datos en nodos y bordes. Los nodos suelen almacenar información sobre personas, lugares y cosas, mientras que las aristas almacenan información sobre las relaciones entre los nodos. Las bases de datos de grafos son excelentes herramientas para consultar estructuras de grafos (por ejemplo, redes sociales, jerarquías). Los proveedores populares de estas bases de datos NoSQL incluyen Neo4j, AWS y Kibana.


## Diferencias clave entre bases de datos SQL y NoSQL ##


Si bien las bases de datos SQL y NoSQL ofrecen una funcionalidad valiosa, es importante comprender las diferencias clave entre ellas.

### Modelo de almacenamiento de base de datos ###

La diferencia entre los sistemas de bases de datos SQL y NoSQL en relación con el almacenamiento de datos es muy marcada. Específicamente, las bases de datos SQL almacenan datos en tablas que contienen filas y columnas, mientras que los sistemas NoSQL almacenan datos utilizando varios métodos según el tipo de datos no estructurados que se ingieren (por ejemplo, documentos JSON, emparejamiento de valor clave, agrupación familiar, nodos/bordes de gráficos).

### Tipo de datos ###

Mientras que las bases de datos NoSQL, a veces denominadas bases de datos no relacionales, son capaces de ingerir, almacenar y recuperar datos no estructurados, las bases de datos SQL (por ejemplo, bases de datos relacionales tradicionales) no lo son. Las bases de datos SQL solo pueden ingerir, almacenar y recuperar datos estructurados. Esto se debe a la diferencia entre los esquemas SQL y NoSQL utilizados.

### Esquemas ###

Las bases de datos SQL se basan en un esquema de datos estricto y predefinido con el que deben alinear los datos que se van a ingerir. Sin embargo, las bases de datos NoSQL emplean esquemas flexibles que les permiten ingerir datos en sus diversos formatos nativos.

### Escalabilidad ###

Es importante que los administradores de bases de datos planifiquen el crecimiento y la expansión de sus sistemas de bases de datos; este es otro punto claro de diferenciación entre las bases de datos SQL y NoSQL.

![Imagen](https://webimages.mongodb.com/_com_assets/cms/lxx9suk6j4ybvdqy0-image1.png?ixlib=js-3.7.1&auto=format%2Ccompress&w=1247)

### Bases de datos SQL ###

Las bases de datos SQL se escalan tradicionalmente verticalmente. Esto significa que los recursos (por ejemplo, CPU, almacenamiento o memoria) se agregan a un solo servidor. Y, aunque esto puede causar limitaciones en la cantidad de crecimiento posible, ya que solo hay un servidor con capacidad finita que se está escalando, hay varias razones para esta elección de escalado:


- Cumplimiento de atomicidad, consistencia, aislamiento y durabilidad (ACID): El cumplimiento de ACID se refiere a un conjunto de propiedades que garantizan la confiabilidad, consistencia e integridad de los datos de las transacciones de bases de datos. Esto es muy importante ya que muchas bases de datos SQL contienen información bancaria y financiera que debe cumplir con los estándares gubernamentales y de la industria. Sin embargo, es más difícil mantener el cumplimiento de ACID en un sistema distribuido (por ejemplo, muchos equipos conectados por una red) donde los recursos se incrementan a través del escalado horizontal en comparación con un equipo y un servidor que se escalan verticalmente.



> Nota: Hay algunas bases de datos NoSQL de sistemas distribuidos que pueden mantener el cumplimiento de ACID, como MongoDB Atlas.


- Gestión de transacciones: Las bases de datos SQL emplean mecanismos de gestión de transacciones para mantener la integridad de los datos y la coherencia de la base de datos. La administración de transacciones simultáneas a través de múltiples nodos en un entorno de base de datos distribuida probablemente crearía una complejidad adicional y un uso de recursos que podría afectar tanto la integridad de los datos como posiblemente el rendimiento general de la base de datos. Si se utilizara la escala horizontal, estos problemas serían una posibilidad.

- Rigidez del esquema: Las bases de datos SQL emplean esquemas rígidos y predefinidos con los que ingieren datos. Si bien esto es fácil de mantener en un entorno de una computadora/servidor, se agregaría complejidad si se empleara un sistema distribuido con escalado horizontal. En concreto, cada nodo podría tener una versión de esquema diferente, lo que aumentaría la sobrecarga de administración y podría causar problemas adicionales de coherencia de los datos.

### Bases de datos NoSQL ###

Los sistemas de bases de datos NoSQL a menudo se configuran en lo que se denomina un sistema distribuido. Esto significa que un serial de computadoras independientes (por ejemplo, nodos) están conectadas a través de una red y trabajan juntas para lograr objetivos comunes. Ser parte de un sistema distribuido también significa que se puede emplear el escalamiento horizontal frente al escalamiento vertical.

El escalado horizontal implica aumentar los recursos disponibles y la capacidad de un sistema distribuido mediante la adición de más nodos (por ejemplo, computadoras, servidores) a ese sistema. Al hacerlo, hay más nodos disponibles para soportar la carga de trabajo del sistema. Además, prácticamente no hay límite en cuanto al tamaño que puede crecer la base de datos desde una perspectiva de capacidad, ya que se pueden continuar agregando nodos adicionales.

## ¿Qué es una API? ##


Las API (Interfaz de Programación de Aplicaciones) son una parte fundamental en la creación de aplicaciones modernas, permitiendo la comunicación entre diferentes sistemas de forma efectiva y eficiente.

Para comprender mejor cómo aprovechar al máximo las API en el desarrollo web, es crucial entender algunos conceptos clave:



- **¿Qué es una API?**:   
Una API es un conjunto de reglas y protocolos que permite a las aplicaciones comunicarse entre sí. Define la forma en que diferentes componentes de software interactúan. 


![Imagen Api](https://patriciaemiguel.com/assets/2021-01-28-apis.png)



- **Tipos de API**: Existen varios tipos de API, siendo la API REST una de las más utilizadas en el desarrollo web por su simplicidad y flexibilidad.


- **API REST:** Esta arquitectura se basa en principios como el uso de métodos HTTP (GET, POST, PUT, DELETE) para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en recursos.

Algunas buenas prácticas para trabajar con API REST incluyen:



1. **Utilizar verbos HTTP de forma adecuada**: Asignar las operaciones correctas a los verbos correspondientes para mantener la coherencia y claridad en la comunicación.

2. **Gestionar correctamente los códigos de estado HTTP**: Proporcionar códigos de estado apropiados para indicar el resultado de una operación (200 para éxito, 404 para recurso no encontrado, etc.).


3. **Seguridad y autenticación:** Implementar medidas de seguridad como tokens de acceso o OAuth para proteger la API de accesos no autorizados.


Además, es crucial documentar adecuadamente una API para facilitar su uso por parte de otros desarrolladores. Una documentación clara y concisa ayuda a comprender cómo interactuar con la API, qué recursos están disponibles y cómo utilizarlos correctamente.

En resumen, las API en el desarrollo web son herramientas poderosas que permiten la integración de sistemas y la creación de experiencias digitales innovadoras. Al comprender los conceptos fundamentales y seguir buenas prácticas, se puede aprovechar al máximo el potencial de las API para construir aplicaciones robustas y escalables.

## Una guía completa sobre el uso correcto de una API REST ##

Las API REST (Representational State Transfer) son un componente fundamental en el desarrollo de aplicaciones web y móviles modernas. Permiten la comunicación entre diferentes sistemas de manera eficiente y escalable. Es crucial comprender cómo utilizarlas de forma correcta para maximizar su potencial y asegurar una integración exitosa.

Para utilizar una API REST de manera efectiva, es importante seguir algunas buenas prácticas:

1. **Utilizar métodos HTTP adecuados**: Los verbos HTTP como GET, POST, PUT y DELETE deben ser utilizados de acuerdo a su función específica. GET para recuperar datos, POST para crear recursos, PUT para actualizar recursos y DELETE para eliminarlos.

2. **Utilizar códigos de estado HTTP apropiados**: Los códigos de estado como 200 (OK), 201 (Created), 400 (Bad Request) y 404 (Not Found) proporcionan información sobre el resultado de la solicitud y son clave para la comunicación entre cliente y servidor.

3. **Implementar una estructura de URL consistente**: El diseño de las URL debe ser coherente y seguir las convenciones RESTful para facilitar su comprensión y mantenimiento.

4. **Utilizar JSON como formato de intercambio de datos**: JSON (JavaScript Object Notation) es ampliamente utilizado en las API REST debido a su simplicidad y ligereza. Facilita la lectura y escritura de datos por parte de los desarrolladores.

5. **Autenticación y autorización**: Implementar mecanismos de autenticación como tokens JWT (JSON Web Tokens) y autorización adecuada para proteger la API de accesos no autorizados.

# ¿Qué es Postman? #

Postman es una plataforma diseñada específicamente para probar y gestionar APIs, permitiendo a los desarrolladores simplificar cada paso del ciclo de vida de una API. Originalmente creado como una extensión del navegador, hoy en día Postman se encuentra disponible como aplicación independiente para Windows, Linux y macOS.

Con Postman, los desarrolladores pueden enviar peticiones HTTP (GET, POST, PUT, DELETE, entre otros), realizar pruebas automatizadas, y generar documentación detallada para las APIs, todo desde una interfaz gráfica amigable. Esta herramienta no solo ahorra tiempo, sino que también reduce errores en la programación de aplicaciones que requieren comunicación constante con servicios externos.

### Características de Postman ###

Una de las principales fortalezas de Postman es la cantidad de características que ofrece para facilitar el desarrollo con APIs. A continuación, detallamos algunas de las más destacadas:


- Colecciones de solicitudes: Postman permite agrupar diferentes solicitudes en colecciones, lo cual facilita la organización de las pruebas y la reutilización de peticiones en distintos entornos de desarrollo.


- Pruebas automatizadas: Utilizando JavaScript, Postman permite la creación de scripts personalizados para automatizar pruebas y validar respuestas. Esto es esencial para garantizar que los servicios web funcionen correctamente en diferentes etapas del ciclo de desarrollo.


- Gestión de entornos: Postman permite crear y gestionar distintos entornos (desarrollo, pruebas, producción) para probar cómo se comportan las APIs en diferentes configuraciones. Esto proporciona una gran flexibilidad a la hora de realizar pruebas sin necesidad de cambiar manualmente los parámetros.


- Generación de documentación: La documentación es fundamental para que otros desarrolladores comprendan cómo interactuar con una API. Postman genera automáticamente documentación a partir de las solicitudes y las respuestas, haciendo que sea más sencillo compartir los detalles de la API con el equipo.

### Ventajas de Usarlo ###

Postman se ha convertido en una herramienta indispensable gracias a sus múltiples ventajas. Estas facilitan la vida del desarrollador y mejoran la eficiencia en la gestión de APIs. Aquí te contamos las más relevantes:


1. Interfaz gráfica intuitiva: Postman ofrece una interfaz amigable y fácil de usar, que permite a los desarrolladores ejecutar pruebas sin necesidad de escribir código complejo. La posibilidad de interactuar de manera visual con las APIs reduce significativamente la curva de aprendizaje y favorece la productividad.



2. Compatibilidad multiplataforma: Postman es compatible con diversos sistemas operativos y puede ejecutarse en cualquier lugar, lo cual permite a los desarrolladores trabajar de manera colaborativa y sin restricciones. Además, su capacidad para soportar múltiples protocolos, como HTTP, HTTPS, y GraphQL, lo convierte en una herramienta versátil.



3. Mejora en la colaboración: Postman fomenta la colaboración en los equipos de desarrollo al permitir compartir colecciones de solicitudes y entornos. Esto facilita la integración de todos los miembros del equipo y asegura que todos trabajen sobre la misma base, mejorando la coordinación.



4. Versión gratuita: Postman ofrece un plan gratuito con características suficientes para equipos pequeños y proyectos individuales. Aunque también tiene una versión premium, la opción gratuita sigue siendo muy potente para los desarrolladores que recién comienzan a trabajar con APIs.



5. Automatización y productividad: Postman permite automatizar tareas repetitivas, como la ejecución de pruebas o la generación de documentación, lo cual incrementa la productividad del equipo. Los desarrolladores pueden enfocarse en resolver problemas más complejos y mejorar la calidad del software.


Postman no solo facilita el desarrollo y las pruebas de APIs, sino que también optimiza la documentación y fomenta la colaboración en equipos, posicionándose como una herramienta esencial en el desarrollo de aplicaciones modernas.

### ¿Para qué sirve Postman? ###

Al proporcionar un entorno gráfico e intuitivo, Postman permite a los usuarios interactuar de manera eficiente con APIs, realizar pruebas exhaustivas y colaborar con otros desarrolladores. A continuación, exploramos para qué sirve esta herramienta y cómo se puede aprovechar al máximo en el contexto del desarrollo de software.

### Desarrollo y Prueba de APIs ###

Uno de los principales usos de Postman es el desarrollo y prueba de APIs. La herramienta permite enviar solicitudes HTTP a servicios web y analizar sus respuestas, lo que es esencial para verificar el correcto funcionamiento de los endpoints. Los desarrolladores pueden utilizar Postman para enviar solicitudes GET, POST, PUT, DELETE, entre otros métodos, y comprobar cómo responde la API en diferentes circunstancias.

Esto no solo ayuda a identificar errores o comportamientos inesperados, sino que también permite validar las funciones que se han implementado. Por ejemplo, al construir un servicio web, Postman puede utilizarse para verificar si la API devuelve los datos correctos cuando se le proporcionan entradas específicas.

### Automatización de Pruebas ###

Además de la prueba manual, Postman permite la automatización de pruebas, una función sumamente valiosa en entornos de desarrollo ágil. Los desarrolladores pueden escribir scripts de prueba utilizando JavaScript para automatizar la validación de las respuestas recibidas. Esta capacidad es particularmente útil para realizar pruebas de regresión, asegurando que nuevas funcionalidades no afecten negativamente el comportamiento existente de la API.

Postman también facilita la ejecución de pruebas de integración, donde se comprueban múltiples solicitudes y sus interdependencias. Gracias a la posibilidad de automatizar estas secuencias, los equipos de desarrollo pueden mejorar la calidad y estabilidad del software antes de implementarlo en producción.

### Documentación de APIs ###

Postman no solo sirve para realizar pruebas; también es una herramienta eficaz para documentar APIs. La documentación generada por Postman incluye detalles de las solicitudes realizadas, ejemplos de respuestas y descripciones de los endpoints. Esta documentación interactiva es muy útil para los equipos de desarrollo y facilita la comprensión del funcionamiento de la API a otros desarrolladores o colaboradores del proyecto.

La documentación puede compartirse online, permitiendo que cualquier miembro del equipo acceda a ella y la consulte según sea necesario. Además, con Postman se pueden generar colecciones que sirven como una especie de guía sobre cómo utilizar la API, lo cual es esencial para garantizar un uso correcto y eficaz de los servicios ofrecidos.

### Colaboración en Equipos de Desarrollo ###

Otra función clave de Postman es la capacidad para facilitar la colaboración en equipos de desarrollo. Los equipos que trabajan en proyectos grandes y distribuidos pueden compartir colecciones de solicitudes, entornos de pruebas y los resultados obtenidos. Esta funcionalidad ayuda a que todos los miembros del equipo trabajen de manera coordinada y eficiente, evitando errores y asegurando que todos estén alineados respecto al comportamiento y evolución de la API.

Postman también ofrece opciones de sincronización en la nube, permitiendo a los desarrolladores acceder a sus colecciones desde cualquier lugar y dispositivo. De esta manera, la colaboración se hace más fluida, ya que todos tienen acceso a la misma información actualizada.

### Pruebas de Integración Continua ###

En un contexto de integración continua, Postman también juega un papel importante. Las pruebas automatizadas de APIs pueden integrarse con herramientas de CI/CD para verificar cada cambio realizado en el software, lo cual asegura que el nuevo código no afecte negativamente al funcionamiento del sistema. Gracias a las integraciones de Postman con herramientas populares de automatización, los equipos pueden implementar un flujo de trabajo que permita la prueba continua y el despliegue ágil del software.

Postman es, sin duda, una herramienta esencial para cualquier equipo de desarrollo que busque mejorar la calidad del software, facilitar la colaboración y reducir el tiempo de entrega al cliente. Al combinar sus capacidades de prueba, automatización, documentación y colaboración, Postman se convierte en un aliado clave en el desarrollo de servicios web robustos y fiables.


# ¿Qué es el polimorfismo? #

El polimorfismo es una técnica en la programación orientada a objetos que permite que los objetos de diferentes clases respondan a un mismo mensaje de diferentes maneras. Esto significa que el mismo método puede tener diferentes comportamientos según la clase del objeto que lo recibe.

El polimorfismo permite crear una jerarquía de clases relacionadas que se comportan de manera diferente pero que comparten una interfaz común. Esto hace que el código sea más fácil de mantener y actualizar, ya que se puede agregar una nueva clase sin afectar el código existente.

## Tipos de polimorfismo ##

En la POO, hay dos tipos principales de polimorfismo: el polimorfismo de sobrecarga y el polimorfismo de sobreescritura.



- Polimorfismo de sobrecarga: La sobrecarga de métodos es una técnica que permite que una clase tenga varios métodos con el mismo nombre, pero con diferentes parámetros. En tiempo de compilación, el compilador identifica el método adecuado a partir de los parámetros utilizados.


- Polimorfismo de sobreescritura: La sobreescritura de métodos es una técnica que permite que una subclase redefina un método de su superclase. Esto significa que el método de la subclase reemplaza al método de la superclase y se ejecuta en su lugar cuando se llama al método.


# ¿Qué es un método dunder? #


Los métodos dunder son funciones predefinidas en Python que tienen un propósito especial. Estos métodos están rodeados por dos guiones bajos antes y después del nombre del método, de ahí el nombre «dunder». Los métodos dunder también se conocen como «métodos mágicos». Algunos ejemplos comunes incluyen \__init\__, \__str\__, \__len\__, \__add\__, entre otros.

Estos métodos permiten a los desarrolladores definir cómo los objetos de una clase deben comportarse en ciertas situaciones, como cuando se imprimen, se comparan, se agregan, etc.

### Principales Métodos Dunder ###

1 \__init__(self, ...)

Este es probablemente el método dunder más conocido. Es utilizado para inicializar una nueva instancia de una clase. Es el constructor de la clase en Python.


        class Persona:  
    		def __init__(self, nombre, edad):  
    			self.nombre = nombre  
    			self.edad = edad
    
    	p = Persona("Juan", 30)

2 \__str__(self)

Este método define cómo se debe representar un objeto como una cadena de texto. Es el método al que se llama cuando se utiliza print() o str() en una instancia de la clase.

    class Persona:
    	def __init__(self, nombre, edad):
    		self.nombre = nombre
    		self.edad = edad
    
    	def __str__(self):
    		return f"{self.nombre}, {self.edad} años"
    
    p = Persona("Juan", 30)
    print(p)  # Output: Juan, 30 años

3 \__repr__(self)

Este método define una representación oficial de la instancia de la clase. Es útil para depuración y desarrollo. Se llama cuando se usa repr() en una instancia.

    class Persona:
    	def __init__(self, nombre, edad):
    		self.nombre = nombre
    		self.edad = edad
    
    	def __repr__(self):
    		return f"Persona({self.nombre}, {self.edad})"
    
    p = Persona("Juan", 30)
    print(repr(p))  # Output: Persona(Juan, 30)


4 \__len__(self)

Este método permite definir la longitud de un objeto. Es útil para clases que contienen una colección de elementos.

    class Grupo:
    	def __init__(self, miembros):
    		self.miembros = miembros
    
    	def __len__(self):
    		return len(self.miembros)
    
    g = Grupo(["Juan", "Ana", "Luis"])
    print(len(g))  # Output: 3


5 \__add__(self, other)

Este método permite definir el comportamiento de la suma + entre dos objetos de la clase.

    class Vector:
    	def __init__(self, x, y):
    		self.x = x
    		self.y = y
    
    	def __add__(self, otro):
    		return Vector(self.x + otro.x, self.y + otro.y)
    
    	def __str__(self):
    		return f"({self.x}, {self.y})"
    
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(v3)  # Output: (4, 6)


6 \__eq__(self, other)

Este método permite definir el comportamiento de la comparación de igualdad == entre dos objetos de la clase.

    class Persona:
    	def __init__(self, nombre, edad):
    		self.nombre = nombre
    		self.edad = edad
    
    	def __eq__(self, otro):
    		return self.nombre == otro.nombre and self.edad == otro.edad
    
    p1 = Persona("Juan", 30)
    p2 = Persona("Juan", 30)
    print(p1 == p2)  # Output: True


7 \__getitem__(self, key)

El método \__getitem__ permite que los objetos de una clase se comporten como colecciones (por ejemplo, listas o diccionarios). Esto permite acceder a los elementos utilizando la notación de corchetes.

    class MiLista:
    	def __init__(self, elementos):
    		self.elementos = elementos
    
    	def __getitem__(self, indice):
    		return self.elementos[indice]
    
    lista = MiLista([1, 2, 3, 4])
    print(lista[2])  # Output: 3


8 \__setitem__(self, key, value)

El método \__setitem__ se usa para asignar valores a los elementos de un objeto utilizando la notación de corchetes. Es útil para objetos que deben permitir la modificación de sus elementos.

    class MiLista:
    	def __init__(self, elementos):
    		self.elementos = elementos
    
    	def __getitem__(self, indice):
    		return self.elementos[indice]
    
    	def __setitem__(self, indice, valor):
    		self.elementos[indice] = valor
    
    lista = MiLista([1, 2, 3, 4])
    lista[2] = 10
    print(lista[2])  # Output: 10


9 \__delitem__(self, key)

El método delitem permite eliminar elementos de un objeto utilizando la notación de corchetes. Es apropiado para clases que necesitan permitir la eliminar de sus elementos.

    class MiLista:
    	def __init__(self, elementos):
    		self.elementos = elementos
    
    	def __getitem__(self, indice):
    		return self.elementos[indice]
    
    	def __setitem__(self, indice, valor):
    		self.elementos[indice] = valor
    
    	def __delitem__(self, indice):
    		del self.elementos[indice]
    
    lista = MiLista([1, 2, 3, 4])
    del lista[2]
    print(lista.elementos)  # Output: [1, 2, 4]


# ¿Qué es un decorador de python? #

Los decoradores decoran una función. ¿Obvio no? Vale, todavía no… Pero una vez hayas terminado el artículo entenderás el porqué de su nombre. Por ahora quedémonos con la idea de que un decorador es como un interruptor. Un interruptor que podemos encender o apagar para añadir funcionalidad extra a una función sin necesidad de añadir más código al cuerpo de dicha función. En la práctica un decorador se indica con el signo @ y se pone encima de la función que decora. Es algo tal que así:

    @un_decorador
    def mi_funcion():
    	# realizar alguna tarea
    	return algo

El funcionamiento de los decoradores se basa en tres ideas que vamos a desarrollar a continuación y que son las siguientes:



- Dentro de una función se pueden crear más funciones


- Las funciones pueden retornar funciones


- Las funciones se pueden pasar como argumentos a otras funciones


Una vez entendidos estos tres conceptos ya tendremos todo lo necesario para crear nuestros propios decoradores.

## Conceptos en los que se basan los decoradores ##

### Funciones dentro de una función ###

En el siguiente ejemplo definimos la funcion_intera() dentro la funcion_externa() y hacemos una llamada a la funcion_interna() también dentro de la funcion_externa(). Notar la indentación del código.

    def funcion_externa():
    	print("Código de la funcion_externa()")

    	def funcion_interna():
    		print("Código de la funcion_interna()")

    funcion_interna()


Es decir, que podemos llamar a la funcion_interna() porque lo hacemos dentro de la funcion_externa() que es donde la hemos definido. Efectivamente no podemos llamar a la funcion_externa() desde otros lugares de nuestro código ya que el intérprete de Python nos dice que tal función no existe.


### Retornando funciones ###

En el punto anterior acabamos de concluir que la funcion_interna() de nuestro ejemplo sólo se puede llamar dentro de la funcion_externa(). Pero ¿qué pasaría si la funcion_externa() retornara la funcion_interna()? Para saberlo, vamos a modificar un poco el código de nuestra funcion_externa() para reflejar tal cambio.

    def funcion_externa():
    	print("Código de la funcion_externa()")

    	def funcion_interna():
    		print("Código de la funcion_interna()")

    	return funcion_interna


Notar que para el retorno en la última línea no usamos paréntesis ya que en este caso no queremos ejecutar la funcion_interna() sino retornarla. Ahora vayamos un paso más allá y asignemos esta función a una variable que denominamos mi_funcion.

    >>> mi_funcion = funcion_externa()
    Código de la funcion_externa()
    >>> mi_funcion()
    Código de la funcion_interna()

Lo que observamos es que ahora, al haber retornado y asignado la funcion_interna() a la variable mi_funcion, podemos ejecutar el código de la funcion_interna() en otras partes de nuestro programa llamando a mi_funcion().

### Funciones como argumentos ###

Una de las cosas que hemos hecho en el apartado anterior es asignar una función a una variable. Por otro lado sabemos que las funciones admiten variables como argumentos. Esto significa que a una función se le puede pasar otra función como argumento. Veámoslo con el siguiente ejemplo.

    def una_funcion():
    	return "Código de una_funcion()"

    def otra_funcion(alguna_funcion):
    	print("Código de otra_funcion()")
    	print(alguna_funcion())

Como vemos ambas funciones son muy simples. Por un lado tenemos una_funcion() que retorna un string. Por otro, la función otra_funcion() que imprime un string, y a continuación el resultado retornado por la función que se le ha pasado como argumento. Llegados a este punto seguro que ya te imaginas el siguiente paso: ver que sucede cuando le pasamos a otra_funcion() una_funcion() como argumento.

    >>> otra_funcion(una_funcion)
    Código de otra_funcion()
    Código de una_funcion()

Y lo que vemos es que en otra_funcion() podemos ejecutar sin problema el código de una_funcion().

### Estructura de un decorador ###

Un decorador se compone de las tres ideas que acabamos de ver. Es decir, acepta una función como argumento y define una función interior la cual retorna. Además, dentro de la función interior ejecuta la función que se le ha pasado como argumento. Esto, que puede sonar algo confuso, traducido a código Python queda tal que así:

    def mi_decorador(funcion_original):
    	def funcion_envolvente():
    		print("Código antes de la funcion_original()")
    		funcion_original()
    		print("Código después de la funcion_original()")
    	return funcion_envolvente

Ahora definamos una función que vamos a pasarle a mi_decorador():

    def funcion_necesita_decorador():
    	print("¡Quiero que me decoren!")

Si pasamos la función anterior al decorador definido arriba, guardamos la función retornada por el decorador en una variable y ejecutamos dicha función obtenemos el siguiente resultado:

    >>> funcion_decorada = mi_decorador(funcion_necesita_decorador)
    >>> funcion_decorada()
    Código antes de la funcion_original()
    ¡Quiero que me decoren!
    Código después de la funcion_original()

Tal y como veíamos en la definición del inicio de ese artículo, en este último paso, hemos añadido funcionalidad extra a una función sin necesidad de añadir dicha funcionalidad explícitamente. En otras palabras, hemos envuelto o “decorado” una función con nueva funcionalidad dejando dicha función intacta, ya que el código que hemos añadido está en el decorador. Si queremos añadir o quitar dicha funcionalidad a la función, basta con añadirle o quitarle el decorador.

En Python la asignación que hemos realizado en la primera línea del código anterior se realiza con el signo @. Es decir, que esa asignación es equivalente a realizar lo siguiente:

    @mi_decorador
    def funcion_necesita_decorador():
    	print("¡Quiero que me decoren!")

De este modo el código queda muy limpio y fácil de entender. Además, podemos ejecutar la función por su nombre original obteniendo los mismos resultados que antes.

    >>> funcion_necesita_decorador()
    Código antes de la funcion_original()
    ¡Quiero que me decoren!
    Código después de la funcion_original()

### Decoradores en funciones con parámetros ###

Para simplificar la explicación del apartado anterior hemos utilizado una función sin parámetros. Sin embargo, es habitual que las funciones tomen parámetros de entrada para realizar alguna operación con ellos. En el siguiente código de ejemplo, al decorar una función con dos parámetros de entrada con el decorador que hemos definido anteriormente no sucede nada.

    @mi_decorador
    def mostrar_info(nombre, edad):
    	print(f"{nombre} tiene {edad} años")

Sin embargo, al ejecutar dicha función obtenemos un error. Esto sucede porque la función que hemos definido dentro de mi_decorador no toma argumentos, pero le estamos pasando los dos de la función decorada.

    >>> mostrar_info("Yoda", 900)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: funcion_envolvente() takes 0 positional arguments but 2 were given

Entonces, ¿sólo podemos decorar funciones sin argumentos o tenemos que crear tantas versiones del decorador como números distintos de parámetros de entrada tengan las funciones que vamos a decorar? Pues ni una cosa ni la otra ya que esto lo podemos resolver de un modo más simple. En Python existe el concepto *args, **kwargs que se utiliza para tomar en cuenta números de parámetros variables. Utilizando *args, **kwargs podemos reescribir nuestro decorador del siguiente modo:

    def mi_decorador(funcion_original):
    	def funcion_envolvente(*args, **kwargs):
    		print("Código antes de la funcion_original()")
    		funcion_original(*args, **kwargs)
    		print("Código después de la funcion_original()")
    	return funcion_envolvente

Ahora si volvemos a ejecutar la función mostrar_informacion() decorada con la definición anterior de mi_decorador, sí que obtenemos el resultado esperado.

    >>> mostrar_info("Yoda", 900)
    Código antes de la funcion_original()
    Yoda tiene 900 años
    Código después de la funcion_original()




## Fuentes ##

[http://https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html](http://https://www.udacity.com/blog/2021/11/__init__-in-python-an-overview.html)  
[https://www.byronvargas.com/web/como-se-usa-una-api-rest/?ufjnjten=775](https://www.byronvargas.com/web/como-se-usa-una-api-rest/?ufjnjten=775)  
[https://programacion.top/orientada-objetos/polimorfismo/](https://programacion.top/orientada-objetos/polimorfismo/)  
[https://programacion365.com/metodos-dunder](https://programacion365.com/metodos-dunder)  
[https://imaginaformacion.com/tutoriales/que-es-postman-y-para-que-sirve](https://imaginaformacion.com/tutoriales/que-es-postman-y-para-que-sirve)  
[https://www.mongodb.com/es/resources](https://www.mongodb.com/es/resources)  
[https://www.programaenpython.com/avanzado/decoradores-en-python/](https://www.programaenpython.com/avanzado/decoradores-en-python/)
