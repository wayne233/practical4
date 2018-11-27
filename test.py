def main():
    n = str(input("What is your user's name"))
    print("Hello",n, ",Welcome to Tropical Airlines Ticket Ordering System.")
    total=0
    getTypetrip(n)
    total = total + a
    print(total)
    print("asd")

def getTypetrip(n):
    typetrip=str(input(""))
    global a
    classcost=0
    a = classcost
    if typetrip == "R":
        a=10
        print("Please select the destination for your return trip. Fare prices are listed below: \n, (C)airns – $400 "
              "\n, (S)ydney – $57 \n, (P)erth - $700")
    elif typetrip == "O":
        a=20
        print("Please select the destination for your return trip. Fare prices are listed below: \n, (C)airns – $400 "
              "\n, (S)ydney – $57 \n, (P)erth - $700")
    else:
        print("Invalid choice.")
        return classcost

main()