from LSE.metodos import Metodos
class Lista:
    def __init__(self):
        self.primero = None
        self.metodos = Metodos(self)

    def titulo_existe(self, titulo):
        return self.metodos.titulo_existe(titulo)

    def ingresar_task(self, task):
        self.metodos.ingresar_task(task)

    def listar_tasks(self):
        self.metodos.listar_tasks()

    def marcar_completada(self, titulo):
        self.metodos.marcar_completada(titulo)

    def eliminar_task(self, titulo):
        self.metodos.eliminar_task(titulo)

    def export_tasks(self, archivo):
        self.metodos.export_tasks(archivo)

    def import_tasks(self, archivo):
        self.metodos.import_tasks(archivo)