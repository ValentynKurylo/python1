def min(list=[]):
    list.sort()
    return list[0]

def delete(list=[]):
    x = []
    list.sort()
    for i in range(len(list)):
        if i != 0:
            if list[i] == list[i - 1]:
                x.append(list[i - 1])

    for i in range(len(x)):
        list.remove(x[i])
        list.remove(x[i])
    return print(list)

def four(list=[]):
    for i in range(len(list)):
       if i != 0:
           if i % 4 == 0:
               list[i] = 'X'
    return list

def square(side):
    for i in range(side):
        if (i == 0):
          print("*"*side)
        elif(i == side - 1):
          print("*" * side)
        else:
          print("*" + (" "* (side - 2)) + "*")

def table():
    for i in range(1, 10):
        for j in range(1, 10):
            sum = i*j
            print(sum)

def avr(list=[]):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    sum /= len(list)

    print(sum)
    list.sort()
    print(list)
    for i in range(1, len(list) - 1):
        if sum >= list[i - 1] and sum <= list[i+1]:
            print(list[i])


def menu():
    list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(list)
    print(" 1 - min number")
    print(" 2 - delete all some number")
    print(" 3 - change all 4 number on X")
    print(" 4 - Show square")
    print(" 5 - multiplication table")
    print(" 6 - avr")
    n = int(input("Enter number: "))
    if(n == 1):
        m = min(list)
        print(m)
        menu()
    elif(n == 2):
        x = delete(list)
        print(x)
        menu()
    elif(n == 3):
        list3 = four(list)
        print(list3)
    elif(n == 4):
        side = int(input("Side of square"))
        square(side)
    elif n == 5:
        table()
    elif n == 6:
        avr(list)

menu()

