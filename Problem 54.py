import time
start_time = time.clock()
file=open("C:\\Users\\Florian Habenstein\\PycharmProjects\\Project Euler\\p054_poker.txt","r")
zwischen=[]
for line in file:
    zwischen.append(str(line).replace("\n",""))
file.close()
p1vs=[]
p2vs=[]
for hand in zwischen:
    p1vs.append(hand[0:15])
    p2vs.append(hand[15:])

p1v=[]
p1s=[]
p2s=[]
p2v=[]

for x in p1vs:
    p1v.append(x.replace('H','').replace("C",'').replace("D",'').replace("S",'').replace(' ',""))
for x in p2vs:
    p2v.append(x.replace('H','').replace("C",'').replace("D",'').replace("S",'').replace(' ',""))

for x in p1vs:
    p1s.append(x.replace('2','').replace("3",'').replace("4",'').replace("5",'').replace('6','').replace("7",'').replace("8",'').replace("9",'').replace('T','').replace("J",'').replace("Q",'').replace("K",'').replace("A",'').replace(" ",''))
for x in p2vs:
    p2s.append(x.replace('2','').replace("3",'').replace("4",'').replace("5",'').replace('6','').replace("7",'').replace("8",'').replace("9",'').replace('T','').replace("J",'').replace("Q",'').replace("K",'').replace("A",'').replace(" ",''))

p1v=p1v+p2v
p1s=p1s+p2s

scores=[]
for z in range(len(p1v)):
    flush=False
    straight=False
    high_card=False
    score=0


    'Flush'
    if score<600000000:
        for x in p1s[z]:
            y=p1s[z].count(x)
            if y==5:
                score=600000000
                flush=True
                if p1v[z].count('A') == 1:
                    score = 614000000
                if p1v[z].count('K') == 1 and score < 614000000:
                    score = 614000000
                if p1v[z].count('Q') == 1 and score < 613000000:
                    score = 612000000
                if p1v[z].count('J') == 1 and score < 612000000:
                    score = 611000000
                if p1v[z].count('T') == 1 and score < 611000000:
                    score = 610000000
                if p1v[z].count('9') == 1 and score < 610000000:
                    score = 609000000
                if p1v[z].count('8') == 1 and score < 609000000:
                    score = 608000000
                if p1v[z].count('7') == 1 and score < 608000000:
                    score = 607000000
                if p1v[z].count('6') == 1 and score < 607000000:
                    score = 606000000
                if p1v[z].count('5') == 1 and score < 606000000:
                    score = 605000000
                if p1v[z].count('4') == 1 and score < 605000000:
                    score = 604000000
                if p1v[z].count('3') == 1 and score < 604000000:
                    score = 603000000
                if p1v[z].count('2') == 1 and score < 603000000:
                    score = 602000000
    'Four of a Kind'
    if score<800000000:
        for x in p1v[z]:
            y=p1v[z].count(x)
            if y==4:
                score=800000000
                high_card=True
                if y == 'A':
                    score = 814000000
                if y == 'K':
                    score = 813000000
                if y == 'Q':
                    score = 812000000
                if y == 'J':
                    score = 811000000
                if y == 'T':
                    score = 810000000
                if y == '9':
                    score = 809000000
                if y == '8':
                    score = 808000000
                if y == '7':
                    score = 807000000
                if y == '6':
                    score = 806000000
                if y == '5':
                    score = 805000000
                if y == '4':
                    score = 804000000
                if y == '3':
                    score = 803000000
                if y == '2':
                    score = 802000000
            'hier fehlt noch die bestimmung der höhe'
    'Three of a Kind'
    if score<400000000:
        for x in p1v[z]:
            y=p1v[z].count(x)
            if y==3:
                score=400000000
                high_card=True
                if x == 'A':
                    score = 414000000
                if x == 'K':
                    score = 413000000
                if x == 'Q':
                    score = 412000000
                if x == 'J':
                    score = 411000000
                if x == 'T':
                    score = 410000000
                if x == '9':
                    score = 409000000
                if x == '8':
                    score = 408000000
                if x == '7':
                    score = 407000000
                if x == '6':
                    score = 406000000
                if x == '5':
                    score = 405000000
                if x == '4':
                    score = 404000000
                if x == '3':
                    score = 403000000
                if x == '2':
                    score = 402000000
    'Two pairs'
    if score<300000000:
        for a in p1v[z]:
            for b in p1v[z]:
                if p1v[z].count(a)==2 and p1v[z].count(b)==2 and a!=b:
                    score=300000000
                    high_card=True
                    if a=='A' or b=='A':
                        score = 314000000
                    if a=='K' or b=='K' and score<314000000:
                        score = 313000000
                    if a=='Q' or b=='Q' and score<313000000:
                        score = 312000000
                    if a=='J' or b=='J' and score<312000000:
                        score = 311000000
                    if a=='T' or b=='T' and score<311000000:
                        score = 310000000
                    if a=='9' or b=='9' and score<310000000:
                        score = 309000000
                    if a=='8' or b=='8' and score<309000000:
                        score = 308000000
                    if a=='7' or b=='7' and score<308000000:
                        score = 307000000
                    if a=='6' or b=='6' and score<307000000:
                        score = 306000000
                    if a=='5' or b=='5' and score<306000000:
                        score = 305000000
                    if a=='4' or b=='4' and score<305000000:
                        score = 304000000
                    if a=='3' or b=='3' and score<304000000:
                        score = 303000000
                    if a == '2' or b == '2' and score < 303000000:
                        score = 302000000
                'es fehlt die bestimmung der höhe'
    'Full House'
    if score<700000000:
        for a in p1v[z]:
            for b in p1v[z]:
                if p1v[z].count(a)==2 and p1v[z].count(b)==3 and a!=b:
                    if a=='A':
                        score=714000000
                    if a=='K':
                        score=713000000
                    if a=='Q':
                        score=712000000
                    if a=='J':
                        score = 711000000
                    if a=='T':
                        score = 710000000
                    if a=='9':
                        score = 709000000
                    if a=='8':
                        score = 708000000
                    if a=='7':
                        score = 707000000
                    if a=='6':
                        score = 706000000
                    if a=='5':
                        score = 705000000
                    if a=='4':
                        score = 704000000
                    if a=='3':
                        score = 703000000
                    if a=='2':
                        score = 702000000
                    if b=='A':
                        score = score + 140000
                    if b=='K':
                        score = score + 130000
                    if b=='Q':
                        score = score + 120000
                    if b=='J':
                        score = score + 110000
                    if b=='T':
                        score = score + 100000
                    if b=='9':
                        score = score + 90000
                    if b=='8':
                        score = score + 80000
                    if b=='7':
                        score = score + 70000
                    if b=='6':
                        score = score + 60000
                    if b=='5':
                        score = score + 50000
                    if b=='4':
                        score = score + 40000
                    if b=='3':
                        score = score + 30000
                    if b=='2':
                        score = score+20000
    'Straight'
    if score<500000000:
        if p1v[z].count('2')==1 and p1v[z].count('3')==1 and p1v[z].count('4')==1 and p1v[z].count('5')==1 and p1v[z].count('6')==1:
            score=501000000
            straight=True
        if p1v[z].count('7')==1 and p1v[z].count('3')==1 and p1v[z].count('4')==1 and p1v[z].count('5')==1 and p1v[z].count('6')==1:
            score=502000000
            straight=True
        if p1v[z].count('7')==1 and p1v[z].count('8')==1 and p1v[z].count('4')==1 and p1v[z].count('5')==1 and p1v[z].count('6')==1:
            score=503000000
            straight=True
        if p1v[z].count('7')==1 and p1v[z].count('8')==1 and p1v[z].count('9')==1 and p1v[z].count('5')==1 and p1v[z].count('6')==1:
            score=504000000
            straight=True
        if p1v[z].count('7')==1 and p1v[z].count('8')==1 and p1v[z].count('9')==1 and p1v[z].count('T')==1 and p1v[z].count('6')==1:
            score=505000000
            straight=True
        if p1v[z].count('7')==1 and p1v[z].count('8')==1 and p1v[z].count('9')==1 and p1v[z].count('T')==1 and p1v[z].count('J')==1:
            score=506000000
            straight=True
        if p1v[z].count('Q')==1 and p1v[z].count('8')==1 and p1v[z].count('9')==1 and p1v[z].count('T')==1 and p1v[z].count('J')==1:
            score=507000000
            straight=True
        if p1v[z].count('Q')==1 and p1v[z].count('K')==1 and p1v[z].count('9')==1 and p1v[z].count('T')==1 and p1v[z].count('J')==1:
            score=508000000
            straight=True
        if p1v[z].count('Q')==1 and p1v[z].count('K')==1 and p1v[z].count('A')==1 and p1v[z].count('T')==1 and p1v[z].count('J')==1:
            score=509000000
            straight=True
    'one Pair'
    if score<200000000:
        for a in p1v[z]:
            if p1v[z].count(a)==2:
                cv=p1v[z].replace(a,'')
                high_card=True
                if a == 'A':
                    score = 214000000
                if a == 'K':
                    score = 213000000
                if a == 'Q':
                    score = 212000000
                if a == 'J':
                    score = 211000000
                if a == 'T':
                    score = 210000000
                if a == '9':
                    score = 209000000
                if a == '8':
                    score = 208000000
                if a == '7':
                    score = 207000000
                if a == '6':
                    score = 206000000
                if a == '5':
                    score = 205000000
                    if cv.count('K') == 1:
                        score = score + 130000
                    if cv.count('Q') == 1 and score < 205130000:
                        score = score + 120000
                    if cv.count('J') == 1 and score < 205120000:
                        score = score + 110000
                    if cv.count('T') == 1 and score < 205110000:
                        score = score + 100000
                    if cv.count('9') == 1 and score < 205100000:
                        score = score + 90000
                    if cv.count('8') == 1 and score < 205090000:
                        score = score + 80000
                    if cv.count('7') == 1 and score < 205080000:
                        score = score + 70000
                    if cv.count('6') == 1 and score < 205070000:
                        score = score + 60000
                    if cv.count('5') == 1 and score < 205060000:
                        score = score + 50000
                    if cv.count('4') == 1 and score < 205050000:
                        score = score + 40000
                    if cv.count('3') == 1 and score < 205040000:
                        score = score + 30000
                    if cv.count('2') == 1 and score < 205030000:
                        score = score + 20000
                if a == '4':
                    score = 204000000
                if a == '3':
                    score = 203000000
                if a == '2':
                    score = 202000000
    'high card'
    if score<100000000:
        score=100000000
        current_values=p1v[z]
        if p1v[z].count('A')==1:
            score=114000000
            cv=current_values.replace('A','')
            if cv.count('K')==1:
                score=score+130000
            if cv.count('Q')==1 and score<114130000:
                score=score+120000
            if cv.count('J')==1 and score<114120000:
                score=score+110000
            if cv.count('T')==1 and score<114110000:
                score=score+100000
            if cv.count('9')==1 and score<114100000:
                score=score+90000
            if cv.count('8')==1 and score<114090000:
                score=score+80000
            if cv.count('7')==1 and score<114080000:
                score=score+70000
            if cv.count('6')==1 and score<114070000:
                score=score+60000
            if cv.count('5')==1 and score<114060000:
                score=score+50000
            if cv.count('4')==1 and score<114050000:
                score=score+40000
            if cv.count('3')==1 and score<114040000:
                score=score+30000
            if cv.count('2')==1 and score<114030000:
                score=score+20000
        if p1v[z].count('K')==1 and score<114000000:
            score=113000000
        if p1v[z].count('Q')==1 and score<113000000:
            score=112000000
        if p1v[z].count('J')==1 and score<112000000:
            score=111000000
        if p1v[z].count('T')==1 and score<111000000:
            score=110000000
        if p1v[z].count('9')==1 and score<110000000:
            score=109000000
        if p1v[z].count('8')==1 and score<109000000:
            score=108000000
        if p1v[z].count('7')==1 and score<108000000:
            score=107000000
        if p1v[z].count('6')==1 and score<107000000:
            score=106000000
        if p1v[z].count('5')==1 and score<106000000:
            score=105000000
        if p1v[z].count('4')==1 and score<105000000:
            score=104000000
        if p1v[z].count('3')==1 and score<104000000:
            score=103000000
        if p1v[z].count('2')==1 and score<103000000:
            score=102000000
    scores.append(score)

score1=scores[0:1000]
score2=scores[1000:2000]

wins=0
unentschieden=0
for x in range(len(score1)):
    if score1[x]>score2[x]:
        wins=wins+1
    if score1[x]==score2[x]:
        unentschieden=unentschieden+1

print('\n \n ------------------------------------------------------------------------------------------------\nSpieler 1 gewinnt %s mal! Spieler 2 gewinnt %s mal! Unentschieden gibt es %s! Um dieses Ergebnis zu erhalten hat \n das Programm %s Sekunden gerechnet und ich habe 5 Tage programmiert.\n--------------------------------------------------------------------'%(wins,1000-wins,unentschieden,time.clock() - start_time))
