
select=input("is this temperature in Celcius or Fahrenheit(C/F):")
temperature=float(input("Enter the temperature:"))

if select == "C":
    Fahrenheit=round((9 * temperature) / 5+32, 1)
    print("The temperature in Fahrenheit =",Fahrenheit,"°F")
elif select == "F":
    Celcius=round((temperature - 32) * 5/9, 1)
    print("The temperature in Celcius is =",Celcius,"°C")  
else:
    print("{select} is an invalid")
    