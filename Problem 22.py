#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
#is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?
import time
start_time = time.clock()
file=open("C:\\Users\\Florian Habenstein\\PycharmProjects\\Project Euler\\p022_names.txt","r")
x=str(file.read())
names=[]
y=x.replace('"','')
name=""
for z in y:
    if z==",":
        names.append(name)
        name=""
    else:
        name=name+z
names.append(name)
file.close
scores={"A":1,
"B":2,
"C":3,
"D":4,
"E":5,
"F":6,
"G":7,
"H":8,
"I":9,
"J":10,
"K":11,
"L":12,
"M":13,
"N":14,
"O":15,
"P":16,
"Q":17,
"R":18,
"S":19,
"T":20,
"U":21,
"V":22,
"W":23,
"X":24,
"Y":25,
"Z":26}

names.sort()
names_and_scores={}
for word in names:
    name_score=0
    for letter in word:
        for score in scores:
            if letter==score:
                name_score=name_score+scores[score]
    names_and_scores[word]=name_score

print(names_and_scores)
n=1
summe=0
for entry in names_and_scores:
    summe=summe+n*names_and_scores[entry]
    print(n)
    print(names_and_scores[entry])
    n=n+1


print(summe)
print(time.clock() - start_time, "seconds")