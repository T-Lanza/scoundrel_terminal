from deck import Deck
from deck import Card
import os

scoundrel = Deck()
deck = scoundrel.deck
weapon = []

os.system('clear')
health = 20

print("")
print(f"==========================================")
print(f"          Scoundrel")
print(f"==========================================")

print("")

check = str(input("Press 'Enter' to Begin"))
active_cards = []

while health > 0 and len(deck) > 0:
    os.system('clear')
    if len(active_cards) == 0:
        for i in range(4):
            active_cards.append(deck[i])  
        del deck[0:4]
    else: 
        for i in range(3):
            active_cards.append(deck[i])
        del deck[0:3]

    while len(active_cards) > 1 and health > 0 and len(deck) > 0:
        os.system('clear')
        print("")
        print(f"Remaining Cards: {len(deck)}")
        print("")
        print(f"==========================================")
        print(f"          Scoundrel       HP: {health}")
        print(f"==========================================")
        if len(weapon) == 0:
            print(f"    Weapon: None")
            print(f"==========================================")

        if len(weapon) == 1:
            diamond = weapon[0]
            print(f"    Weapon: {diamond.value}")
            print(f"==========================================")

        if len(weapon) > 1:
            diamond = weapon[0]
            handicap = weapon[-1]
            print(f"    Weapon: {diamond.value}, Max Attack: {handicap.value}")
            print(f"==========================================")

        print("")
        counter = 1
        for card in active_cards:
            print(f"{counter}. {card}")
            counter += 1

        print("")
        print(f"==========================================")
        print("")
        print("Pick your Option: ")
        print("")
        print("A: Take / Trade a Weapon")
        print("B: Use a Health Potion")
        print("C: Barefist attack a Monster")
        print("D: Fight a Monster with your weapon")
        print("E: Run from Room")
        print("")
        print(f"==========================================")
        print("")

        selection = str(input("> Enter here: "))

        if selection.lower() == "a":
            print("")
            choice = int(input("> Enter Weapon choice:  "))
            weapon = []
            weapon.append(active_cards[choice - 1])
            del active_cards[choice - 1]

        if selection.lower() == "b":
            print("")
            choice = int(input("> Enter Potion Choice:  "))
            potion_choice = active_cards[choice - 1]
            strength = potion_choice.worth
            health += strength
            if health > 20:
                health = 20
            del active_cards[choice - 1]

        if selection.lower() == "c":
            print("")
            choice = int(input("> Enter Monster Choice:  "))
            monster_choice = active_cards[choice - 1]
            print(f"You took {monster_choice.value} points of damage")
            monster_damage = monster_choice.worth
            health -= monster_damage
            del active_cards[choice - 1]

        if selection.lower() == "d":
            print("")
            choice = int(input("> Enter Monster Choice:  "))
            monster_choice = active_cards[choice - 1]
            held_weapon = weapon[0]
            weapon_strength = held_weapon.worth
            monster_strength = monster_choice.worth
            weapon.append(monster_choice)
            if monster_strength > weapon_strength:
                monster_damage = monster_strength - weapon_strength
                health -= monster_damage
            if weapon_strength > monster_strength:
                continue
            del active_cards[choice - 1]

        if selection.lower() == "e":
            for card in active_cards:
                deck.append(card)
            del active_cards[0:4]    

if health <= 0:
    os.system('clear')
    print("")
    length = len(deck)
    print(f"Remaining Cards: {length}")
    print("")
    print(f"==========================================")
    print(f"   THE SCOUNDREL DIED -- GAME OVER")
    print(f"==========================================")
    print("")

if len(deck) == 0:
    os.system('clear')
    print("")
    length = len(deck)
    print(f"Remaining Cards: {length}")
    print("")
    print(f"==========================================")
    print(f"CONGRATULATIONS!! YOU CLEARED THE DUNGEON!")
    print(f"==========================================")
    print("")