import random
import secrets
from colorama import init, Fore, Back, Style
import random
init()
print(Fore.GREEN +'''
████████╗░█████╗░██████╗░░█████╗░██╗░░██╗██╗██╗░░██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░░██║██║██║░██╔╝
░░░██║░░░██║░░██║██████╔╝██║░░╚═╝███████║██║█████═╝░
░░░██║░░░██║░░██║██╔══██╗██║░░██╗██╔══██║██║██╔═██╗░
░░░██║░░░╚█████╔╝██║░░██║╚█████╔╝██║░░██║██║██║░╚██╗
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝

Варианты генерации ключей:
1) AAAAA-BBBBB-CCCCC
2) AAAAA-BBBBB-CCCCC-DDDDD-EEEEEE
3) 237ABCDGHJLPRST 23''')

def genera():
    a = random.choice(arr)
    b = random.choice(arr)
    c = random.choice(arr)
    d = random.choice(arr)
    e = random.choice(arr)
    q = a + b + c + d + e
    return (q)

def genera2():
    a = random.choice(arr2)
    b = random.choice(arr2)
    q = a + b
    return (q)
def Type_A_B ():
    Var_a = genera()
    Var_b = genera()
    Var_c = genera()
    Var_qwerr=Var_a + "-" + Var_b + "-" + Var_c
    return(Var_qwerr)
init()
Vibor = int(input(Fore.GREEN +"Введите вариант и нажмите Enter: "))
arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
       "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
arr2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
if Vibor == 1:
    qwe = int(input(Fore.GREEN +"Введите количество ключей: "))
    file = open(str(qwe) + "Keys.txt", "w")
    qwer = 0
    while (qwer < qwe):
        qwer += 1
        file.write(Type_A_B()+"\n")
        print(str(qwer)+" complete")
    input(Fore.YELLOW +"Для завершения нажмите Enter")
elif Vibor == 2:
    qwe = int(input(Fore.GREEN +"Введите количество ключей: "))
    file = open(str(qwe) + "Keys.txt", "w")
    qwer = 0
    while (qwer < qwe):
        qwer += 1
        Var_d = genera()
        Var_e = genera()
        file.write(Type_A_B() + "-" + Var_d + "-" + Var_e + "\n")
        print(str(qwer) + " complete")
    input(Fore.YELLOW +"Для завершения нажмите Enter.")
elif Vibor == 3:
    qwe = int(input(Fore.GREEN +"Введите количество ключей:"))
    file = open(str(qwe) + "Keys.txt", "w")
    qwer = 0
    while (qwer < qwe):
        qwer += 1
        Var_a = genera()
        Var_b = genera()
        Var_c = genera()
        file.write(Var_a + Var_b + Var_c + " " + genera2()+"\n")
        print(str(qwer) + " complete")
    input(Fore.YELLOW +"Для завершения нажмите Enter")
else:
    print(Fore.RED +"Выввели не верное число")
