import random
rows = int(input("How many quick picks?"))
random_list = []

for i in range(rows):
    print("")
    random_list = []
    for j in range(6):
        num = random.randrange(1,46)
        if num not in random_list:
            random_list.append(num)
        else:
            j-=1
            random_list.sort()
    for k in random_list:
        print("{:2}".format(k),end=" ")