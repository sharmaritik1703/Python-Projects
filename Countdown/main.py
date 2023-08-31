__author__ = "Ritik Sharma"
__email__ = "sharmaritik351@gmail.com"

from time import sleep

hours = int(input("Enter the starting hours: "))
minutes = int(input("Enter the starting minutes: "))
seconds = int(input("Enter the starting seconds: "))
timer_on = True

def display_time(hour_value: int, minute_value: int, second_value: int):
    hour_string = f"{hour_value}" if hour_value > 9 else f"0{hour_value}"
    minute_string = f"{minute_value}" if minute_value > 9 else f"0{minute_value}"
    second_string = f"{second_value}" if second_value > 9 else f"0{second_value}"
    print(f"{hour_string}:{minute_string}:{second_string}")

while timer_on:
    display_time(hour_value=hours, minute_value=minutes, second_value=seconds)

    if hours == 0 and minutes == 0 and seconds == 0:
        print("Timer Stopped!")
        timer_on = False

    elif minutes == 0 and hours > 0:
        hours -= 1
        minutes = 60

    elif seconds == 0:
        minutes = minutes - 1
        seconds = 60

    else:
        seconds = seconds - 1

    sleep(0.5)
