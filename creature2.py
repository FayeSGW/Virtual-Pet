class Creature:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
        self._age = -1
        self._health = 10
        self._hunger = 10
        self._cleanliness = 10
        self._fitness = 10
        self._toilet = 0
        self._alive = True
        self._tiredness = 0
        self._awake = True

    def him_her(self):
        if self._gender.lower() == "male" or self._gender.lower() == "m":
            return "him"
        elif self._gender.lower() == "female" or self._gender.lower() == "f":
            return "her"
        else:
            return "them"
    
    def he_she(self):
        if self._gender.lower() == "male" or self._gender.lower() == "m":
            return "he"
        elif self._gender.lower() == "female" or self._gender.lower() == "f":
            return "she"
        else:
            return "they"

    def name2(self):
        return self._name

    def status_update(self):
        self.tiredness_update()
        self.hunger_update()
        self.cleanliness_update()
        self.fitness_update()
        self.toilet_update()
        self.old_age()

    def age_up(self):
        self._age += 1
        self.age_message()
        self.old_age()

    def age_message(self):
        print(f"{self._name} is {self._age} days old!")

    def old_age(self):
        if self._age == 10:
            self._alive = False
            print(f"{self._name} has died of old age! RIP.")

    
    def is_alive(self):
        return self._alive

    def feed(self):
        if self._hunger <= 7:
            self._hunger += 3
            message = f"{self._name} enjoyed the food!"
        else:
            self._hunger = 10
            self._health -= 1
            message = f"{self._name} is too full!"
        print(message)

    def hunger_update(self):
        if self._hunger != 0:
            self._hunger -=1
        self.hunger_message()

    def hunger_message(self):
        if self._hunger == 0:
            self._health -= 1
            print(f"{self._name} is starving! Please feed {self.him_her()} soon or {self.he_she()} will lose health!")
        elif self._hunger <= 2:
            print(f"{self._name} is very hungry!")
        elif self._hunger <= 5:
            print(f"{self._name} is hungry!")

    def cleanliness_update(self):
        if self._cleanliness != 0:
            self._cleanliness -= 1
        self.cleanliness_message()
    
    def bath(self):
        self._cleanliness = 10
        print(f"{self._name} is nice and clean!")

    def cleanliness_message(self):
        if self._cleanliness < 1:
            self._health -= 1
            print(f"{self._name} is filthy! Please give {self.he_she()} a bath soon or {self.him_her()} will lose health!")
        elif self._cleanliness < 4:
           print(f"{self._name} would like a bath!")
        

    def fitness_update(self):
        if self._fitness != 0:
            self._fitness -= 1
        self.fitness_message()

    def exercise(self):
        if self._fitness <= 5:
            self._fitness += 5
        else:
            self._fitness = 10
            print(f"{self._name} is tired! No more exercise please.")
    
    def fitness_message(self):
        if self._fitness < 4:
            print(f"{self._name} would like to do some exercise!")


    def sleep(self):
        self._awake = False
        if self._tiredness == 0:
            print(f"{self._name} is not tired!")
            self.wake()
        else:
            print(f"{self._name} has fallen asleep!")
    
    def wake(self):
        self._awake = True
        print(f"{self._name} has woken up!")

    def tired_message(self):
        if self._tiredness == 10:
            self.sleep()
        elif self._tiredness >= 8:
            print(f"{self._name} is tired! Please put {self.him_her()} to bed soon!")

    def tiredness_update(self):
        if self._awake == True:
            self._tiredness += 1
            self.tired_message()
        else:
            self._tiredness -= 1
            if self._tiredness == 0:
                self.wake()
        
    def toilet_update(self):
        self._toilet += 1
        self.toilet_message()

    def toilet_message(self):
        if self._toilet == 5:
            print(f"{self._name} has pooped!")
            self._toilet = 0

    def __str__(self):
        return f"Name: {self._name} \nAge: {self._age} days \nHealth: {self._health} \nHunger: {self._hunger} \nCleanliness: {self._cleanliness} \nFitness: {self._fitness} \nToilet: {self._toilet} \n Tiredness: {self._tiredness}"



