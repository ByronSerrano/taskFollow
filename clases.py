# Todas las clases del proyecto

class Task:
   '''
    Se inicializa una clase llamada Task, la cual representa la tarea

    param: con titulo y la descripción de la tarea
    param no required: 
   '''
   def __init__(self, title, description):
       self.title = title
       self.description = description
       self.completed = False

    # Se crea está función la cual cambia el param completed de la clase a un valor True, para indicar que ya está completa
   def complete(self):
       self.completed = True

    # Regresa un formato de texto para visualizar si la tarea está completa
   def __str__(self):
       return f" - Titulo de Tarea: '{self.title}' /// Descripción: {self.description} /// Estado:  {'completada' if self.completed else 'pendiente'}\n"


class TaskManager:
   '''
    Se inicializa una clase llamada TaskManager

    param no required: una lista de tareas vacia
   '''
   def __init__(self):
       self.tasks = []

    # Se añade la tarea a lista de tareas
   def add_task(self, task):
       self.tasks.append(task)

    # Elimina la tarea en la lista de tareas
   def remove_task(self, task):
       if task in self.tasks:
           self.tasks.remove(task)
       else:
           print(f"Tarea '{task.title}' no encontrada.")

    # Se lista todas las tareas
   def list_tasks(self):
       for task in self.tasks:
           print(task)

    # Busca la tarea, por titulo, pasada por param
   def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
               return task
        return task
