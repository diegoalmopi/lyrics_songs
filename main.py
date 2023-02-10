import beatles
import linkin_park
import don_omar
from os import system
import sys


def menu():
    system("clear")
    song = input("""Select one of the next songs:

                    1. Yesterday - The Beatles
                    2. I want to hold your hand - The Beatles
                    3. Yellow submarine - The Beatles
                    4. In the end - Linkin Park
                    5. Numb - Linkin Park
                    6. Virtual Diva - Don Omar
                    
                    Press e or type exit to finish

                    """)
    return song

def options(option):
    match option:
        case "yesterday" | "1":
            system("clear")
            print("---- Yesterday - The Beatles ----")
            print(beatles.yesterday())
        case "i want to hold your hand" | "2":
            system("clear")
            print("---- I want to hold your hand - The Beatles ----")
            print(beatles.I_want_to_hold_your_hand())
        case "yellow submarine" | "3":
            system("clear")
            print("---- Yellow submarine - The Beatles ----")
            print(beatles.yellow_submarine())
        case "in the end" | "4":
            system("clear")
            print("---- In the end - Linkin Park ----")
            print(linkin_park.in_the_end())
        case "numb" | "5":
            system("clear")
            print("---- Numb - Linkin Park ----")
            print(linkin_park.numb())
        case "virtual diva" | "6":
            system("clear")
            print("---- Virtual Diva - Don Omar ----")
            print(don_omar.virtual_diva())

        case "exit" | "e":
            sys.exit()

        case _:   
            print("I'm sorry, I can't find this song in my database :(") 
def run():
    while(1):
        song = menu()
        options(song)      
        input("Press enter to select another one")

if __name__ == "__main__":
    run()
    
    