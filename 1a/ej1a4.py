"""
Enunciado:
Desarrolla un sistema de gestión de tareas simple en Python, utilizando `Enum` para definir estados de las tareas y
`typing.NamedTuple` para modelar las tareas y tipado estático.

Funciones a desarrollar:
- `create_task(title: str) -> int`:
    Descripción:
    Añade una nueva tarea al sistema con un estado inicial "Pendiente". La función genera un ID único para cada tarea,
    lo asigna junto con el título proporcionado, y retorna el ID de la tarea creada, mantiene la siguiente estructura:
    `tasks[id] = Task(id, title, TaskStatus.PENDING)`.
    Parámetros:
        - `title` (str): El título de la tarea a crear.

- `change_task_status(task_id: int, new_status: TaskStatus) -> bool`:
    Descripción:
    Actualiza el estado de una tarea existente basándose en su ID. Retorna `True` si la operación es exitosa, o `False`
    si la tarea no se encuentra realizada.
    Parámetros:
        - `task_id` (int): El ID de la tarea a actualizar.
        - `new_status` (TaskStatus): El nuevo estado asignado a la tarea.

- `list_tasks() -> None`:
    Descripción:
    Imprime una lista de todas las tareas registradas, manteniendo el siguiente formato: "ID: {task.id},
    Title: {task.title}, Status: {task.status.value}".


Clases y Enums:
- `TaskStatus(Enum)`: Define los posibles estados de una tarea, incluyendo "Pendiente", "En Progreso" y "Completada".
- `Task(typing.NamedTuple)`: Modelo de una tarea, incluyendo campos para ID, título y estado.

Ejemplo:
    id1 = create_task("Learn Python")
    id2 = create_task("Read Enum documentation")
    change_task_status(id1, TaskStatus.IN_PROGRESS)
    change_task_status(id2, TaskStatus.COMPLETED)
    list_tasks()

Salida esperada:
- Creación y actualización exitosa de tareas en el sistema, seguida por una impresión de todas las tareas, mediante
`Enum` para estados de tarea y `typing.NamedTuple` para la estructura de datos de tarea.
"""

from enum import Enum
from typing import NamedTuple, Dict


class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Task(NamedTuple):
    id: int
    title: str
    status: TaskStatus
    
    
tasks: Dict[int, Task] = {}


def create_task(title: str) -> int:
    # Generamos un ID único para la nueva tarea.
    task_id = len(tasks) + 1
    # Creamos la tarea con el título indicado y estado inicial pendiente.
    tasks[task_id] = Task(task_id, title, status=TaskStatus.PENDING)
    # Devolvemos el ID de la tarea creada.
    return task_id



def change_task_status(task_id: int, new_status: TaskStatus) -> bool:
    # Comprobamos si el ID de la tarea existe en el diccionario.
    if task_id in tasks:
        # Creamos una nueva instancia de Task con el mismo ID y título, pero con el nuevo estado. Porque al ser inmutable no se puede modificar sólo ese valor
        tasks[task_id] = Task(task_id, tasks[task_id].title, new_status)
        # Indicamos que el estado se ha actualizado correctamente.
        return True
    else:
        # Indicamos que no se ha encontrado ninguna tarea con el ID proporcionado.
        return False


def list_tasks() -> None:
    # Recorremos todos los objetos Task almacenados en el diccionario.
    for task in tasks.values():
        # Imprimimos el ID, el título y el valor del estado de cada tarea.
        # Se utiliza task.status.value en lugar de task.status, porque queremos mostrar el 
        # texto del estado ("Pending", "In Progress" o "Completed") y no el nombre del miembro del Enum.
        print(f"ID: {task.id}, Title: {task.title}, Status: {task.status.value}")


# Para probar el código, descomenta las siguientes líneas 
if __name__ == "__main__":
    id1 = create_task("Learn Python")
    id2 = create_task("Read Enum documentation")
    change_task_status(id1, TaskStatus.IN_PROGRESS)
    change_task_status(id2, TaskStatus.COMPLETED)
    list_tasks()
