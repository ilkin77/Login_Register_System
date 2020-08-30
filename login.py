from read import *
from write import *
from delete import *
from update import *

def login():


    print("""Menu
    Telebeleri gormek             -> 1
    Telebe elave etmek            -> 2
    Telebe silmek                 -> 3
    Telebe melumatlarini deyismek -> 4
    Ada gore telebe axtarisi      -> 5
        """)

    order = int(input("Choose your number : "))

    try:
        if order == 1:
            reading()
        elif order == 2:
            Writing()
        elif order == 3:
            deleting()
        elif order == 4:
            updating()
        elif order == 5:
            pass
        else:
            print("duzgun reqem yazmadiniz.")
    except:
        print("Xeta bas verdi")