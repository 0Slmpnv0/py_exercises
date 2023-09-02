from dataclasses import dataclass
from operator import le


@dataclass
class Time_measure_parametres:
    name: str
    divider: int
    quantity: int


def format_duration(seconds: int):
    result_list: list[str] = []
    second = Time_measure_parametres('second', 1, 0)
    minute = Time_measure_parametres('minute', 60, 0)
    hour = Time_measure_parametres('hour', 3600, 0)
    day = Time_measure_parametres('day', 86400, 0)
    year = Time_measure_parametres('year', 31536000, 0)

    time_measure_list = [year, day, hour, minute, second]
    for time in time_measure_list:
        time.quantity = int(seconds / time.divider)
        seconds -= time.quantity * time.divider
        if time.quantity > 1:
            time.name += 's'
        if time.quantity:
            result_list.append(str(time.quantity) + ' ' + time.name)
    if len(result_list) > 1:
        result_list.append(result_list.pop(-2) + ' and ' + result_list.pop(-1))
    if not len(result_list):
        result_list.append('now')
    return ', '.join(result_list)
