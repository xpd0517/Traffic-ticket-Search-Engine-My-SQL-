import sys
import cx_Oracle
import getpass
import os
from datetime import date, datetime, timedelta

from NewVehicleReg import *
from autoTransaction import *
from driverlicenceregistration import *
from violationRecord import *
from searchEngine import *
from addvehicle import *

def connect():
    logintime = 0
    while logintime < 3:
        #connstr = input("Enter your username: ")
        #if connstr.lower() == 'q' or connstr.lower() == "quit":
        #    return 0, 0
        #connstr += '/' + getpass.getpass("Enter your password: ")
        user = 'pengda'
        pw = '03m21d32h' 
        connstr = ''+user + '/'+pw+'@gwynne.cs.ualberta.ca:1521/crs'
        try:
            connection = cx_Oracle.connect(connstr)
            print("Connection successful")
            return connection, connection.cursor()
        except:
            print("Unable to connect to the database")
            logintime += 1
            continue
    print("Unable to connect to ORACLE after 3 attempts, exit the program")
    return 0, 0




def main():
    
    connection, curs = connect()
    if connection == 0:
        print("Error connecting to database")
        return

    print("Main Menu")
    print("Choose the number of function")
    print("1. New Vehicle Registration (n)")
    print("2. Auto Transaction (a)")
    print("3. Driver Licence Registration (d)")
    print("4. Violation Record (v)")
    print("5. Search Engine (s)")
    print("type quit(q) to quit, cls(c) to clear screen")
    print("type menu(m) to display menu")
    
    while True:
        inp = input("Enter your choice: ").lower()
        if inp == 'q' or inp == 'quit' or inp == "exit":
            while True:
                inp = input("Do you want to exit? ").lower()
                if inp == 'y' or inp == 'yes' or inp == 'q':
                    print("Quit")
                    return
                elif inp == 'n' or inp == 'no':
                    break
                else:
                    print("Please enter yes (y) or no (n)")
                    continue
            continue
        elif inp == '1' or inp == 'n':
            newVehicleRegistration(curs, connection)
        elif inp == '2' or inp == 'a':
            driverLicenceRegistration(curs, connection)
        elif inp == '3' or inp == 'd':
            inp = '3'
            while inp == '3':
                driverLicenceRegistration(curs, connection)
                inp = input("Do you want to register another licence? (y/n) > ").lower()
                while True:
                    if inp == 'y' or inp == 'yes':
                        inp = '3'
                        break
                    elif inp == 'n' or inp == 'no' or inp == 'quit':
                        inp = 'zzzzz'
                        break
                    else:
                        inp = input("Please answer yes(y) or no(n) > ").lower()
        elif inp == '4' or inp == 'v':
            violationRecord(curs, connection)
        elif inp == '5' or inp == 's':
            searchEngine(curs, connection)
        elif inp == 'cls' or inp == 'c':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Main Menu")
            print("1. New Vehicle Registration (n)")
            print("2. Auto Transaction (a)")
            print("3. Driver Licence Registration (d)")
            print("4. Violation Record (v)")
            print("5. Search Engine (s)")
            print("type quit(q) to quit, cls(c) to clear screen")
            print("type menu(m) to display menu")
        elif inp == 'menu' or inp == 'm':
            print("Main Menu")
            print("1. New Vehicle Registration (n)")
            print("2. Auto Transaction (a)")
            print("3. Driver Licence Registration (d)")
            print("4. Violation Record (v)")
            print("5. Search Engine (s)")
            print("type quit to quit(q), cls(c) to clear screen")
            print("type menu(m) to display menu")
        else:
            print("Invalid")
        print(inp)

    cursor.close()
    connection.close()
    return

if __name__ == "__main__":
    main()
