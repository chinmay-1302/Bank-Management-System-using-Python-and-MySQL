import time
import random
import mysql.connector as middleboi

class Account :
    accNo = 0
    name = ''
    deposit=0
    address = ''

    def createAccount(self):
        self.accNo= random.randint(1,1000)*27937
        print("Please fill up the required fields -")
        self.name = input("\nEnter your Name : ")
        self.address = input("List your Address : ")
        self.deposit = int(input("What is your Initial Deposit Amount (in INR) ? : "))
        print("\nYour system generated Account Number is:", self.accNo)
        print("\nPlease wait while we generate your Account Certificate...")
        time.sleep(5)
        print("\n******************************************************************")
        print("***           YOUR ACCOUNT IS REGISTERED IN THE NAME OF")
        print("***                      ",self.name)
        print("***      Your Account Number is :", self.accNo)
        print("***      Listed Address is :", self.address)
        print("***      Account Balance :", self.deposit,"INR")
        print("********************************************************************")
        print("\n               HAPPY BANKING WITH US!")
        print("\n(REMEMBER your Account Number as it is a VERY important Security feature)")
        print("\nPlease wait while we take you back to the Homescreen...")
        Executor.execute("INSERT INTO accinfo(AccountNo, Name, Address, Balance) VALUES({},'{}','{}',{})".format(self.accNo, self.name, self.address, self.deposit))
        accountantMan.commit()
        Executor.execute("SELECT * FROM accinfo")
        data=Executor.fetchall()
        for row in data:
            print(row)
        time.sleep(17)

def intro():
    print("\n\t\t*********************************************************************************")
    print("\t\t**  W E L C O M E   T O   T H E   Chinmay   B A N K  **")
    print("\t\t*********************************************************************************")
    print("\n\n")
    print("Please wait while our system is loading.....")
    print("(It is advised to run this program on Full Screen mode)")
    time.sleep(8)

def writeAccount():
    account = Account()
    account.createAccount()


def depositAndWithdraw(num1,num2):
    Executor.execute("SELECT Balance FROM accinfo WHERE AccountNo={}".format(num1))
    data=Executor.fetchone()
    balance=0
    for i in data:
        balance=i
    if num2 == 1 :
        print("DEPOSIT SCREEN\n")
        print("Your current Account balance is :",balance,"INR")
        amount = int(input("Enter the amount to be deposited to your Account : "))
        if amount >= 0 :
            balance = balance+amount
            print("\nYour new Account balance is :",balance,"INR")
        else :
            print("\nYou are supposed to enter your deposit amount as a POSITIVE integer...")
    elif num2 == 2 :
        print("WITHDRAW SCREEN\n")
        print("Your current Account balance is :",balance,"INR")
        amount = int(input("Enter the amount to be withdrawn from your account : "))
        if amount <= balance :
            if amount >= 0:
                balance = balance-amount
                print("\nYour new Account balance is :",balance,"INR")
            else:
                print("\nYou are supposed to enter your withdraw amount as a POSITIVE integer...")

        else :
            print("\nThis task cannot be executed because you have insufficient balance")
    print("\nTaking you back to the Selection screen...")
    Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(balance,num1))
    accountantMan.commit()
    time.sleep(8)


def modifyAccount(num):
    balance=None
    name=None
    address=None
    Executor.execute("SELECT Balance FROM accinfo WHERE AccountNo={}".format(num))
    data=Executor.fetchone()
    for i in data:
        balance=i
    Executor.execute("SELECT Name FROM accinfo WHERE AccountNo={}".format(num))
    data=Executor.fetchone()
    for i in data:
        name=i
    Executor.execute("SELECT Address FROM accinfo WHERE AccountNo={}".format(num))
    data=Executor.fetchone()
    for i in data:
        address=i
    print("ACCOUNT DETAILS SCREEN\n")
    print("This is your current Account Certificate")
    print("It contains all your given details...\n")
    print("\n******************************************************************")
    print("***           YOUR ACCOUNT IS REGISTERED IN THE NAME OF")
    print("***                      ",name)
    print("***      Your Account Number is :", num)
    print("***      Listed Address is :", address)
    print("***      Account Balance :", balance,"INR")
    print("********************************************************************")
    print("\nWould you like to modify your current Account details?")
    print("1) Yes       2)No")
    answer = input()
    if answer == '1':
        print("Please update the required fields -")
        print("\nEnter your new Name :")
        newName = input()
        print("List your Address :")
        listedAddress = input()
        print("\nThis is your updated Account Certificate...")
        print("\n******************************************************************")
        print("***           YOUR ACCOUNT IS REGISTERED IN THE NAME OF")
        print("***                      ",newName)
        print("***      Your Account Number is :", num)
        print("***      Listed Address is :", listedAddress)
        print("***      Account Balance :", balance,"INR")
        print("********************************************************************")
        Executor.execute("UPDATE accinfo SET Name='{}', Address='{}' WHERE AccountNo={}".format(newName,listedAddress,num))
        accountantMan.commit()
        name=newName
    elif answer == '2':
        print("OK")
        print("No changes have been made in your Account")
    else:
        print("\nPlease select either 1 or 2 only")
    print("Taking you back to the Selection screen...")
    time.sleep(8)

def transferFunds(num1):
    balance1=None
    Executor.execute("SELECT Balance FROM accinfo WHERE AccountNo={}".format(num1))
    data=Executor.fetchone()
    for i in data:
        balance1=i
    print("TRANSFER FUNDS SCREEN")
    num2=int(input("Enter the Account number of the Account that you want to transfer money to :"))
    name2=input("Enter the name of the holder of that Account :")
    balance2=None
    Executor.execute("SELECT Balance FROM accinfo WHERE AccountNo={} AND Name='{}'".format(num2,name2))
    data=Executor.fetchone()
    if data != None:
        for i in data:
            balance2=i
        print("\n************************************************************")
        transfer=float(input("Enter the amount to be transferred from your Account :"))
        balance1=balance1-transfer
        balance2=balance2+transfer
        print("\n************************************************************")
        print("TRANSFER SUCCESSFUL")
        print("\nYour current Account balance is :",balance1,"INR")
        Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(balance1,num1))
        Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(balance2,num2))
        accountantMan.commit()
        print("Taking you back to the Selection screen...")
    else:
        print("\n************************************************************")
        print("The Account Number and Name specified do not exist in our Databases")
        print("TIP: Enter the EXACT Account Number of that Account OR Enter the EXACT Name of the holder of that Account")
        print("Try again")
    time.sleep(5)


def currConvertMenu(num):
    balance=None
    Executor.execute("SELECT Balance FROM accinfo WHERE AccountNo={}".format(num))
    data=Executor.fetchone()
    for i in data:
        balance=i
    print("FOREIGN EXCHANGE SCREEN")
    print("\nSelect the currency you would like to convert your INR into : ")
    print("1) US Dollars (USD)")
    print("2) Great Britain Pounds (GBP)")
    print("3) Hong Kong Dollars (HKD)")
    print("4) Swiss Francs (CHF)")
    print("5) Australian Dollars (AUD)")
    print("6) Euros (EUR)")
    print("7) UAE Dirham (AED)")
    print("8) Go back to the Selection Screen")
    ans = input()
    if ans == '1':
        print("\n1 INR = 0.014 USD")
        print("1 USD = 72.91 INR")
        print("\nHow many INR would you like to convert to USD?")
        con = float(input())
        print("You will get", con*0.014, "USD")
        remainingBalance = float(balance)-con
        print("You will be left with", remainingBalance,"INR")
        print("\nWould you like to proceed?")
        print("1)Yes      2)No")
        proceed = input()
        if proceed == '1':
            Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(remainingBalance,num))
            accountantMan.commit()
            print("\nYou have received :", con*0.014, "USD")
            print(con,"INR have been withdrawn from your Account in the form of", con*0.014, "USD")
            print("\nYour current Account balance :", remainingBalance, "INR")
        elif proceed == '2':
            print("\nYou have cancelled the transfer and no amount has been deducted from your account")
            print("Your current Account balance :", balance,"INR")
        else:
            print("\nInvalid Input")
    elif ans == '2':
        print("\n1 INR = 0.010 GBP")
        print("1 GBP = 99.97 INR")
        print("\nHow many INR would you like to convert to GBP?")
        con = float(input())
        print("You will get", con*0.010, "GBP")
        remainingBalance = float(balance)-con
        print("You will be left with", remainingBalance,"INR")
        print("\nWould you like to proceed?")
        print("1)Yes      2)No")
        proceed = input()
        if proceed == '1':
            Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(remainingBalance,num))
            accountantMan.commit()
            print("\nYou have received :", con*0.010, "GBP")
            print(con,"INR have been withdrawn from your Account in the form of", con*0.010, "GBP")
            print("\nYour current Account balance :", remainingBalance,"INR")
        elif proceed == '2':
            print("\nYou have cancelled the transfer and no amount has been deducted from your account")
            print("Your current Account balance :", balance,"INR")
        else:
            print("\nInvalid Input")
    elif ans == '3':
        print("\n1 INR = 0.11 HKD")
        print("1 HKD = 9.40 INR")
        print("\nHow many INR would you like to convert to HKD?")
        con = float(input())
        print("You will get", con*0.11, "HKD")
        remainingBalance = float(balance)-con
        print("You will be left with", remainingBalance,"INR")
        print("\nWould you like to proceed?")
        print("1)Yes      2)No")
        proceed = input()
        if proceed == '1':
            Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(remainingBalance,num))
            accountantMan.commit()
            print("\nYou have received :", con*0.11, "HKD")
            print(con,"INR have been withdrawn from your Account in the form of", con*0.11, "HKD")
            print("\nYour current Account balance :", remainingBalance,"INR")
        elif proceed == '2':
            print("\nYou have cancelled the transfer and no amount has been deducted from your account")
            print("Your current Account balance :", balance,"INR")
        else:
            print("\nInvalid Input")
    elif ans == '4':
        print("\n1 INR = 0.012 CHF")
        print("1 CHF = 81.87 INR")
        print("\nHow many INR would you like to convert to CHF?")
        con = float(input())
        print("You will get", con*0.012, "CHF")
        remainingBalance = float(balance)-con
        print("You will be left with", remainingBalance, "INR")
        print("\nWould you like to proceed?")
        print("1)Yes      2)No")
        proceed = input()
        if proceed == '1':
            Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(remainingBalance,num))
            accountantMan.commit()
            print("\nYou have received :", con*0.012, "CHF")
            print(con,"INR have been withdrawn from your Account in the form of", con*0.012, "CHF")
            print("\nYour current Account balance :", remainingBalance,"INR")
        elif proceed == '2':
            print("\nYou have cancelled the transfer and no amount has been deducted from your account")
            print("Your current Account balance :", balance,"INR")
        else:
            print("\nInvalid Input")
    elif ans == '5':
        print("\n1 INR = 0.018 AUD")
        print("1 AUD = 55.72 INR")
        print("\nHow many INR would you like to convert to AUD?")
        con = float(input())
        print("You will get", con*0.018, "AUD")
        remainingBalance = float(balance)-con
        print("You will be left with", remainingBalance, "INR")
        print("\nWould you like to proceed?")
        print("1)Yes      2)No")
        proceed = input()
        if proceed == '1':
            Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(remainingBalance,num))
            accountantMan.commit()
            print("\nYou have received :", con*0.018, "AUD")
            print(con,"INR have been withdrawn from your Account in the form of", con*0.018, "AUD")
            print("\nYour current Account balance :", remainingBalance, "INR")
        elif proceed == '2':
            print("\nYou have cancelled the transfer and no amount has been deducted from your account")
            print("Your current Account balance :", balance,"INR")
        else:
            print("\nInvalid Input")
    elif ans == '6':
        print("\n1 INR = 0.011 EUR")
        print("1 EUR = 88.49 INR")
        print("\nHow many INR would you like to convert to EUR?")
        con = float(input())
        print("You will get", con*0.011, "EUR")
        remainingBalance = float(balance)-con
        print("You will be left with", remainingBalance, "INR")
        print("\nWould you like to proceed?")
        print("1)Yes      2)No")
        proceed = input()
        if proceed == '1':
            Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(remainingBalance,num))
            accountantMan.commit()
            print("\nYou have received :", con*0.011, "EUR")
            print(con,"INR have been withdrawn from your Account in the form of", con*0.011, "EUR")
            print("\nYour current Account balance :", remainingBalance,"INR")
        elif proceed == '2':
            print("\nYou have cancelled the transfer and no amount has been deducted from your account")
            print("Your current Account balance :", balance,"INR")
        else:
            print("\nInvalid Input")
    elif ans == '7':
        print("\n1 INR = 0.050 AED")
        print("1 AED = 19.85 INR")
        print("\nHow many INR would you like to convert to AED?")
        con = float(input())
        print("You will get", con*0.050, "AED")
        remainingBalance = float(balance)-con
        print("You will be left with", remainingBalance, "INR")
        print("\nWould you like to proceed?")
        print("1)Yes      2)No")
        proceed = input()
        if proceed == '1':
            Executor.execute("UPDATE accinfo SET Balance={} WHERE AccountNo={}".format(remainingBalance,num))
            accountantMan.commit()
            print("\nYou have received :", con*0.050, "AED")
            print(con,"INR have been withdrawn from your Account in the form of", con*0.050, "AED")
            print("\nYour current Account balance :", remainingBalance, "INR")
        elif proceed == '2':
            print("\nYou have cancelled the transfer and no amount has been deducted from your account")
            print("Your current Account balance :", balance, "INR")
        else:
            print("\nInvalid Input")
    elif ans == '8':
        print("\nReturning to the Selection Screen...")
    else :
        print("\nWHY")
        print("Enter a number between 1 and 8 (Including 1 and 8)")
    time.sleep(7)


def selectionScreen(num, accName):
    Executor.execute("SELECT AccountNo FROM accinfo WHERE AccountNo={} AND Name='{}'".format(num,accName))
    data=Executor.fetchone()
    numfetched=0
    if data != None :
        for i in data:
            numfetched=i
            print("SUCCESSFULLY LOGGED IN")

    while numfetched != 0:
        print("\nSELECTION SCREEN")
        print("\nWhat would you like to do ?\n")
        print("1) DEPOSIT MONEY")
        print("2) WITHDRAW MONEY")
        print("3) VIEW OR MODIFY ACCOUNT DETAILS")
        print("4) FOREIGN EXCHANGE")
        print("5) TRANSFER FUNDS")
        print("6) LOG OUT")
        decision = input()
        if decision == '1':
            num = numfetched
            print("\n************************************************************")
            depositAndWithdraw(num, 1)
            print("\n************************************************************")
        elif decision == '2':
            num = numfetched
            print("\n************************************************************")
            depositAndWithdraw(num, 2)
            print("\n************************************************************")
        elif decision == '3':
            num = numfetched
            print("\n************************************************************")
            modifyAccount(num)
            print("\n************************************************************")
        elif decision == '4':
            num = numfetched
            print("\n************************************************************")
            currConvertMenu(num)
            print("\n************************************************************")
        elif decision == '5':
            num=numfetched
            print("\n************************************************************")
            transferFunds(num)
            print("\n************************************************************")
        elif decision == '6':
            print("SUCCESSFULLY LOGGED OUT")
            print("\tThank you for using our Bank Management System")
            time.sleep(3)
            break
        else :
            print("Please enter a digit between 1 and 6 including them both")
            time.sleep(6)
    else:
        print("Incorrect Account Number OR Name")
        print("TIP: Enter the EXACT Account Number that was given to you OR Enter the EXACT Name that you had entered previously")
        print("Try again")
        time.sleep(5)



# start of the program
creatorMan=middleboi.connect(host="localhost",user="root",passwd="booga")
Creator=creatorMan.cursor()
Creator.execute("CREATE DATABASE IF NOT EXISTS teab_db")
accountantMan=middleboi.connect(host="localhost",user="root",passwd="booga",database="teab_db")
Executor=accountantMan.cursor()
Executor.execute("CREATE TABLE IF NOT EXISTS accinfo (AccountNo VARCHAR(8) , Name VARCHAR(255), Address VARCHAR(255), Balance BIGINT)")
ch=''
num=0
intro()

while ch != 8:
    print("\n************************************************************")
    print("\tPlease select one of the following :")
    print("\t1) OPEN A NEW ACCOUNT")
    print("\t2) LOG IN (OPEN AN EXISTING ACCOUNT)")
    print("\t3) EXIT")
    print("\tSelect Your Option (1-4) ")
    ch = input()

    if ch == '1':
        print("\n************************************************************")
        writeAccount()
        print("\n************************************************************")
    elif ch =='2':
        print("\n************************************************************")
        num = int(input("\tEnter your Account Number :"))
        accName = input("\tEnter your Name :")
        print("\n************************************************************")
        selectionScreen(num, accName)
        print("************************************************************")
    elif ch =='3':
        print("\tThank You for choosing our Bank, the System will now shut down")
        creatorMan.close()
        accountantMan.close()
        break
    else :
        print("Now now now. Choose from the given options only")
        time.sleep(3)
    print("\n")
    ch = input("Press the Enter key to continue")
