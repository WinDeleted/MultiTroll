print("░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄")
print("░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄")
print("░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█")
print("░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█")
print("░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█")
print("█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█")
print("█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█")
print("░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█")
print("░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█")
print("░░░█░░██░░▀█▄▄▄█▄▄█▄████░█")
print("░░░░█░░░▀▀▄░█░░░█░░█░█░██░█")
print("░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█")
print("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█")
print("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█")
print("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█")
print("      MultiTroll V1")
 
import time

def Line1():
    print("This is a program that shows the multiplication table from 1 to 10.")


def Line2():
    n = int (input("Insert the multiplier: "))
    for i in range(1, 11):
        print(n*i)

Line1()
time.sleep(5)
Line2()
