from login import signIn, signUp
from userFunction import arsiparis

while True:
    menu1 = input()
    if menu1 == "1":
        signUp()
    elif menu1 == "2":
        signIn(arsiparis)
    else:
        break