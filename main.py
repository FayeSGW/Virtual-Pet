from creature2 import Creature
import threading, pickle, time, sys

def create():
    name = input("What would you like to call your pet? ")
    gender = input("Is your pet male (M), female (F), or other (O)? ")

    pet = Creature(name, gender)
    return pet

def update(pet):
    while pet.is_alive() == True:
        pet.status_update()
        time.sleep(1800)
    print("Press Enter to play again.")


def age_up(pet):
    while pet.is_alive() == True:
        pet.age_up()
        time.sleep(86400)
    print("Press Enter to play again.")


def interact(pet):
    options = {"Status": f"Check {pet.name2()}'s stats", "Feed": f"Give {pet.name2()} some food", "Bath": f"Give {pet.name2()} a bath", "Exercise": f"Exercise with {pet.name2()}", "Sleep": f"Put {pet.name2()} to bed", "Wake": f"Wake {pet.name2()} up", "Quit": "Quit the programme"}
    for option in options:
        print(f"{option}: {options[option]}")
    choice = input("What would you like to do? \n").title()
    chosen(pet, choice, options)

def chosen(pet, choice, options):
    if pet.is_alive() == False:
        sys.exit()
    if choice in options:
        if choice == "Status":
            print(pet)
            interact(pet)
        elif choice == "Feed":
            pet.feed()
            interact(pet)
        elif choice == "Bath":
            pet.bath()
            interact(pet)
        elif choice == "Exercise":
            pet.exercise()
            interact(pet)
        elif choice == "Sleep":
            pet.sleep()
            interact(pet)
        elif choice == "Wake":
            pet.wake()
            interact(pet)
        elif choice == "Quit":
            print("Ok, Bye!")
    else:
        print("Invalid choice. PLease try again!")
        interact(pet)


def main():

    pet = create()

    aging = threading.Thread(target = age_up, args = (pet,), daemon = True)
    aging.start()

    timer = threading.Thread(target = update, args = (pet,), daemon = True)
    timer.start()

    interaction = threading.Thread(target = interact, args = (pet,))
    interaction.start()



if __name__ == "__main__":
    main()

    


