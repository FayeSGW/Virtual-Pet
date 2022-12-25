from creature2 import Creature
import threading, pickle

def create():
    name = input("What would you like to call your pet? ")
    gender = input("Is your pet male (M), female (F), or other (O)? ")

    pet = Creature(name, gender)
    return pet

def update(pet):
    pet.status_update()

def age_up(pet):
    pet.age_up()

def interact(pet):
    options = {"status": f"check {pet.name2()}'s stats", "feed": f"give {pet.name2()} some food", "bath": f"give {pet.name2()} a bath", "exercise": f"exercise with {pet.name2()}", "sleep": f"put {pet.name2()} to bed", "wake": f"wake {pet.name2()} up"}
    for option in options:
        print(f"{option}: {options[option]}")
    choice = input("What would you like to do? ").lower()
    chosen(pet, choice, options)

def chosen(pet, choice, options):
    if choice in options:
        if choice == "status":
            print(pet)
        elif choice == "feed":
            pet.feed()
        elif choice == "bath":
            pet.bath()
        elif choice == "exercise":
            pet.exercse()
        elif choice == "sleep":
            pet.sleep()
        elif choice == "wake":
            pet.wake()
        else:
            print("Invalid choice. PLease try again!")
            interact(pet)

def main():
    pet = create()


    i = 0
    for i in range(5):
        interact(pet)
        i+= 1

if __name__ == "__main__":
    main()

    


