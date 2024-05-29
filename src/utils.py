# Todas las funciones y constanstes que tiene el proyecto
from .clases import *

# Declarar a la constante de manager
MANAGER = TaskManager()

# Permite al usuario entrar los param de la tarea por consola
def userCreationTask():
    print('\nCreación de tareas')
    title = input('-Ingresa el titulo de la tarea: ')
    description = input('-Ingresa la descripción de la tarea: ')
    task = Task(title , description)
    print('----Tarea creada-----')
    return task

# Permite a los usuarios insertar la tarea que se quiere marcar como completada por consola
def completeTask(manager):
    print('\nMarcar como completada una tarea')
    title = input('-Pon el titulo de la tarea que quieras marcar como completada: ')
    task = manager.find_task(title)
    task.complete()
    print('----Tarea Actualizada-----')

# Permite a los usuarios insertar la tarea que se quiere eliminar por consola
def deleteTask(manager):
    print('\nEliminar una tarea')
    title = input('-Pon el titulo de la tarea que quieras eliminar: ')
    task = manager.find_task(title)
    manager.remove_task(task)
    print('----Tarea Eliminada-----')


# Permite a los usuarios insertar la tarea que se quiere buscar por consola
def findTask(manager):
    print('\nBuscar una tarea')
    findedTask = manager.find_task()
    if findedTask == None:
        pass
    else:
        print(findedTask)

# Permite al usuario seleccionar una opción para ejecutar
def run():
    option = 0
    while option != 6:
        print('\n¿Que quieres hacer?')
        print('1. Crear tarea')
        print('2. Marcar tarea como completada')
        print('3. Listar tareas')
        print('4. Eliminar tarea')
        print('5. Buscar tarea')
        print('6. Salir')
        option = int(input('Selecciona una opción: '))
        match option:
            case 1:
                task = userCreationTask()
                MANAGER.add_task(task)
            case 2:
                completeTask(MANAGER)
            case 3:
                MANAGER.list_tasks()
            case 4:
                deleteTask(MANAGER)
            case 5:
                findTask(MANAGER)
            case 6:
                print('\nAdios!!! ')
                break
            case _:
                print('La opción no válida')
