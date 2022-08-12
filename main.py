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
    with open('result.txt', 'w') as f:
        f.write('')
        f.close()
    n = int (input("Insert the multiplier: "))
    for i in range(1, 11):
            print(n*i)
            with open('result.txt', 'a') as f:
                f.write(str (n*i))
                f.write('\n')
                f.close()


Line1()
time.sleep(2)
Line2()
 
