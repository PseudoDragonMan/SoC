import random as rd

class Car:
    def __init__(self, state, distance):
        self.state = state
        self.distance = distance

    def move(self, speed):
        if speed == 1 and self.state == 0:
            return 1
        elif speed == 2 and self.state == 0:
            return 2
        elif speed == 1 and self.state == 1:
            return 3
        elif speed == 2 and self.state == 1:
            return 4

def print_state(state):
    if state == 0:
        print('cool')
    elif state == 1:
        print('warm')

cond = 0
car = Car(0, 0)

counter = int(input("Enter the required number of iterations of the game: "))
for i in range(counter):
    speed = int(input("Enter 1 for slow and 2 for fast: "))
    process = car.move(speed)
    if process == 1:
        car.state = 0
        print('cool')
        car.distance += 1
    elif process == 2:
        car.state = rd.randint(0,1)
        print_state(car.state)
        car.distance += 2
    elif process == 3:
        car.state = 0
        car.distance += 0.5
        print_state(car.state)
    elif process == 4:
        print('overheated')
        cond = 1
        break
if cond==0:
    if car.distance < 20:
        print('halted midway')
    else:
        print('reached')