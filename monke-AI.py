import random 

name = input("what is your monke name? ")
source = input("do you like monke? ")
monke = input("what do you like? ")

if source != "yes":
    print("get out!")
    quit()
if source != "no":
    print("good monke")
if monke != "monke":
    print("worng!")
    quit()

math = input("whats 9 + 10? ")
if math != "21":
    print("you stupid!")
    quit()

if math == "21":
    print("good boy")    



