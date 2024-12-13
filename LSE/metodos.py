import json
from sqlalchemy.orm import sessionmaker
from Database.connection import engine, TaskDB, TaskStatus
from LSE.nodo import Nodo
from Clase_Asignada.task import Task

Session = sessionmaker(bind=engine)

class Metodos:
    def __init__(self, lista):
        self.lista = lista
        self.session = Session()
        self.sync_with_db()

    def sync_with_db(self):
        """Sincroniza las tareas desde la base de datos a la lista enlazada."""
        tareas_db = self.session.query(TaskDB).all()
        for tarea_db in tareas_db:
            task = Task(
                titulo=tarea_db.titulo,
                descripcion=tarea_db.descripcion
            )
            if tarea_db.completada == TaskStatus.Completada:
                task.marcar_completada()
            self.ingresar_task(task, sync_db=False)

    def titulo_existe(self, titulo):
        actual = self.lista.primero
        while actual is not None:
            if actual.task.titulo == titulo:
                return actual.task
            actual = actual.siguiente
        return None

    def ingresar_task(self, task, sync_db=True):
        """Agrega una tarea a la lista y opcionalmente a la base de datos."""
        if self.titulo_existe(task.titulo):
            print(f"Error: Ya existe una tarea con el título '{task.titulo}'.")
            return
        nuevo_nodo = Nodo(task)
        if self.lista.primero is None:
            self.lista.primero = nuevo_nodo
        else:
            actual = self.lista.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

        if sync_db:
            # Agregar tarea a la base de datos
            nueva_tarea_db = TaskDB(
                titulo=task.titulo,
                descripcion=task.descripcion,
                completada=TaskStatus.Completada if task.completada else TaskStatus.Pendiente
            )
            self.session.add(nueva_tarea_db)
            self.session.commit()
            print(f"Tarea '{task.titulo}' agregada a la base de datos.")

    def listar_tasks(self):
        if self.lista.primero is None:
            print("No hay tareas en la lista.")
        else:
            actual = self.lista.primero
            while actual is not None:
                print(actual.task)
                print("-" * 30)
                actual = actual.siguiente

    def marcar_completada(self, titulo):
        """Marca una tarea como completada en la lista y la base de datos."""
        actual = self.lista.primero
        while actual is not None:
            if actual.task.titulo == titulo:
                actual.task.marcar_completada()
                print(f"Tarea '{titulo}' marcada como completada.")

                # Actualizar en la base de datos
                tarea_db = self.session.query(TaskDB).filter_by(titulo=titulo).first()
                if tarea_db:
                    tarea_db.completada = TaskStatus.Completada
                    self.session.commit()
                return
            actual = actual.siguiente
        print(f"No se encontró una tarea con el título '{titulo}'.")

    def eliminar_task(self, titulo):
        """Elimina una tarea de la lista y de la base de datos."""
        actual = self.lista.primero
        anterior = None
        while actual is not None:
            if actual.task.titulo == titulo:
                if anterior is None:
                    self.lista.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                # Eliminar de la base de datos
                tarea_db = self.session.query(TaskDB).filter_by(titulo=titulo).first()
                if tarea_db:
                    self.session.delete(tarea_db)
                    self.session.commit()
                    print(f"Tarea '{titulo}' eliminada de la base de datos.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f"No se encontró una tarea con el título '{titulo}'.")

    def export_tasks(self, archivo):
        """Exporta las tareas de la base de datos a un archivo JSON."""
        tareas = []
        tareas_db = self.session.query(TaskDB).all()
        for tarea_db in tareas_db:
            tarea = {
                "titulo": tarea_db.titulo,
                "descripcion": tarea_db.descripcion,
                "completada": tarea_db.completada.value
            }
            tareas.append(tarea)
        with open(archivo, "w") as file:
            json.dump(tareas, file, indent=4)
        print(f"Tareas exportadas exitosamente a {archivo}.")

    def import_tasks(self, archivo):
        """Importa tareas desde un archivo JSON a la base de datos y la lista."""
        try:
            with open(archivo, "r") as file:
                tareas = json.load(file)
            for tarea in tareas:
                # Verificar si la tarea ya existe en la base de datos
                if self.session.query(TaskDB).filter_by(titulo=tarea["titulo"]).first():
                    print(f"Advertencia: La tarea '{tarea['titulo']}' ya existe. Se omite.")
                    continue

                # Insertar la tarea en la base de datos
                nueva_tarea_db = TaskDB(
                    titulo=tarea["titulo"],
                    descripcion=tarea["descripcion"],
                    completada=TaskStatus.Completada if tarea["completada"] == "Completada" else TaskStatus.Pendiente
                )
                self.session.add(nueva_tarea_db)

                # Crear una tarea en la lista enlazada
                nueva_tarea = Task(
                    titulo=tarea["titulo"],
                    descripcion=tarea["descripcion"]
                )
                if tarea["completada"] == "Completada":
                    nueva_tarea.marcar_completada()
                self.ingresar_task(nueva_tarea, sync_db=False)
            
            self.session.commit()
            print(f"Tareas importadas exitosamente desde {archivo}.")
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe.")
        except json.JSONDecodeError:
            print(f"Error al leer el archivo {archivo}. Asegúrate de que sea un JSON válido.")