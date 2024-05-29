from clases import *
from utils import *

# Declarar a la constante de manager
MANAGER = TaskManager()
task = userCreationTask()

MANAGER.add_task(task)


completeTask(MANAGER)
print('')
MANAGER.list_tasks()
# manager.find_task("Pay bills")

