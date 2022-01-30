import time
import random

# Parking Garage Class
class Parking_Garage:
    def __init__(self, tickets_available, parking_spaces, current_ticket):
        self.tickets_available = tickets_available
        self.parking_spaces = parking_spaces
        self.current_ticket = current_ticket
        self.customer_ticket = {"Paid": False}

    def new_car_in_garage(self): # Adds a new car by ticket number in the form of a dictionary at index 0 in list
        new_ticket_num = str(random.randint(0, 500))
        return new_ticket_num

    def pay_for_parking(self): # Paying for parking
        payment = int(input("Thank you for using our parking garage. It is time to pay: "))
        while payment == 5:
            self.customer_ticket["Paid"] = True # Working
            print("Your parking has been paid, have a nice day!")
            break
        
    def take_ticket(self, spaces_available): # checks if there are spaces available in the parking garage
        if len(spaces_available) < 10:
            new_car_dict = dict(Ticket_Number = self.new_car_in_garage())
            time.sleep(1)
            spaces_available.insert(0, new_car_dict)
        else:
            print("Our parking is full at this time. Please try again later")
            time.sleep(3)    
           
    def leave_garage(self): # Leaving Garage
        if self.customer_ticket["Paid"] == True: # If class atribute customer ticket is true
            return "Thank you, have a nice day!" # thank customer for paying
        elif self.customer_ticket["Paid"] == False: # If class attribute customer ticket is false
            payment = int(input("Whoopsies, looks like we need to pay for that there parking ticket: ")) # Start a loop to get customer to pay the proper amount
            while payment != 5:
                second_try_payment = int(input("That wasn't $5. Try again.: "))
                payment = second_try_payment
                if payment == 5:
                    self.customer_ticket["Paid"] = True
                    print("Thank you, have a nice day!")
        self.customer_ticket["Paid"] = False
    
    def ticket_paid(self):
        self.customer_ticket["Paid"] = False
            
            
# Group Responsibilities
# Hamilton wrote first draft of class body
# Shakti designed the functionality of our while loops
# Hamilton imported the time package that loops our main program
# Shakti provided revisions to functionality of class body and its attributes

