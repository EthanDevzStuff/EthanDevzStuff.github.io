inv = {}
takenItems = []
actions = []

print("Welcome to the game.\nControls:\nN = North\nW = West\nS = South\nE = East\nTake = Take an item\nSearch = Search the current area if allowed.\nOpen = Break open a door or gate (requires Crowbar)\nSneak = Sneak past something\nSteal = Attempt to steal an item\nShoot = Shoot something\nINV = Check your inventory")

def inventoryHandler(item, action):
    if not action: return
    if action.lower() == "give":
        if not inv.get(item):
            print("\nYou have picked up a " + item + "!")
            inv[item] = 1
        else:
            print("\nYou have gained another " + item + "!")
            inv[item] += 1
        print("You now have " + str(inv[item]) + " " + item + "(s).")
        if item not in takenItems:
            takenItems.append(item)
    elif action.lower() == "drop":
        if item in inv and inv[item] > 0:
            inv[item] -= 1
            print("\nYou dropped 1 " + item + ".")
            if inv[item] == 0:
                del inv[item]
            return True
        else:
            print("\nYou don't have any " + item + " to drop.")
            return None
    elif action.lower() == "check":
        return item in inv

def showInventory():
    print("\nYou look in your inventory:")
    if not inv:
        print("- Nothing")
    else:
        for key, qty in inv.items():
            print("- " + key + " x" + str(qty))

def gateFight():
    print()
    print("You approach a suspicious gate.")
    print("A guard is sitting on a chair, half asleep. A Glock 17 rests on his belt.")
    if "Glock 17" in inv:
        print("You can SHOOT, SNEAK, or go back EAST.")
    else:
        print("You can SNEAK to steal his weapon, or go back EAST.")
    choice = input("What do you do? -> ").upper()
    if choice == "E":
        outsideHospital()
    elif choice == "SNEAK":
        if "Glock 17" in inv:
            print()
            print("You already have the weapon.")
            gateFight()
        else:
            print()
            print("You slowly creep toward the guard...")
            print("Your hand reaches for the Glock...")
            steal = input("STEAL or BACK -> ").upper()
            if steal == "STEAL":
                print()
                print("You yank the Glock 17 from his belt!")
                inventoryHandler("Glock 17", "give")
                print("The guard jolts awake!")
                print("Before he can react, you point the gun at him.")
                print("He freezes.")
                print("YOU WON. Ending: Silent Thief.")
            else:
                print()
                print("You step back quietly.")
                gateFight()
    elif choice == "SHOOT":
        if "Glock 17" not in inv:
            print()
            print("You reach for a gun you do not have.")
            print("The guard wakes up and shoots you.")
            print("GAME OVER.")
        else:
            print()
            print("You fire first.")
            print("The guard collapses instantly.")
            print("You search his body.")
            print("Nothing else of value remains.")
            print("YOU WON. Ending: Guns Blazing.")
    elif choice == "INV":
        showInventory()
        gateFight()
    else:
        print()
        print("Invalid choice.")
        gateFight()

def outsideHospital():
    print("\nYou are outside the abandoned hospital. The air smells of decay and ash.")
    print("North: Hospital reception.")
    print("East: Car park with a dangerous drop.")
    print("South: Thick black smoke rises from a distant fire.")
    print("West: Suspicious gate.")
    choice = input("Use your controls -> ").upper()
    if choice == "N":
        hospitalReception()
    elif choice == "S":
        burntBus()
    elif choice == "E":
        carPark()
    elif choice == "W":
        if not inventoryHandler("Crowbar", "check"):
            print("\nThe gate is locked tight. You need a Crowbar to open it.")
            outsideHospital()
        else:
            if "gate" not in actions:
                print("\nYou use the Crowbar to pry the gate open.")
                actions.append("gate")
            gateFight()
    elif choice == "INV":
        showInventory()
        outsideHospital()
    elif choice == "OPEN":
        if not inventoryHandler("Crowbar", "check"):
            print("\nYou need a Crowbar to break open the gate.")
            outsideHospital()
        elif "gate" in actions:
            print("\nThe gate is already opened. You can go through.")
            gateFight()
        else:
            print("\nYou use the Crowbar to pry the gate open.")
            actions.append("gate")
            gateFight()
    else:
        print("\nInvalid choice.")
        outsideHospital()

def carPark():
    print("\nYou enter the car park. The concrete floor is cracked and unstable.")
    print("You see a gaping hole in the floor. One wrong step could be fatal.")
    print("You can try to carefully move around it, or jump across the cars to the other side.")
    choice = input("Do you try to MOVE carefully or JUMP? -> ").upper()
    if choice == "MOVE":
        print("\nYou tiptoe carefully but the floor collapses beneath you!")
        print("You fall into the darkness below.")
        print("GAME OVER.")
    elif choice == "JUMP":
        if "Crowbar" in inv:
            print("\nYou leap across, using the Crowbar to steady yourself.")
            print("You make it safely across the car park.")
            forestPath()
        else:
            print("\nYou try to jump across but slip and fall into the hole.")
            print("GAME OVER.")
    elif choice == "INV":
        showInventory()
        carPark()
    else:
        print("\nInvalid choice.")
        carPark()

def hospitalReception():
    print("\nYou are in the hospital reception. Dust and broken furniture everywhere.")
    print("East: Cleaner's cupboard.")
    print("South: Main entrance back outside.")
    print("North: Staircase leading to the rooftop.")
    choice = input("Use your controls -> ").upper()
    if choice == "S":
        outsideHospital()
    elif choice == "E":
        cleanerCupboard()
    elif choice == "N":
        rooftop()
    elif choice == "INV":
        showInventory()
        hospitalReception()
    else:
        print("\nInvalid choice.")
        hospitalReception()

def cleanerCupboard():
    print("\nYou are in a dusty cupboard. Cobwebs cover the corners.")
    if "Cleaner's Key" not in inv:
        print("There is a small key hanging on the wall.")
    else:
        print("The hook where the key once hung is now empty.")
    print("West: Back to reception.")
    choice = input("Use your controls -> ").upper()
    if choice == "W":
        hospitalReception()
    elif choice == "TAKE":
        if "Cleaner's Key" in inv:
            print("\nYou already have the key.")
        else:
            inventoryHandler("Cleaner's Key", "give")
        cleanerCupboard()
    elif choice == "INV":
        showInventory()
        cleanerCupboard()
    else:
        print("\nInvalid choice.")
        cleanerCupboard()

def burntBus():
    print("\nYou arrive at the charred remains of a yellow school bus.")
    print("North: Hospital.")
    if "Crowbar" not in inv:
        print("Something glints in the ashes, you can search it.")
    else:
        print("Only faint footprints are left in the ashes.")
    choice = input("Use your controls -> ").upper()
    if choice == "SEARCH":
        if "Crowbar" in inv:
            print("\nYou already have the Crowbar.")
        else:
            inventoryHandler("Crowbar", "give")
        burntBus()
    elif choice == "N":
        outsideHospital()
    elif choice == "INV":
        showInventory()
        burntBus()
    else:
        print("\nInvalid choice.")
        burntBus()

def rooftop():
    print("\nYou reach the rooftop. You can see the city skyline and a distant forest.")
    print("You can jump down to the fire escape (E) or explore the helipad (N).")
    choice = input("Choose direction -> ").upper()
    if choice == "E":
        fireEscape()
    elif choice == "N":
        helipad()
    elif choice == "INV":
        showInventory()
        rooftop()
    else:
        print("\nInvalid choice.")
        rooftop()

def fireEscape():
    print("\nYou descend the fire escape carefully and reach the ground safely.")
    print("Ahead, a forest path leads away from the city.")
    forestPath()

def helipad():
    print("\nYou step onto the helipad. The metal floor creaks under your weight.")
    print("Suddenly, it collapses and you fall several meters.")
    print("GAME OVER.")

def forestPath():
    print("\nYou enter a forest. The smoke from the city fades behind you.")
    print("North: A small abandoned cabin.")
    print("East: A river path.")
    print("West: Back towards the city.")
    choice = input("Choose direction -> ").upper()
    if choice == "N":
        cabin()
    elif choice == "E":
        river()
    elif choice == "W":
        outsideHospital()
    elif choice == "INV":
        showInventory()
        forestPath()
    else:
        print("\nInvalid choice.")
        forestPath()

def cabin():
    print("\nYou find an abandoned cabin. Inside, there are supplies and a map.")
    if "Map" not in inv:
        inventoryHandler("Map", "give")
    print("You can rest here (R) or continue north into unknown forest (N).")
    choice = input("What do you do? -> ").upper()
    if choice == "R":
        print("\nYou rest for a while and regain strength. The map shows a safe route out of the forest.")
        print("YOU SURVIVED. Ending 1: Safe Escape.")
    elif choice == "N":
        print("\nYou venture deeper into the forest and get lost. Night falls, and you cannot find shelter.")
        print("GAME OVER.")
    elif choice == "INV":
        showInventory()
        cabin()
    else:
        print("\nInvalid choice.")
        cabin()

def river():
    print("\nYou follow the river and find a small boat.")
    if "Boat Key" in inv:
        print("You use the key to start the boat and sail downstream to safety.")
        print("YOU SURVIVED. Ending 2: River Escape.")
    else:
        print("The boat is locked. You cannot cross. You must turn back.")
        forestPath()

def secretTunnel():
    print("\nBehind the guard, a dark tunnel leads underground.")
    print("You can follow it (N) or go back outside (S).")
    choice = input("Choose direction -> ").upper()
    if choice == "N":
        print("\nYou follow the tunnel and find an underground shelter stocked with supplies.")
        print("YOU SURVIVED. Ending 3: Hidden Shelter.")
    elif choice == "S":
        outsideHospital()
    elif choice == "INV":
        showInventory()
        secretTunnel()
    else:
        print("\nInvalid choice.")
        secretTunnel()

outsideHospital()