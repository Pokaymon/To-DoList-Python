# To-DoList-Python

Aplicación para la gestión de tareas utilizando Python, con una interfaz gráfica y conexión a una base de datos MySQL.

---

## 🚀 **¿Cómo Funciona?**

Este aplicativo permite gestionar tareas a través de una **Lista Simplemente Enlazada (LSE)** como estructura de datos, y utiliza las siguientes tecnologías:

- **customtkinter**: Para la creación de la interfaz gráfica.
- **SQLAlchemy**: Para gestionar la conexión y operaciones con la base de datos MySQL.
- **PyMySQL**: Para gestionar operaciones con la base de datos MySQL.

### 📂 **Estructura del Proyecto**

- **`main.py`**:  
  - Se conecta a la base de datos usando `connection.py`.  
  - Llama a la interfaz gráfica definida en `interfazGrafica.py`.  
  - **Nota**: Es crucial configurar correctamente las variables de entorno para que funcione.
 
- **`connection.py`**:
  - Contiene los metodos para crear la base de datos en caso de que no exista, conectarse a la base de datos usando las variables de entorno y crear la tabla `tasks` con sus respectivas columnas.
  - Gestiona la conexión utilizando `SQLAlchemy`.

- **`interfazGrafica.py`**:  
  - Inicializa la interfaz gráfica utilizando `customtkinter`.  
  - Depende de los archivos `task.py`, `lista.py` y el archivo de estilo `rubi_theme.json` para personalizar los componentes de la interfaz.

- **`task.py`**:  
  - Contiene la definición de la clase `Task`, que incluye sus atributos y métodos.

- **`lista.py`**:  
  - Define la clase `Lista`, que implementa una Lista Simplemente Enlazada (LSE).  
  - Utiliza los métodos definidos en `metodos.py`.

- **`metodos.py`**:  
  - Define la clase `Metodos`, que centraliza todas las operaciones necesarias para el correcto funcionamiento del sistema.  
  - Este archivo utiliza las clases definidas en `task.py` y `nodo.py`.

- **`nodo.py`**:  
  - Define la clase `Nodo`, con los atributos:  
    - `data`: Almacena objetos de tipo `Task`.  
    - `siguiente`: Es un puntero al siguiente nodo en la lista.

---

## ⚙️ **Requisitos**

### Dependencias:
Es necesario instalar las librerías listadas en el archivo `requirements.txt`.  
Usa el siguiente comando:  
```bash
pip install -r requirements.txt
```

### Variables de Entorno:
Para establecer la conexión con la base de datos MySQL, debes configurar las siguientes variables de entorno. Esto se realiza desde PowerShell o la terminal de Visual Studio Code.

**Crear Variables**
```bash
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "123"
$env:MYSQL_HOST = "localhost"
$env:MYSQL_DB = "To_do_list_db"
```

**Verificar Variables**

Puedes confirmar que las variables se configuraron correctamente con los siguientes comandos:
```bash
echo $env:MYSQL_USER
echo $env:MYSQL_PASSWORD
echo $env:MYSQL_HOST
echo $env:MYSQL_DB
```

---

## ▶️ **¿Comó Ejecutarlo?**

Asegúrate de estar en el directorio principal del proyecto, dentro de la carpeta Main.
Por ejemplo:

- **`C:\Users\Andre\Desktop\To-DoList\Main\`**

Ejecuta el programa con el siguiente comando:
```bash
python -u "main.py"
```

---

<div align="center">
  <h1> 🔎 Pruebas</h1>
  <br>
  
  <img src="https://github.com/user-attachments/assets/03076e97-14dc-4eb8-b3a0-f43a2afdbdcc" alt="">
  <img src="https://github.com/user-attachments/assets/dd5c2902-21f7-4fb9-bc33-4f36e95555b9" alt="">
  <img src="https://github.com/user-attachments/assets/3fb38f56-8edf-4ade-8e90-b70b1ead5bab" alt="">
  <img src="https://github.com/user-attachments/assets/d13c3d7e-9944-4426-b8af-d8512b6aa766" alt="">
  <img src="https://github.com/user-attachments/assets/1dd5c3c0-047f-4212-8697-971666aba81b" alt="">
  <img src="https://github.com/user-attachments/assets/e4de4eab-b4d4-4481-a1c9-6cb05346286e" alt="">
  <img src="https://github.com/user-attachments/assets/d3758028-c9e0-4a3c-803f-e9b6e43fbdca" alt="">
  <img src="https://github.com/user-attachments/assets/969148a8-c594-48db-96da-084933586627" alt="">
  <img src="https://github.com/user-attachments/assets/6db6f8d2-4359-448b-8f20-c02baca165ad" alt="">
  <img src="https://github.com/user-attachments/assets/d71031a3-5cfc-43a7-8cf0-12d3cf2ce3eb" alt="">
  <img src="https://github.com/user-attachments/assets/9bad600d-6f6d-4f50-b058-73ded12c5b9c" alt="">
  <img src="https://github.com/user-attachments/assets/02e24cb0-476b-442f-862b-28ec50b74446" alt="">
</div>


