import json 
print("-------WELCOME TO UBER APP-----------")
import random
name = input("-------enter the  your name------------= ")
print("welcome to my uber app",name)
rider=["kappu","somi","ravi","vishal","rishabh"]
def booking():
    limit = int(input(" \U0001F61B how much ride we have to do for you \U0001F61B	= "))
    index = 1
    total = 0
    dict = {}
    while index <= limit:
        distance = int(input("how much km...you want to go = "))
        place = input("enter the any place..")
        print("*******")
        driver = random.choice(rider)
        print(driver ,"driver is avalable")
        print("******")
        if driver in rider:
            print("you choice",driver,"driver for go to",place)
            print("******")
            money = distance*50
            total += money
            print(index,"rider money =",money)
            print("*********")
        else:
            print("\U0001F614 driver is not avalable")
            print("*******")
        print(limit," \U0001F7E3 ride your total amount =",total)
        print("*******")
        dict[driver] = total
        index = index + 1
    print(dict," \U0001F696 this is all ride data")
    print("*******")
    i = 0
    max = 0
    for key in dict:
        if dict[key]>max:
            max = dict[key]
        with open("main.json","w+") as file:
            json.dump(dict,file)
    print(key," \U0001F607 this driver is earn more money",max)
    print("*******")
def cancel():
    print("\U0001F499 thanks for visit my Rider sharing app and and you cancel the safely.\U0001F499")
    print("*******")
def main():
    option = int(input("\n1).book \n2).cancle \n.\U0001F635.."))
    if option == 1:
        booking()
        print(" \U0001F636 THANKS VISIT FOR MY UBER APP \U0001F636")
        print("*******")
    else:
        cancel()
main()
def play_again():
    while True:
        again = input("If You Want To book Again  Press yes or no = ")
        if again == "yes":
            main()
        else:
            break
play_again()