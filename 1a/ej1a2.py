"""
Enunciado:
Desarrolla un conjunto de funciones para gestionar eventos en diferentes zonas horarias, facilitando la creación,
manipulación y consulta de eventos programados utilizando Python, con especial énfasis en el manejo de fechas, horas y
zonas horarias mediante datetime y pytz.

Funciones a desarrollar:
- `create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Crea un diccionario representando un evento, incluyendo su nombre, fecha y hora de inicio, y zona horaria.
    Parámetros:
        - `name` (str): Nombre del evento.
        - `datetime_start` (datetime): Fecha y hora de inicio del evento.
        - `timezone_str` (str): Identificador de la zona horaria del evento.

- `time_until_event(event: Dict[str, str]) -> timedelta`:
    Descripción:
    Calcula el tiempo restante hasta el inicio de un evento dado.
    Parámetros:
        - `event` (Dict[str, str]): Evento para calcular el tiempo restante.

- `change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]`:
    Descripción:
    Cambia la zona horaria de un evento existente a una nueva especificada.
    Parámetros:
        - `event` (Dict[str, str]): Evento a modificar.
        - `new_timezone_str` (str): Nueva zona horaria.

- `find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]`:
    Descripción:
    Identifica el próximo evento entre una lista de eventos, considerando la fecha y hora actual.
    Parámetros:
        - `events` (List[Dict[str, str]]): Lista de eventos entre los cuales buscar el próximo evento.

Ejemplo:

    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    
    time_to_event = time_until_event(event)
    print(f"Time until '{event['name']}':", time_to_event)

    changed_event1 = change_event_timezone(event1, "America/New_York")
    print(f"Event after timezone change: {changed_event1}")

    next_event = find_next_event(events)
    print("\nThe next event is:", next_event["name"])

Salida esperada:
- Crear eventos con sus respectivas zonas horarias.
    {'name': 'Global Meeting', 'datetime_start': datetime.datetime(2024, 9, 10, 10, 0), 'timezone': 'UTC'}

- Mostrar el tiempo restante hasta el inicio de cada uno de los eventos.
    "Time until 'Global Meeting': 1 day, 20:00:00"

- Cambiar dinámicamente la zona horaria de un evento.
    "Event after timezone change: {'name': 'Global Meeting', 'datetime_start': datetime.datetime(2024, 9, 10, 6, 0,
        tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>), 'timezone': 'America/New_York'}"

- Calcular cuál será el siguiente evento.
    "The next event is: Global Meeting"
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import pytz


def create_event(name: str, datetime_start: datetime, timezone_str: str) -> Dict[str, str]:
    # Obtenemos el objeto correspondiente a la zona horaria indicada.
    zona_horaria = pytz.timezone(timezone_str)
    # Asociamos la zona horaria a la fecha de inicio del evento.
    datetime_start = zona_horaria.localize(datetime_start)
    # Creamos un diccionario con el nombre, la fecha de inicio y la zona horaria del evento.
    event = {
        "name": name,
        "datetime_start": datetime_start,
        "timezone": timezone_str
    }
    return event


def time_until_event(event: Dict[str, str]) -> timedelta:
    # Obtenemos el objeto de zona horaria a partir del nombre almacenado en el diccionario.
    zona_horaria = pytz.timezone(event["timezone"])
    # Obtenemos la fecha y hora actuales en la zona horaria del evento.
    dia_actual = datetime.now(zona_horaria)
    # Guardamos la fecha del evento en una variable.
    dia_evento = event["datetime_start"]
    # Calculamos el tiempo restante hasta el evento restando ambas fechas.
    cuenta_atras = dia_evento - dia_actual
    return cuenta_atras


def change_event_timezone(event: Dict[str, str], new_timezone_str: str) -> Dict[str, str]:
    # Obtenemos los objetos correspondientes a la zona horaria nueva.
    zona_horaria_nueva = pytz.timezone(new_timezone_str)
    # Guardamos la fecha del evento original en una variable.
    fecha_evento_original = event["datetime_start"]
    # Convertimos la fecha del evento a la nueva zona horaria, manteniendo el mismo instante temporal.
    fecha_evento_nueva = fecha_evento_original.astimezone(zona_horaria_nueva)
    # Actualizamos la fecha de inicio y la zona horaria del evento en el diccionario original.
    event["datetime_start"] = fecha_evento_nueva
    event["timezone"] = new_timezone_str
    return event


def find_next_event(events: List[Dict[str, str]]) -> Optional[Dict[str, str]]:
    # Inicializamos la variable que almacenará el próximo evento.
    proximo_evento = None
    # Recorremos todos los eventos de la lista.
    for event in events:
        # Calculamos el tiempo que queda hasta el inicio del evento actual.
        tiempo_restante = time_until_event(event)
        # Comprobamos si el evento ya ha pasado. Recuerda que tiempo_restante es un objeto tipo timedelta
        if tiempo_restante < timedelta(0):
            pass
        else:
            # Si todavía no tenemos ningún evento próximo, guardamos el actual.
            if proximo_evento is None:
                proximo_evento = event
            # Comparamos el tiempo restante del evento actual con el del evento guardado.
            elif time_until_event(proximo_evento) < tiempo_restante:
                # Si el evento guardado está más próximo, mantenemos ese evento.
                pass
            else:
                # Si el evento actual está más próximo, lo establecemos como próximo evento.
                proximo_evento = event
    # Devolvemos el evento más próximo o None si no hay eventos futuros.
    return proximo_evento

# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    event1 = create_event("Global Meeting", datetime(2024, 9, 10, 10, 0), "UTC")
    event2 = create_event("Python Talk", datetime(2024, 9, 10, 18, 30), "America/New_York")
    event3 = create_event("Data Science Workshop", datetime(2024, 9, 10, 12, 0), "Europe/London")

    for event in [event1, event2, event3]:
        time_to_event = time_until_event(event)
        print(f"Time until '{event['name']}':", time_to_event)

    changed_event1 = change_event_timezone(event1, "America/New_York")
    print(f"Event after timezone change: {changed_event1}")

    events = [event1, event2, event3]
    next_event = find_next_event(events)
    if next_event:
        print("\nThe next event is:", next_event["name"])
    else:
        print("There are no future events.")
