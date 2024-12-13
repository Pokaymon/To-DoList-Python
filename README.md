# To-DoList-Python

Aplicativo para la gestion de Tareas.

# ¿Comó Funciona?

El aplicativo puede gestionar tareas, utiliza una estructura de datos de Lista Simplemente Enlazada (LSE), se utilizo customtkinter para la creación de la interfaz de usuario y sqlAlchemy para gestionar la conexion a la base de datos (MySQL).

Asi es el funcionamiento:
- main.py -> Se conecta a la base de datos usando el archivo 'connection.py' y llama a la interfaz grafica (Es importante la existencia correcta de las variables de Entorno).
- interfazGrafica.py -> Inicia la interfaz grafica usando customtkinter, utiliza los archivos task.py y lista.py, tambien utiliza el archivo 'rubi_thme.json' para manejar un estilo general para los componentes de la interfaz.
- task.py -> Se define la clase 'Task', con sus respectivos atributos y metodos.
- lista.py -> Define la clase 'Lista' y utiliza los metodos en el archivo metodos.py.
- metodos.py -> Se define la clase 'Metodos' que se encarga de gestionar todos los metodos para el correcto funcionamiento del sistema, utiliza los archivos 'task.py' y 'nodo.py'.
- nodo.py -> Define la clase 'Nodo' con los atributos data('task') y siguiente('Enlace').

# Para Ejecutarlo:

Requerimientos:
Es necesario instalar las librerias en el archivo requirements.txt

Variables de Entorno:
Es necesario crear las variables de entorno en el Cmd o Powershell de Visual

Crear Variables:
- $env:MYSQL_USER = "root"
- $env:MYSQL_PASSWORD = "123"
- $env:MYSQL_HOST = "localhost"
- $env:MYSQL_DB = "To_do_list_db"

Verificar Variables:
- echo $env:MYSQL_USER
- echo $env:MYSQL_PASSWORD
- echo $env:MYSQL_HOST
- echo $env:MYSQL_DB

Ejecución:
Posicionarse en la carpeta Main, Ruta: "C:\Users\Andre\Desktop\To-DoList\Main>" y usar el comando 'python -u "main.py"'

![image](https://github.com/user-attachments/assets/03076e97-14dc-4eb8-b3a0-f43a2afdbdcc)

![image](https://github.com/user-attachments/assets/dd5c2902-21f7-4fb9-bc33-4f36e95555b9)

![image](https://github.com/user-attachments/assets/3fb38f56-8edf-4ade-8e90-b70b1ead5bab)

![image](https://github.com/user-attachments/assets/d13c3d7e-9944-4426-b8af-d8512b6aa766)

![image](https://github.com/user-attachments/assets/1dd5c3c0-047f-4212-8697-971666aba81b)

![image](https://github.com/user-attachments/assets/e4de4eab-b4d4-4481-a1c9-6cb05346286e)

![image](https://github.com/user-attachments/assets/d3758028-c9e0-4a3c-803f-e9b6e43fbdca)

![image](https://github.com/user-attachments/assets/969148a8-c594-48db-96da-084933586627)

![image](https://github.com/user-attachments/assets/6db6f8d2-4359-448b-8f20-c02baca165ad)

![image](https://github.com/user-attachments/assets/d71031a3-5cfc-43a7-8cf0-12d3cf2ce3eb)

![image](https://github.com/user-attachments/assets/9bad600d-6f6d-4f50-b058-73ded12c5b9c)

![image](https://github.com/user-attachments/assets/02e24cb0-476b-442f-862b-28ec50b74446)

