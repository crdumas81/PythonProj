# Bob Smith
# a fun fact, about me
from tkinter.tix import Balloon

c1 = "CCCCC"
c2 = "c    "
c3 = "c    "
c4 = "c    "
c5 = "c    "
c6 = "c    "
c7 = "CCCCC"


r1 = "rrrrr"
r2 = "r   r"
r3 = "r   r"
r4 = "rrrrr"
r5 = "r   r"
r6 = "r   r"
r7 = "r   r"

space = "   "

initials = c1 + space + r1 + "\n"
initials += c2 + space + r2 + "\n"
initials += c3 + space + r3 + "\n"
initials += c4 + space + r4 + "\n"
initials += c5 + space + r5 + "\n"
initials += c6 + space + r6 + "\n"
initials += c7 + space + r7 + "\n"

print(initials)

#ordering

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.12

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description + '\n'

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:"+ '\n')
print(customer_one_itemization+ '\n')
print("Customer One Total:" + str(round(customer_one_total, 2)))

# 'Magic 8-Ball'

import random


name = 'Bob'
question = 'some questions... '

answer = ''

random_number = random.randint(1, 8)

if random_number == 1:
    answer = 'Yes - definitely'
elif random_number == 2:
    answer = 'It is decidedly so'
elif random_number == 3:
    answer = 'Without a doubt'
elif random_number == 4:
    answer = 'Reply hazy, try again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
else:
    print('Whoops!')


print(name + "asks " + question)
print('Magic 8-Ball\'s answer: ' + answer + ' using random number:' + str(random_number))

# Shipping

weight = 41.50
ground_cost = 0.00
premium_ground_cost = 125.00
drone_cost = 0.00
# ground shipping

if weight <= 2:
    ground_cost = (weight * 1.50) + 20.00
elif weight >2 and weight <= 6:
    ground_cost = (weight * 3.00) + 20.00
elif weight >6 and weight <= 10:
    ground_cost = (weight * 4.00) + 20.00
else:
    ground_cost = (weight * 4.75) + 20.00

print('Cost to Ship by Ground:' + str(ground_cost))
print('Premium costs are: ' + str(premium_ground_cost))
# drone costs

if weight <= 2:
    drone_cost = (weight * 4.50)
elif weight >2 and weight <= 6:
    drone_cost = (weight * 9.00)
elif weight >6 and weight <= 10:
    drone_cost = (weight * 12.00)
else:
    drone_cost = (weight * 14.25)

print('Cost to Ship by Drone:' + str(drone_cost))

