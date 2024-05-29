# Todas las funciones que tiene el proyecto
from clases import *

# Permite al usuario entrar los param de la tarea por consola
def userCreationTask():
    print('\nCreación de tareas')
    title = input('-Ingresa el titulo de la tarea: ')
    description = input('-Ingresa la descripción de la tarea: ')
    task = Task(title , description)
    return task

# Permite a los usuarios insertar la tarea que se quiere marcar como completada por consola
def completeTask(manager):
    print('\nMarcar como completada una tarea')
    title = input('-Pon el titulo de la tarea que quieras marcar como completada: ')
    task = manager.find_task(title)
    task.complete()
    print('Ya se te actualizó papito')
