import random
import time

random_number = random.randint(1000, 200000)

localtime = time.asctime(time.localtime(time.time()))




registerUsers = {
    'Seyi':'passwordSeyi',
    'Mike':'passwordMike',
    'Love':'passwordLove'
}


def choices():
    print("Welcome, Please choose what you would like to do.")
    choice = int(input(" To register Type 1 and to login Type 2 \n"))
    if choice == 1:
        print("You have already registered")
    elif choice == 2:
        return login()
    else:
        Print("Please make the right choice, or excuse us")



def login():
    #login function here
            name = input("Enter your name \n")
            password = input("Enter your password \n")
            if(name in registerUsers and password == registerUsers[name]):
                  print(localtime)

                  print("Welcome " + name)


                  
                  print("This is your designated account number: ")
                  print(random_number)
                  bankingOptions()
            else:
                print("Password or Username Incorrect. Please try again")
                return False


def bankingOptions():
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Log out')

    selectedOption = int(input('Please select an option:'))

    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        withdraw = int(input("Enter how much, you would like to withdraw \n"))
        if withdraw < 20000:
            print('Take your cash')
        else:
            print("For easy withdrawal, please withdraw cash less than 20,000 Naira")

    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
        deposit = int(input('How much would you like to deposit? \n'))
        if deposit:
            print(deposit)

    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
        complaints = input('What issue would you like to report? \n')
        if complaints:
            print('Thank you for contacting us')
     
    elif(selectedOption == 4):
        exit()

    else:
        print('Invalid option selected, please try again')

    

#if (name in allowedUsers):
    #password = input("Your password? \n")
    #userId = allowedUsers.index(name)

    #if(password == allowedPassword[userId]):

     #   print('Welcome %s' % name)
      #  bankingOptions()

        
   # else:
    #    print('Password incorrect, please try again')

#else:
  #  print('Name not found, please try again')



choices()



        