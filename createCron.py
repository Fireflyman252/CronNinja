
import random
import requests
import json


def format(minute, minuteString, hour, hourString, day, dayString, month, monthString, dow, dowString):
    cronString = f"{minute}, {hour}, {day}, {month}, {dow}"
    print(cronString)
    humanString = f"{minuteString}{hourString}{dayString}{dowString}{monthString}"
    print(humanString)
    payload = {"prompt": f"Reword the following sentence, only return the reworded sentence: {humanString}"}
    response = requests.post("http://192.168.1.146:8000/query", json=payload)
    print(response.json()["response"])
    final = humanString
    if random.choice([True, False]):
        final = response.json()["response"]
    return {
        "cron": cronString,
        "simpleString": humanString,
        "chatString": response.json()["response"],
        "final": final
    }

def createMinute(simple):
    minute = "*"
    minuteString = "At every minute"

    if (simple):
        randomNum = random.randint(1,3)
    else:
        randomNum = random.randint(1,6)

    if randomNum == 1:
        minute = "*"
        minuteString = "At every minute"

    elif randomNum == 2:
        minute = random.randint(0,59);
        minuteString = f"At minute {minute}"

    elif randomNum == 3:
        first = random.randint(0,59)
        second = random.randint(0,59)
        while first == second:
            second = random.randint(0,59)
        if first<second:
            minute = f'{first}-{second}'
            minuteString = f"At every minute from {first} to {second}"
        else:
            minute = f'{second}-{first}'
            minuteString = f"At every minute from {second} to {first}"

    elif randomNum == 4:
        first = random.randint(0,59)
        second = random.randint(0,59)
        third = random.randint(0,59)
        while first == second:
            second = random.randint(0,59)
        while second == third or first == third:
            third = random.randint(0,59)
        minute = f'{first},{second},{third}'
        minuteString = f"At minutes {first}, {second} and {third}"

    elif randomNum == 5:
        first = random.randint(1,20)
        if first == 1:
            minute = f'*/{first}'
            minuteString = f"At every minute"
        elif first == 2:
            minute = f'*/{first}'
            minuteString = f"At every second minute"
        elif first == 3:
            minute = f'*/{first}'
            minuteString = f"At every third minute"
        else:
            minute = f'*/{first}'
            minuteString = f"At every {first}th minute"

    elif randomNum == 6:
        first = random.randint(1,10)
        second = random.randint(0,10)
        if first == 1:
            minute = f'{second}/{first}'
            minuteString = f"At every minute starting at {second}"
        elif first == 2:
            minute = f'{second}/{first}'
            minuteString = f"At every second minute starting at {second}"
        elif first == 3:
            minute = f'{second}/{first}'
            minuteString = f"At every third minute starting at {second}"
        else:
            minute = f'{second}/{first}'
            minuteString = f"At every {first}th minute starting at {second}"

    return minute, minuteString

def createHour(simple):

    hour = "*"
    hourString = ""

    if (simple):
        randomNum = random.randint(1,3)
    else:
        randomNum = random.randint(1,6)

    if randomNum == 1:
        hour = "*"
        hourString = ""

    elif randomNum == 2:
        hour = random.randint(0,23);
        hourString = f" past hour {hour}"

    elif randomNum == 3:
        first = random.randint(0,23)
        second = random.randint(0,23)
        while first == second:
            second = random.randint(0,23)
        if first<second:
            hour = f'{first}-{second}'
            hourString = f" past every hour from {first} to {second}"
        else:
            hour = f'{second}-{first}'
            hourString = f" past every hour from {second} to {first}"

    elif randomNum == 4:
        first = random.randint(0,23)
        second = random.randint(0,23)
        third = random.randint(0,23)
        while first == second:
            second = random.randint(0,23)
        while second == third or first == third:
            third = random.randint(0,23)
        hour = f'{first},{second},{third}'
        hourString = f" past hours {first}, {second} and {third}"

    elif randomNum == 5:
        first = random.randint(1,10)
        if first == 1:
            hour = f'*/{first}'
            hourString = f" past every hour"
        elif first == 2:
            hour = f'*/{first}'
            hourString = f" past every second hour"
        elif first == 3:
            hour = f'*/{first}'
            hourString = f" past every third hour"
        else:
            hour = f'*/{first}'
            hourString = f" past every {first}th hour"

    elif randomNum == 6:
        first = random.randint(1,10)
        second = random.randint(0,10)
        if first == 1:
            hour = f'{second}/{first}'
            hourString = f" past every hour starting at {second}"
        elif first == 2:
            hour = f'{second}/{first}'
            hourString = f" past every second hour starting at {second}"
        elif first == 3:
            hour = f'{second}/{first}'
            hourString = f" past every third hour starting at {second}"
        else:
            hour = f'{second}/{first}'
            hourString = f" past every {first}th hour starting at {second}"

    return hour, hourString


def createDay(simple):

    day = "*"
    dayString = ""

    if (simple):
        randomNum = random.randint(1,3)
    else:
        randomNum = random.randint(1,6)

    if randomNum == 1:
        day = "*"
        dayString = ""

    elif randomNum == 2:
        day = random.randint(0,31);
        dayString = f" on day of the month {day}"

    elif randomNum == 3:
        first = random.randint(0,31)
        second = random.randint(0,31)
        while first == second:
            second = random.randint(0,31)
        if first<second:
            day = f'{first}-{second}'
            dayString = f" on day of the month from {first} to {second}"
        else:
            day = f'{second}-{first}'
            dayString = f" on day of the month from {second} to {first}"

    elif randomNum == 4:
        first = random.randint(0,31)
        second = random.randint(0,31)
        third = random.randint(0,31)
        while first == second:
            second = random.randint(0,31)
        while second == third or first == third:
            third = random.randint(0,31)
        day = f'{first},{second},{third}'
        dayString = f" on days of the month {first}, {second} and {third}"

    elif randomNum == 5:
        first = random.randint(1,10)
        if first == 1:
            day = f'*/{first}'
            dayString = f" on every day of the month"
        elif first == 2:
            day = f'*/{first}'
            dayString = f" on every second day of the month"
        elif first == 3:
            day = f'*/{first}'
            dayString = f" on every third day of the month"
        else:
            day = f'*/{first}'
            dayString = f" on every {first}th hour"

    elif randomNum == 6:
        first = random.randint(1,10)
        second = random.randint(0,10)
        if first == 1:
            day = f'{second}/{first}'
            dayString = f" on every day of the month starting at {second}"
        elif first == 2:
            day = f'{second}/{first}'
            dayString = f" on every second day of the month starting at {second}"
        elif first == 3:
            day = f'{second}/{first}'
            dayString = f" on every third day of the month starting at {second}"
        else:
            day = f'{second}/{first}'
            dayString = f" on every {first}th day of the month starting at {second}"

    return day, dayString

def convertIntToMonth(monthInt):
    rv = ""
    if monthInt == 1:
        rv = "January"
    elif monthInt == 2:
        rv = "February"
    elif monthInt == 3:
        rv = "March"
    elif monthInt == 4:
        rv = "April"
    elif monthInt == 5:
        rv = "May"
    elif monthInt == 6:
        rv = "June"
    elif monthInt == 7:
        rv = "July"
    elif monthInt == 8:
        rv = "August"
    elif monthInt == 9:
        rv = "Septemeber"
    elif monthInt == 10:
        rv = "October"
    elif monthInt == 11:
        rv = "Novemeber"
    elif monthInt == 12:
        rv = "December"
    return rv

def createMonth(simple):

    month = "*"
    monthString = ""

    if not simple:
        randomNum = random.randint(1,6)

        if randomNum == 1:
            month = "*"
            dayString = ""

        elif randomNum == 2:
            month = random.randint(1,12);
            monthString = f" in {convertIntToMonth(month)}"

        elif randomNum == 3:
            first = random.randint(1,12)
            second = random.randint(1,12)
            while first == second:
                second = random.randint(1,12)
            if first<second:
                month = f'{first}-{second}'
                monthString = f" in {convertIntToMonth(first)} to {convertIntToMonth(second)}"
            else:
                month = f'{second}-{first}'
                monthString = f" in {convertIntToMonth(second)} to {convertIntToMonth(first)}"

        elif randomNum == 4:
            first = random.randint(0,12)
            second = random.randint(0,12)
            third = random.randint(0,12)
            while first == second:
                second = random.randint(0,12)
            while second == third or first == third:
                third = random.randint(0,12)
            month = f'{first},{second},{third}'
            monthString = f" in {convertIntToMonth(first)}, {convertIntToMonth(second)} and {convertIntToMonth(third)}"

        elif randomNum == 5:
            first = random.randint(1,10)
            if first == 1:
                month = f'*/{first}'
                monthString = f" in every month"
            elif first == 2:
                month = f'*/{first}'
                monthString = f" in every second month"
            elif first == 3:
                month = f'*/{first}'
                monthString = f" in every third month"
            else:
                month = f'*/{first}'
                monthString = f" in every {first}th month"

        elif randomNum == 6:
            first = random.randint(1,10)
            second = random.randint(1,10)
            if first == 1:
                month = f'{second}/{first}'
                monthString = f" in every month starting at {convertIntToMonth(second)}"
            elif first == 2:
                month = f'{second}/{first}'
                monthString = f" in every second month starting at {convertIntToMonth(second)}"
            elif first == 3:
                month = f'{second}/{first}'
                monthString = f" in every third month starting at {convertIntToMonth(second)}"
            else:
                month = f'{second}/{first}'
                monthString = f" in every {first}th month starting at {convertIntToMonth(second)}"

    return month, monthString

def convertIntToDOW(dayInt):
    rv = ""
    if dayInt == 1:
        rv = "Monday"
    elif dayInt == 2:
        rv = "Tuesday"
    elif dayInt == 3:
        rv = "Wednesday"
    elif dayInt == 4:
        rv = "Thursday"
    elif dayInt == 5:
        rv = "Friday"
    elif dayInt == 6:
        rv = "Saturday"
    elif dayInt == 7:
        rv = "Sunday"
    return rv

def createDOW(simple):

    month = "*"
    monthString = ""

    if not simple:
        randomNum = random.randint(1,6)

        if randomNum == 1:
            month = "*"
            dayString = ""

        elif randomNum == 2:
            month = random.randint(1,7);
            monthString = f" on {convertIntToDOW(month)}"

        elif randomNum == 3:
            first = random.randint(1,7)
            second = random.randint(1,7)
            while first == second:
                second = random.randint(1,7)
            if first<second:
                month = f'{first}-{second}'
                monthString = f" in {convertIntToDOW(first)} to {convertIntToDOW(second)}"
            else:
                month = f'{second}-{first}'
                monthString = f" in {convertIntToDOW(second)} to {convertIntToDOW(first)}"

        elif randomNum == 4:
            first = random.randint(1,7)
            second = random.randint(1,7)
            third = random.randint(1,7)
            while first == second:
                second = random.randint(0,31)
            while second == third or first == third:
                third = random.randint(0,31)
            month = f'{first},{second},{third}'
            monthString = f" in {convertIntToDOW(first)}, {convertIntToDOW(second)} and {convertIntToDOW(third)}"

        elif randomNum == 5:
            first = random.randint(1,10)
            if first == 1:
                month = f'*/{first}'
                monthString = f" on every day"
            elif first == 2:
                month = f'*/{first}'
                monthString = f" on every second day"
            elif first == 3:
                month = f'*/{first}'
                monthString = f" on every third day"
            else:
                month = f'*/{first}'
                monthString = f" on every {convertIntToDOW(first)}th day of the week"

        elif randomNum == 6:
            first = random.randint(1,10)
            second = random.randint(0,10)
            if first == 1:
                month = f'{second}/{first}'
                monthString = f" on every day starting on {convertIntToDOW(second)}"
            elif first == 2:
                month = f'{second}/{first}'
                monthString = f" in every second day starting on {convertIntToDOW(second)}"
            elif first == 3:
                month = f'{second}/{first}'
                monthString = f" in every third day starting on {convertIntToDOW(second)}"
            else:
                month = f'{second}/{first}'
                monthString = f" in every {first}th day starting on {convertIntToDOW(second)}"

    return month, monthString



def createCron(simple=True):

    minute = "*"
    minuteString = ""
    hour = "*"
    hourString = ""
    day = "*"
    dayString = ""
    month = "*"
    monthString = ""
    dow = "*"
    dowString = ""

    # minute star
    minute = "*"
    minuteString = "At every minute"
    minute, minuteString = createMinute(simple)
    hour, hourString = createHour(simple)
    day, dayString = createDay(simple)
    month, monthString = createMonth(simple)
    dow, dowString = createDOW(simple)


    return format(minute, minuteString, hour, hourString, day, dayString, month, monthString, dow, dowString)



number = 1000
data = []
for i in range(number):
    print(f"Creating: {i}")
    item = createCron(random.choice([True, False]))
    print(item)
    data.append(item)
print(data)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
