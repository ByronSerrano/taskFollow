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
       return f"\n - Titulo de Tarea: '{self.title}' /// Descripción: {self.description} /// Estado:  {'completada' if self.completed else 'pendiente'}\n"


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
            print(f"Tarea '{'' if task is None else task.title}' no encontrada.")

    # Se lista todas las tareas
    def list_tasks(self):
        if not self.tasks:
            print('----No hay tareas----')
        else:
            for task in self.tasks:
                print(task)

    # Busca la tarea, por titulo, pasada por param
    def find_task(self, title=None):
        if not self.tasks:
            print('----Actualmente no hay tareas para poder buscar---')
            return None
        else:
            title = input('-Pon el titulo de la tarea que quieras buscar: ')
            for task in self.tasks:
                if task.title == title:
                    return task
            return task
