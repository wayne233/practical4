def main():
    n = str(input("What is your user's name"))
    print("Hello", n, ",Welcome to Tropical Airlines Ticket Ordering System.")
    total = 0
    getChoice(n)
    getPersonname(n)
    getTypetrip(n)
    choiceDestinationtrip(n)
    choiceTripfare(n)
    choiceTypeseat(n)
    getAge(n)
    total = (total + b + c + d)/e
    print("Calculating fare . . .")
    print("Ticket for:", n,)
    print("return price $", b,)
    print("tripfare $", c,)
    print("typeseat $", d,)
    print("Total price: $", total,)
    print("\n"*2)
    print("Do you want to order again? \n(Y)es \n (N)o")
    checking(n)

# Display menu and let users choice.
def getChoice(n):
    print("Menu: \n,(I)nstructions \n,(O)rder ticket\n,(E)xit")
    menu = str(input(""))
    if menu == "I":
        print("Thank you for choosing Tropical Airlines for your air travel needs. "
              "You will be asked questions regarding what type of ticket you would like to purchase as well as "
              "destination information. We also offer 50% discounted fares for children.")
        menu == getChoice(n)
    elif menu == "O":
        print("Hello",n, ", is this ticket for: \n, (Y)ou  \n, (S)omeone else")
    elif menu == "E":
        print("Thank for using Tropical Airlines.")
        quit()
    else:
        print("Invalid choice.")
        menu == getChoice(n)

# This ticket for who. If for someone, we need to users input the name.
def getPersonname(n):
    personname = str(input(""))
    if personname == "Y":
        print("Is this a return trip (R) or One-Way (O)?")
    elif personname == "S":
        print("Please enter the name of the person travelling.")
        hisname = str(input(""))
        print("Is this a return trip (R) or One-Way (O)?")
    else:
        print("Invalid choice.")
        personname == getPersonname(n)
        return personname


# Is this a return trip ticket or a one-way ticket. This will affect the final price.
def getTypetrip(n):
    typetrip=str(input(""))
    if typetrip == "R":
        print("Please select the destination for your return trip. Fare prices are listed below: \n, (C)airns – $400 "
              "\n, (S)ydney – $575 \n, (P)erth - $700")
    elif typetrip == "O":
        print("Please confirm your choice, One-way (O)")
    else:
        print("Invalid choice.")
        typetrip == getTypetrip(n)
        return typetrip

# The type of destination for your trip.
def choiceDestinationtrip(n):
    destinationtrip = str(input(""))
    global b
    returncost = 0
    b = returncost
    if destinationtrip == "C":
        b = 400
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. "
              "Please note choosing Frugal fare means you will not be offered a seat choice.: \n, (B)usiness - $275 "
              "\n, (E)conomy - $25 \n, (F)rugal - $0")
    elif destinationtrip == "S":
        b = 575
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. "
              "Please note choosing Frugal fare means you will not be offered a seat choice.: \n, (B)usiness - $275 "
              "\n, (E)conomy - $25 \n, (F)rugal - $0")
    elif destinationtrip == "P":
        b = 700
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. "
              "Please note choosing Frugal fare means you will not be offered a seat choice.: \n, (B)usiness - $275 "
              "\n, (E)conomy - $25 \n, (F)rugal - $0")
    elif destinationtrip == "O":
        b = 0
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. "
              "Please note choosing Frugal fare means you will not be offered a seat choice.: \n, (B)usiness - $275 "
              "\n, (E)conomy - $25 \n, (F)rugal - $0")
    else:
        print("Invalid choice.2")
        destinationtrip == choiceDestinationtrip(n)
        return destinationtrip

# The type of fare
def choiceTripfare(n):
    tripfare = str(input(""))
    global c
    destinationcost = 0
    c = destinationcost
    if tripfare == "B":
        c = 275
        print("Please choose the seat type. Choosing the middle seat will deduct 25 from the total fare: "
          "\n, (W)indow $75 \n, (A)isle $50 \n, (M)iddle -$25")
    elif tripfare == "E":
        c = 25
        print("Please choose the seat type. Choosing the middle seat will deduct 25 from the total fare: "
          "\n, (W)indow $75 \n, (A)isle $50 \n, (M)iddle -$25")
    elif tripfare == "F":
        c = 0
        print("Please choose the seat type. Choosing the middle seat will deduct 25 from the total fare: "
          "\n, (W)indow $75 \n, (A)isle $50 \n, (M)iddle -$25")
    else:
        print("Invalid choice.")
        tripfare == choiceTripfare(n)
        return tripfare

# The type of seat
def choiceTypeseat(n):
    typeseat = str(input(""))
    global d
    seatcost=0
    d = seatcost
    if typeseat == "W":
        d =75
        print("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the "
              "child fare.")
    elif typeseat == "A":
        d =50
        print("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the "
              "child fare.")
    elif typeseat == "M":
        d =-25
        print("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the "
              "child fare.")
    else:
        print("Invalid choice.")
        typeseat == choiceTypeseat(n)
        return seatcost

# Input age
def getAge(n):
    age = int(input(""))
    global e
    e = 0
    if age <= 16:
        e = 2
    else:
        e = 1

def checking(n):
    checked = str(input(""))
    if checked == "Y":
        checked == main()
    elif checked == "N":
        exit()
    else:
        print("Invalid choice.")
        checked == checking(n)


main()