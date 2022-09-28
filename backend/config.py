import enum

URL = "https://iis.bsuir.by/api/v1/schedule?studentGroup="

weekdays = {1: "Понедельник", 
            2: "Вторник", 
            3: "Среда", 
            4: "Четверг", 
            5: "Пятница", 
            6: "Суббота",
            7: "Воскресенье"}


class Week(enum.Enum):
    first: 1
    second: 2
    third: 3
    fourth: 4



