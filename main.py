"""
This script is to familiarize myself with basics of python
Script will contain the BIO data of user inputs and then save it to a file
"""

# We create __init__.py to be able to import the class in a one line from the directory they're residing
#from global_var import DisplayInfo, CheckandSave, Updateinfo

import sys
import os
import csv
from contextlib import redirect_stdout      # For output redirection to a file
import pandas as pd     # Installed to search and replace specific data in csv file. Installed via "pip install pandas" from the command prompt


def outputInfo():

    fname = input("Enter your First Name: ")
    mname = input("Enter your Middle Name: ")
    lname = input("Enter your Last Name: ")
    address = input("Enter your Address: ")

    # Ensure the age is set as a number. If not, retry again
    while True:
        try:
            age = int(input("Enter your Age: "))
        except ValueError:
            print("Please input a number for the age")
        else:
            break

    myList = ["FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "ADDRESS", "AGE"]
    myInputs = [fname.upper(), mname.upper(), lname.upper(), address.upper(), age]

    print(f"\nHello {fname.upper()}, kindly confirm the details are correct before we save it:\n")

    # Pass the reference to a parameter
    definition=myList
    inputdata=myInputs

    # Create parameters which will check the number of data in myList and myInputs from the Biodata class
    countrange_myList=len(definition)
    countrange_myInputs=len(inputdata)

    # Check that myList and myInputs have the same number of array before proceeding
    if countrange_myList == countrange_myInputs:
        # List each information separated by ":"
        for i in range(countrange_myList):
            print(str(definition[i]) + str(": ") + str(inputdata[i]))
    else:
        print("ERROR: Definition list count is not equal to the data inputs count. Kindly verify the script")


    filename=os.path.isfile('Users_Biodata.csv')

    # Verify if all values are correct before proceeding
    ans=input("\nAre all values correct? [Press 'Y' or 'N']: ").upper()

    if ans == 'Y':
        print("OK, will now proceed saving the file")

        # Check if file exist. If it does not exist, create a new one; else, append it to existing file
        if filename == False:
            with open('Users_Biodata.csv', 'w', encoding='UTF-8', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(myList)
                writer.writerow(myInputs)
        else:
            with open('Users_Biodata.csv', 'a', encoding='UTF-8', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(myInputs)

    elif ans == 'N':
        print("Kindly double check your inputs and then try again")
        sys.exit()

    else:
        print("Wrong option. Program will exit")
        sys.exit(1)


def updateinfo():

    filename = os.path.isfile('Users_Biodata.csv')

    if filename == False:
        print(
            "Data file does not exist yet. Make sure an initial record has been created for the file to be created")
        sys.exit(1)

    else:
        option = str(input("""
\nPlease select which data will be updated below:

a) First Name
b) Middle Name
c) Last Name
d) Address
e) Age

Enter your option: """).upper())

        FNAME = "First Name"
        MNAME = "Middle Name"
        LNAME = "Last Name"
        ADD = "Address"
        AGE = "Age"

        # Check the option selected

        # If Option A
        if option == 'A':
            getvalue = str(input(f"Enter {FNAME}: "))

            # Read csv file via pandas
            data = pd.read_csv('Users_Biodata.csv', delimiter=',')

            # Print the record with the matching First Name
            print(f"\nHere is the list of records for {getvalue.upper()}:\n ")
            # print((data[data["FIRST_NAME"] == getvalue]))             # boolean indexing to output list of records

            # dataframe query; faster query than boolean indexing
            dataquery = data.query(f'FIRST_NAME == "{getvalue.upper()}"')
            print(dataquery)

            # Save the index/es from the output of dataquery to a file. This will be use for the getindex below
            dataquery.to_csv('indexlist.csv', columns=[], header=False)

            # Save the command output directly to a file. Reference only
            # with open('recordlist.csv', 'w') as list:
            #     with redirect_stdout(list):
            #         # print((data[data["FIRST NAME"] == getvalue]))

            # Capture index selection from the dataquery output
            getindex = int(input("\nSelect index to be updated: "))

            # Convert the getindex into string to be use in filtering the indexlist.csv file
            getindex2 = str(getindex)

            # Verify the getindex selected exists in the indexlist.csv file
            with open('indexlist.csv', 'r') as indexlistfile:
                reader = csv.reader(indexlistfile, delimiter=',')

                for row in reader:  # Read each row in indexlist.csv file
                    if getindex2 in row:
                        newfirstname = str(input(f"Enter the new {FNAME}: "))
                        data.at[getindex, "FIRST_NAME"] = f"{newfirstname.upper()}"
                        data.index.name = 'Index'  # Add column name to Index

                        print("File saved! See updated entry below for reference:\n")
                        output = data.query(
                            f'Index == {getindex2}')  # Filter the updated index via Index Column Name
                        print(output)

                        data.index.name = None  # Remove the column name of Index before saving
                        data.to_csv('Users_Biodata.csv', index=False)

                        # print("File saved! See updated entry below for reference:\n")
                        # output=data.query(f'FIRST_NAME == "{newfirstname.upper()}"')
                        # print(output)

                    else:
                        with open(os.devnull, 'w') as indexfilter:  # Any rows not matching will be sent to null
                            with redirect_stdout(indexfilter):
                                print(getindex2)

            os.remove("indexlist.csv")  # Remove indexlist.csv file after the update
            exit()

            # Another set of commands to replace value in csv file, replacing all matching values in the file
            # data.replace(to_replace=f"{getvalue}", value=f"{newfirstname}", inplace=True)
            # data.to_csv('outputfile.csv', index=False)
            # os.remove('Users.csv')
            # os.rename('outputfile.csv', 'Users.csv')

        # If Option B
        if option == 'B':
            getvalue = str(input(f"Enter {FNAME}: "))

            # Read csv file via pandas
            data = pd.read_csv('Users_Biodata.csv', delimiter=',')

            # Print the record with the matching First Name
            print(f"\nHere is the list of records for {getvalue.upper()}:\n ")

            # dataframe query; faster query than boolean indexing
            dataquery = data.query(f'FIRST_NAME == "{getvalue.upper()}"')
            print(dataquery)

            # Save the index/es from the output of dataquery to a file. This will be use for the getindex below
            dataquery.to_csv('indexlist.csv', columns=[], header=False)

            # Capture index selection from the dataquery output
            getindex = int(input("\nSelect index to be updated: "))

            # Convert the getindex into string to be use in filtering the indexlist.csv file
            getindex2 = str(getindex)

            # Verify the getindex selected exists in the indexlist.csv file
            with open('indexlist.csv', 'r') as indexlistfile:
                reader = csv.reader(indexlistfile, delimiter=',')

                for row in reader:  # Read each row in indexlist.csv file
                    if getindex2 in row:
                        newmidname = str(input(f"Enter the new {MNAME}: "))
                        data.at[getindex, "MIDDLE_NAME"] = f"{newmidname.upper()}"
                        data.index.name = 'Index'  # Add column name to Index

                        print("File saved! See updated entry below for reference:\n")
                        output = data.query(
                            f'Index == {getindex2}')  # Filter the updated index via Index Column Name
                        print(output)

                        data.index.name = None  # Remove the column name of Index before saving
                        data.to_csv('Users_Biodata.csv', index=False)

                        # print("File saved! See updated entry below for reference:\n")
                        # output=data.query(f'MIDDLE_NAME == "{newmidname.upper()}"')
                        # print(output)

                    else:
                        with open(os.devnull, 'w') as indexfilter:  # Any rows not matching will be sent to null
                            with redirect_stdout(indexfilter):
                                print(getindex2)

            os.remove("indexlist.csv")  # Remove indexlist.csv file after the update
            exit()

        # If Option C
        if option == 'C':
            getvalue = str(input(f"Enter {FNAME}: "))

            # Read csv file via pandas
            data = pd.read_csv('Users_Biodata.csv', delimiter=',')

            # Print the record with the matching First Name
            print(f"\nHere is the list of records for {getvalue.upper()}:\n ")

            # dataframe query; faster query than boolean indexing
            dataquery = data.query(f'FIRST_NAME == "{getvalue.upper()}"')
            print(dataquery)

            # Save the index/es from the output of dataquery to a file. This will be use for the getindex below
            dataquery.to_csv('indexlist.csv', columns=[], header=False)

            # Capture index selection from the dataquery output
            getindex = int(input("\nSelect index to be updated: "))

            # Convert the getindex into string to be use in filtering the indexlist.csv file
            getindex2 = str(getindex)

            # Verify the getindex selected exists in the indexlist.csv file
            with open('indexlist.csv', 'r') as indexlistfile:
                reader = csv.reader(indexlistfile, delimiter=',')

                for row in reader:  # Read each row in indexlist.csv file
                    if getindex2 in row:
                        newlastname = str(input(f"Enter the new {LNAME}: "))
                        data.at[getindex, "LAST_NAME"] = f"{newlastname.upper()}"
                        data.index.name = 'Index'  # Add column name to Index

                        print("File saved! See updated entry below for reference:\n")
                        output = data.query(
                            f'Index == {getindex2}')  # Filter the updated index via Index Column Name
                        print(output)

                        data.index.name = None  # Remove the column name of Index before saving
                        data.to_csv('Users_Biodata.csv', index=False)

                        # print("File saved! See updated entry below for reference:\n")
                        # output=data.query(f'LAST_NAME == "{newlastname.upper()}"')
                        # print(output)

                    else:
                        with open(os.devnull, 'w') as indexfilter:  # Any rows not matching will be sent to null
                            with redirect_stdout(indexfilter):
                                print(getindex2)

            os.remove("indexlist.csv")  # Remove indexlist.csv file after the update
            exit()

        # If Option D
        if option == 'D':
            getvalue = str(input(f"Enter {FNAME}: "))

            # Read csv file via pandas
            data = pd.read_csv('Users_Biodata.csv', delimiter=',')

            # Print the record with the matching First Name
            print(f"\nHere is the list of records for {getvalue.upper()}:\n ")

            # dataframe query; faster query than boolean indexing
            dataquery = data.query(f'FIRST_NAME == "{getvalue.upper()}"')
            print(dataquery)

            # Save the index/es from the output of dataquery to a file. This will be use for the getindex below
            dataquery.to_csv('indexlist.csv', columns=[], header=False)

            # Capture index selection from the dataquery output
            getindex = int(input("\nSelect index to be updated: "))

            # Convert the getindex into string to be use in filtering the indexlist.csv file
            getindex2 = str(getindex)

            # Verify the getindex selected exists in the indexlist.csv file
            with open('indexlist.csv', 'r') as indexlistfile:
                reader = csv.reader(indexlistfile, delimiter=',')

                for row in reader:  # Read each row in indexlist.csv file
                    if getindex2 in row:
                        newaddress = str(input(f"Enter the new {ADD}: "))
                        data.at[getindex, "ADDRESS"] = f"{newaddress.upper()}"
                        data.index.name = 'Index'  # Add column name to Index

                        print("File saved! See updated entry below for reference:\n")
                        output = data.query(
                            f'Index == {getindex2}')  # Filter the updated index via Index Column Name
                        print(output)

                        data.index.name = None  # Remove the column name of Index before saving
                        data.to_csv('Users_Biodata.csv', index=False)

                        # print("File saved! See updated entry below for reference:\n")
                        # output=data.query(f'ADDRESS == "{newaddress.upper()}"')
                        # print(output)

                    else:
                        with open(os.devnull, 'w') as indexfilter:  # Any rows not matching will be sent to null
                            with redirect_stdout(indexfilter):
                                print(getindex2)

            os.remove("indexlist.csv")  # Remove indexlist.csv file after the update
            exit()

        # If Option E
        if option == 'E':
            getvalue = str(input(f"Enter {FNAME}: "))

            # Read csv file via pandas. AGE column was set as str so that line 274 can output the changes
            data = pd.read_csv('Users_Biodata.csv', delimiter=',', dtype={'AGE': str})

            # Print the record with the matching First Name
            print(f"\nHere is the list of records for {getvalue.upper()}:\n ")

            # dataframe query; faster query than boolean indexing
            dataquery = data.query(f'FIRST_NAME == "{getvalue.upper()}"')
            print(dataquery)

            # Save the index/es from the output of dataquery to a file. This will be use for the getindex below
            dataquery.to_csv('indexlist.csv', columns=[], header=False)

            # Capture index selection from the dataquery output
            getindex = int(input("\nSelect index to be updated: "))

            # Convert the getindex into string to be use in filtering the indexlist.csv file
            getindex2 = str(getindex)

            # Verify the getindex selected exists in the indexlist.csv file
            with open('indexlist.csv', 'r') as indexlistfile:
                reader = csv.reader(indexlistfile, delimiter=',')

                for row in reader:  # Read each row in indexlist.csv file
                    if getindex2 in row:
                        newage = str(input(f"Enter the new {AGE}: "))
                        data.at[getindex, "AGE"] = f"{newage}"
                        data.index.name = 'Index'  # Add column name to Index

                        print("File saved! See updated entry below for reference:\n")
                        output = data.query(
                            f'Index == {getindex2}')  # Filter the updated index via Index Column Name
                        print(output)

                        data.index.name = None  # Remove the column name of Index before saving
                        data.to_csv('Users_Biodata.csv', index=False)

                    else:
                        with open(os.devnull, 'w') as indexfilter:  # Any rows not matching will be sent to null
                            with redirect_stdout(indexfilter):
                                print(getindex2)

            os.remove("indexlist.csv")  # Remove indexlist.csv file after the update
            exit()

        else:
            print("Wrong option. Please select correct option from the list")


def main():

    print("USERS BIODATA")

    option=str(input("(A) Create new user information\n(B) Update existing user information\n\nSelect option: "))

    if option.upper() == 'A':
        outputInfo()

    elif option.upper() == 'B':
        updateinfo()

    else:
        print("Wrong option. Program will not exit")
        exit(1)


if __name__ == "__main__":
    main()