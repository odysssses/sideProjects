#Just a test code ><
from time import sleep as delay
from os import system
time = 5
try:
    num1 = int(input("Insert a number: "))
    num2 = int(input("Insert another number: "))
    div = num1 / num2
    print(div)
except ValueError as e:
    print(f"Error: {e}")
    print("You can only insert numbers")
except ZeroDivisionError as e:
    print(f"\nError: {e}.")
    print("You can't divide by zero.")
except Exception:
    print("\nSomething went wrong.")
finally:
    for i in range(0,5):
       print(f"Program will close in: {time}")
       delay(2)
       system("cls")
       time-=1
    exit()
