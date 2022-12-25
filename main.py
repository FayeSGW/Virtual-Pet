from creature2 import Creature
import threading, pickle, time, sys

def create():
    name = input("What would you like to call your pet? ")
    gender = input("Is your pet male (M), female (F), or other (O)? ")

    pet = Creature(name, gender)
    return pet

def update(pet):
    while True:
        pet.status_update()
        time.sleep(1800)


def age_up(pet):
    while pet.is_alive() == True:
        pet.age_up()
        time.sleep(0.1)
    print("Press Enter to play again.")


def interact(pet):
    options = {"status": f"check {pet.name2()}'s stats", "feed": f"give {pet.name2()} some food", "bath": f"give {pet.name2()} a bath", "exercise": f"exercise with {pet.name2()}", "sleep": f"put {pet.name2()} to bed", "wake": f"wake {pet.name2()} up", "quit": "Quit the programme"}
    for option in options:
        print(f"{option}: {options[option]}")
    choice = input("What would you like to do? \n").lower()
    chosen(pet, choice, options)

def chosen(pet, choice, options):
    if pet.is_alive() == False:
        sys.exit()
    if choice in options:
        if choice == "status":
            print(pet)
            interact(pet)
        elif choice == "feed":
            pet.feed()
            interact(pet)
        elif choice == "bath":
            pet.bath()
            interact(pet)
        elif choice == "exercise":
            pet.exercise()
            interact(pet)
        elif choice == "sleep":
            pet.sleep()
            interact(pet)
        elif choice == "wake":
            pet.wake()
            interact(pet)
        elif choice == "quit":
            print("Ok, Bye!")
    else:
        print("Invalid choice. PLease try again!")
        interact(pet)


def main():

    pet = create()

    interaction = threading.Thread(target = interact, args = (pet,))
    interaction.start()
    
    timer = threading.Thread(target = update, args = (pet,), daemon = True)
    timer.start()

    aging = threading.Thread(target = age_up, args = (pet,), daemon = True)
    aging.start()




if __name__ == "__main__":
    main()

    


