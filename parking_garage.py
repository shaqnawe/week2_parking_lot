from week_2_project import Parking_Garage # importing our class
import time # importing time module

time_in_day = 0 # flag for the hour of the day
GARAGE = Parking_Garage(10, 10, 1) # instantiating class Parking_Garage
cars_in_garage = [] # empty list to store our car ticket dicts
time_passed = 15.0 # flag decrementing for the purpose of removing cars from garage

while time_in_day < 24: # while the time in day is not hour 24
    time.sleep(.5) # wait half a second
    time_in_day += 1 # increment the hour of the day
    print(f"It is currently hour {time_in_day} of the day") # print the hour of the day
    inner_flag = 0 # flag used to coerce the pattern of the below while loop
    time_passed -= 7.5
    if time_passed == 0:
        GARAGE.pay_for_parking()
        GARAGE.leave_garage()
        GARAGE.ticket_paid()
        cars_in_garage.pop()
        time_passed = 15
    while inner_flag < 1: # while loop that runs once, then resets at the top of the body, to run again after prior code
        inner_flag += 1 # increment flag so that the while loop stops after 1 iteration
        GARAGE.take_ticket(cars_in_garage) # runs take_ticket attribute
    print(f"Ticket Numbers in garage: {cars_in_garage}") # prints the list of cars in the garage
print("Yippee Kay_A MotherF*****. Merry Christmas") # Merry Christmas