from datetime import date
from .config import weekdays, URL
from .parser import parse
from math import ceil
import pprint

def get_cur_day_str():
    return weekdays[date.isoweekday(date.today())]


def week_of_month(dt):
    """ Returns the week of the month for the specified date.
    """

    first_day = dt.replace(day=1)
    
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()%7

    return int(ceil(adjusted_dom/7.0))


weekday_num = date.today().strftime("%d")


def get_json(group):
    print(parse(f"{URL}{group}")['schedules'])
    return parse(f"{URL}{group}")['schedules']


def get_schedule(dict_):
    subjects = []
    for elem in dict_:
        if elem['weekNumber'] == None or week_of_month(date.today()) in elem['weekNumber']:
            if elem['subject'] == None:
                subjects.append([elem['note'], elem['startLessonTime'], elem['endLessonTime']])
            else:
                subjects.append([elem['subject'], elem['startLessonTime'], elem['endLessonTime']])
    return subjects



#print(pprint.pformat(json_dict['schedules']['Вторник']))
print(pprint.pformat(get_json('010901')['Четверг']))


