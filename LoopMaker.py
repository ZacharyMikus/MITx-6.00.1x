"""
  __________________________________
/ This is a python script written by \
\ Zachary W. Mikus on dd-mm-yyyy.   /
  ----------------------------------
         \    ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                ||     ||
"""

def loopProg():

    firstChar = input("Which char to print first? \n")
    printTimes = int(input("How many times? \n"))
    secondChar = input("Second character? \n")

    print("\n\n\n")

    for i in range(printTimes):
        print(firstChar)

    print(secondChar)

loopProg()
