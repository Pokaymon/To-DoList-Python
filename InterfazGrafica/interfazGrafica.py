import re
import json
import customtkinter as ctk # type: ignore
from tkinter import filedialog, messagebox
from LSE.lista import Lista
from Clase_Asignada.task import Task

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Tareas")
        self.geometry("800x500")
        self.lista = Lista()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("../Json/rubi_theme.json")

        self.center_window(800, 500)

        self.create_widgets()

    def center_window(self, width, height, window=None):
        if window is None:
            window = self
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent", border_width=0)
        self.button_frame.pack(expand=True)

        self.add_task_button = ctk.CTkButton(self.button_frame, text="Agregar Tarea", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.list_tasks_button = ctk.CTkButton(self.button_frame, text="Listar Tareas", command=self.list_tasks)
        self.list_tasks_button.pack(pady=10)

        self.mark_task_button = ctk.CTkButton(self.button_frame, text="Marcar Tarea Completada", command=self.mark_task)
        self.mark_task_button.pack(pady=10)

        self.delete_task_button = ctk.CTkButton(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

        self.import_export_button = ctk.CTkButton(self.button_frame, text="Importar / Exportar Tareas", command=self.import_export_tasks)
        self.import_export_button.pack(pady=10)

    def add_task(self):
        self.withdraw()
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("Agregar Tarea")
        self.popup.geometry("800x500")

        self.center_window(800, 500, self.popup)

        main_frame = ctk.CTkFrame(self.popup, corner_radius=10)
        main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        content_frame = ctk.CTkFrame(main_frame, fg_color="transparent", border_width=0)
        content_frame.pack(expand=True)

        ctk.CTkLabel(content_frame, text="Título:").pack(pady=5)
        self.title_entry = ctk.CTkEntry(content_frame, width=300)
        self.title_entry.pack(pady=5)

        ctk.CTkLabel(content_frame, text="Descripción:").pack(pady=5)
        self.desc_entry = ctk.CTkEntry(content_frame, width=300)
        self.desc_entry.pack(pady=20)

        ctk.CTkButton(content_frame, text="Agregar", command=self.save_task).pack(pady=10)
        self.create_back_to_menu_button(content_frame)

        self.popup.protocol("WM_DELETE_WINDOW", self.close_popup)

    def close_popup(self):
        self.popup.destroy()
        self.deiconify()

    def save_task(self):
        titulo = self.title_entry.get()
        descripcion = self.desc_entry.get()

        titulo_regex = r'^[A-Za-záéíóúÁÉÍÓÚüÜ\s.,]{1,10}$'
        descripcion_regex = r'^[A-Za-záéíóúÁÉÍÓÚüÜ\s.,]{1,50}$'

        if not re.match(titulo_regex, titulo):
            messagebox.showwarning("Advertencia", "El título debe tener un máximo de 10 caracteres y solo contener letras, espacios y tildes.")
            return

        if not re.match(descripcion_regex, descripcion):
            messagebox.showwarning("Advertencia", "La descripción debe tener un máximo de 50 caracteres y solo contener letras, espacios y tildes.")
            return

        if self.lista.titulo_existe(titulo):
            messagebox.showwarning("Advertencia", f"Ya existe una tarea con el título '{titulo}'.")
            return

        if titulo and descripcion:
            nueva_tarea = Task(titulo, descripcion)
            self.lista.ingresar_task(nueva_tarea)
            messagebox.showinfo("Éxito", "Tarea agregada con éxito.")
            self.close_popup()
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def list_tasks(self):
        self.withdraw()
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("Lista de Tareas")
        self.popup.geometry("800x500")
        self.center_window(800, 500, self.popup)

        main_frame = ctk.CTkFrame(self.popup, corner_radius=10, fg_color="#2E2E2E")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        content_frame = ctk.CTkFrame(main_frame, fg_color="transparent", border_width=0)
        content_frame.pack(expand=True)

        if not self.lista.primero:
            ctk.CTkLabel(content_frame, text="No hay tareas en la lista.").pack(pady=10)
        else:
            header_frame = ctk.CTkFrame(content_frame)
            header_frame.pack(pady=10)

            ctk.CTkLabel(header_frame, text="Título", width=180, anchor="w").grid(row=0, column=0, padx=5)
            ctk.CTkLabel(header_frame, text="Descripción", width=360, anchor="w").grid(row=0, column=1, padx=5)
            ctk.CTkLabel(header_frame, text="Estado", width=100, anchor="w").grid(row=0, column=2, padx=5)

            rows_frame = ctk.CTkFrame(content_frame)
            rows_frame.pack(pady=10)

            actual = self.lista.primero
            row = 1
            while actual:
                task = actual.task
                estado = "Completada" if task.completada else "Pendiente"

                ctk.CTkLabel(rows_frame, text=task.titulo, width=180, anchor="w", justify="left").grid(row=row, column=0, padx=5)
                ctk.CTkLabel(rows_frame, text=task.descripcion, width=360, anchor="w", justify="left").grid(row=row, column=1, padx=5)
                ctk.CTkLabel(rows_frame, text=estado, width=100, anchor="w", justify="left").grid(row=row, column=2, padx=5)

                row += 1
                actual = actual.siguiente

        self.create_back_to_menu_button(content_frame)
        self.popup.protocol("WM_DELETE_WINDOW", self.close_popup)

    def mark_task(self):
        self.withdraw()
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("Marcar Tarea")
        self.popup.geometry("800x500")

        self.center_window(800, 500, self.popup)

        main_frame = ctk.CTkFrame(self.popup, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        center_frame = ctk.CTkFrame(main_frame, fg_color="transparent", border_width=0)
        center_frame.pack(expand=True)

        ctk.CTkLabel(center_frame, text="Título de la tarea a marcar:").pack(pady=5)
        self.title_entry = ctk.CTkEntry(center_frame, width=300)
        self.title_entry.pack(pady=20)

        ctk.CTkButton(center_frame, text="Marcar", command=self.confirm_complete_task).pack(pady=10)

        self.create_back_to_menu_button(center_frame)
        self.popup.protocol("WM_DELETE_WINDOW", self.close_popup)

    def confirm_complete_task(self):
        titulo = self.title_entry.get()
        tarea = self.lista.titulo_existe(titulo)

        if tarea:
            confirmacion = messagebox.askyesno("Confirmar", f"¿Está seguro de marcar como completada la tarea '{titulo}' con descripción '{tarea.descripcion}'?")
            
            if confirmacion:
                self.lista.marcar_completada(titulo)
                messagebox.showinfo("Completada", f"La tarea '{titulo}' ha sido marcada como completada.")
                self.close_popup()
            else:
                self.close_popup()
        else:
            messagebox.showerror("Error", f"No se encontró la tarea '{titulo}', por favor intente con otro nombre.")

    def delete_task(self):
        self.withdraw()
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("Eliminar Tarea")
        self.popup.geometry("800x500")

        self.center_window(800, 500, self.popup)

        main_frame = ctk.CTkFrame(self.popup, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        center_frame = ctk.CTkFrame(main_frame, fg_color="transparent", border_width=0)
        center_frame.pack(expand=True)

        ctk.CTkLabel(center_frame, text="Título de la tarea a eliminar:").pack(pady=5)
        self.title_entry = ctk.CTkEntry(center_frame, width=300)
        self.title_entry.pack(pady=20)

        ctk.CTkButton(center_frame, text="Eliminar", command=self.remove_task).pack(pady=10)

        self.create_back_to_menu_button(center_frame)
        self.popup.protocol("WM_DELETE_WINDOW", self.close_popup)

    def remove_task(self):
        titulo = self.title_entry.get()
        tarea = self.lista.titulo_existe(titulo)

        if tarea:
            confirmacion = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar la tarea '{titulo}' con descripción '{tarea.descripcion}'?")
            
            if confirmacion:
                self.lista.eliminar_task(titulo)
                messagebox.showinfo("Eliminada", f"La tarea '{titulo}' ha sido eliminada correctamente.")
                self.close_popup()
            else:
                self.close_popup()
        else:
            messagebox.showerror("Error", f"No se encontró la tarea '{titulo}', por favor intente con otro nombre.")

    def import_export_tasks(self):
        self.withdraw()
        self.popup = ctk.CTkToplevel(self)
        self.popup.title("Importar/Exportar Tareas")
        self.popup.geometry("800x500")

        self.center_window(800, 500, self.popup)

        main_frame = ctk.CTkFrame(self.popup, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        center_frame = ctk.CTkFrame(main_frame, fg_color="transparent", border_width=0)
        center_frame.pack(expand=True)

        ctk.CTkButton(center_frame, text="Importar desde JSON", command=self.import_tasks).pack(pady=10)
        ctk.CTkButton(center_frame, text="Exportar a JSON", command=self.export_tasks).pack(pady=20)

        self.create_back_to_menu_button(center_frame)
        self.popup.protocol("WM_DELETE_WINDOW", self.close_popup)

    def import_tasks(self):
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo JSON",
            filetypes=[("Archivos JSON", "*.json")]
        )
        if archivo:
            try:
                self.lista.import_tasks(archivo)
                messagebox.showinfo("Perfecto", "Tareas importadas con éxito.")
            except json.JSONDecodeError:
                messagebox.showwarning(
                    "Error de formato",
                    "El archivo seleccionado no tiene un formato JSON válido. Revise el contenido del archivo."
                )
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Ocurrió un error al importar las tareas: {str(e)}"
                )
        self.close_popup()

    def export_tasks(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
        if archivo:
            self.lista.export_tasks(archivo)
            messagebox.showinfo("Bien", "Tareas exportadas con éxito.")
        self.close_popup()

    def create_back_to_menu_button(self, parent_frame):
        ctk.CTkButton(parent_frame, text="Volver al Menú", command=self.close_popup).pack(pady=10)