#A common security method used for online banking is to ask the user for three random characters from a passcode.
#For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
#be: 317.

#The text file, keylog.txt, contains fifty successful login attempts.

#Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
#possible secret passcode of unknown length.
import time
start_time = time.clock()
path="C:/Users/Florian Habenstein/PycharmProjects/Project Euler/p079_keylog.txt"
f=open(path)
logins=[]
for line in f:
    logins.append(line[0:3])

numbers={}
for login in logins:
    for number in login:
        if number not in numbers:
            numbers[number]=[]

for login in logins:
    if login[-2] not in numbers[login[-1]]:
        numbers[login[-1]].append(login[-2])
    if login[-3] not in numbers[login[-2]]:
        numbers[login[-2]].append(login[-3])

password=""
while len(password)<8:
    for number in numbers:
        if numbers[number]==[]:
            password=password+str(number)
            numbers[number]="done"
            for element in numbers:
                try:
                    numbers[element].remove(number)
                except:
                    pass

print(password)
print(time.clock() - start_time, "seconds")