import os
import pandas


def newData():
    '''
    Adds password data to the text file for the user
    '''
    newSite = input("Please input the service you want to store your password for!")
    sitePass = input("Password for site: ")
    with open(userid + ".txt", 'a') as ns:
        ns.write(newSite.lower() + " ")
        ns.write(sitePass.lower() + "\n")
    main()


def main():
    if os.stat(userid + ".txt").st_size == 0:  # checks if the password text file for the user is empty
        print("You have no stored passwords! Please add some.")
        newData()
    newDataq = input("Do you want to store new passwords? 'Yes' or 'No")
    if newDataq.lower() == "yes":
        newData()
    with open(userid + ".txt", 'r') as pd:
        pdata = pd.read().splitlines()
    datadict = {}
    for i in pdata:
        d = i.split()
        datadict[d[0]] = d[1]
    site = input("What service do you want the password for: ")
    print(f"Password: {datadict[site]} \nThis has been copied to your clipboard!")
    df = pandas.DataFrame(
        [datadict[site]])  # This line and the following are to copy the password into the user's clipboard
    df.to_clipboard(index=False, header=False)


def userInput():
    global userid
    userid = input("User ID (Leave empty if new user!): ")

    if userid == "":
        uname = input("Please input a new User ID: ")
        newpassw = input("Please input a password for the manager: ")
        with open("userIDList.txt", "a") as f:
            f.write(uname + " ")
        with open("passList.txt", "a") as p:
            p.write(newpassw + " ")
        with open(uname + ".txt", 'w') as _:
            pass
        print("Please restart program and login again using your new account! \n")
        quit()
    with open("userIDList.txt", "r") as fr:
        storedIDs = fr.read()
        storedIdList = storedIDs.split()

    if userid in storedIdList:
        passw = input("Password: ")
        with open("passList.txt", "r") as pr:
            storedPass = pr.read()
            storedPassList = storedPass.split()
        idDict = dict(zip(storedIdList, storedPassList))
        if passw == idDict[userid]:
            main()
        else:
            print("You input the wrong password, try again! \n")
            userInput()
    else:
        print("You input a wrong username, try again! \n")
        userInput()


userInput()
