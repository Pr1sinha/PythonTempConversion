#Program name: MyCalc
#Lab no: 2
#Description: Temperature conversion program
#Your name: Juan Rodriguez
#Date: 06-20-2021
title = "Temperature Conversion Application"
userLetter = input("Press letter 'c' to convert centigrade to fahrenheit. Press letter 'f' to convert fahrenheit to centigrade.\n")
while (userLetter != "f" or "c"):
    if userLetter == "f":
     fah = float(input("Enter fahrenheit :"))
     cel = (fah-32)*.55
    elif userLetter == "c":
     cel = float(input("Enter centigrade :"))
     fah = (1.8*cel)+32
    elif userLetter == 'yes':
     print("Thanks for using the Temperature Conversion Application")
     break
    else :
     userLetter = input("You did not enter c or f. Try again.")
    print(title)
    print("\n")
    print('Your centigrade is '+str(cel)+' and your fahrenheit is '+str(fah))
    f = open("temp_conversion.txt", "a")
    print(' Centigrade '+' '+'Fahrenheit\n'
          '------------'+' '+'------------\n'
           +' '+str(cel)+'          '+str(fah)
          , file=f)
    f.close()
    print("\n")
    print("Press 'f' or 'c'  to perform other conversion. 'f' for fahrenheit to centigrade and 'c' for centigrade to fahrenheit \n Press any other letter to try again.\nEnter 'yes' to exit.")
    userLetter = input("Your choice:  ")
