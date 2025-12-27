

number = input("Type a number: ")

try:
    num = float(number)
    
    if num > 0 and num == int(num):
        print(" YES! That's a natural number! ")
    else:
        print("Wrong number..")
except:
    print(" That's not a number!")