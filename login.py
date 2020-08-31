from read import *
from write import *
from delete import *
from update import *

# continue or break program
def isContinue():
    yesOrNo = input("Do you want to continue? yes / no : ")
    if yesOrNo == "yes":
        login()
    else:
        print("Byeee...")

def login():

    print("""Menu
    Telebeleri gormek             -> 1
    Telebe elave etmek            -> 2
    Telebe silmek                 -> 3
    Telebe melumatlarini deyismek -> 4
    Ada gore telebe axtarisi      -> 5
        """)

    order = input("Choose your number : ")

    try:
        if order == "1":
            reading()
            isContinue()
        elif order == "2":
            Writing()
            isContinue()
        elif order == "3":
            deleting()
            isContinue()
        elif order == "4":
            updating()
            isContinue()
        elif order == "5":
            pass
        else:
            print("duzgun reqem yazmadiniz.")
    except:
        print("Xeta bas verdi")