'''
lab1.def
mohamad
9/5/2018
'''
def alarm_clock():
    current_time_string = input("what is the current time")
    waiting_time_string = input("how many hours do we wait")

    current_time_int = int(current_time_string)
    waiting_time_int = int(waiting_time_string)

    hours = current_time_int + waiting_time_int

    timeofday = hours % 24

    print(timeofday)
