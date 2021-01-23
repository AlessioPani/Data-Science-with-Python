#Run this prior to starting the exercise
from random import randint as rnd


def genFiles(current,old):
    fee =('yes','no')

    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


def cleanFiles(currentMem,exMem):
    '''
    currentMem: File containing list of current members
    exMem: File containing list of old members
    
    Removes all rows from currentMem containing 'no' and appends them to exMem
    '''     
    with open(currentMem, 'r+') as currentFile:
        with open(exMem, 'a+') as appendFile:
            currentFile.seek(0,0)
            data = currentFile.readlines()
            header = data[0]
            members = data[1:]
            inactive = []
            for member in members:
                if 'no' in member:
                    inactive.append(member)

            currentFile.seek(0,0)
            currentFile.write(header)
            for member in members:
                if member in inactive:
                    appendFile.write(member)
                else:
                    currentFile.write(member)
            currentFile.truncate()
            appendFile.truncate()


def printFiles(fullFile, partialFile):
    '''
    Prints the two provided files. 
    '''
    memReg = fullFile
    exReg = partialFile

    with open(memReg,'r') as readFile:
        print("Active Members: \n\n")
        print(readFile.read())
        
    with open(exReg,'r') as readFile:
        print("Inactive Members: \n\n")
        print(readFile.read())


if __name__ == '__main__':

    # Names of the two files
    memReg = 'members.txt'
    exReg = 'inactive.txt'

    # Generate the two memReg and exReg .txt files
    genFiles(memReg,exReg)

    # Print the two files before manipulation
    print('### Files before the manipulation ###')
    printFiles(memReg,exReg)

    # Clean up of both files, according to the request
    cleanFiles(memReg,exReg)

    # Print the two files after manipulation
    print('### Files after the manipulation ###')
    printFiles(memReg,exReg)


