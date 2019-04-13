#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
#The use of "and" when writing out numbers is in compliance with British usage.
import time
start_time = time.clock()
einer={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',0:'',11:'eleven',12:'twelve',13:'thirteen'}
zehner={1:'teen',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',0:''}
word_string=''
for x in range(1,1000):
    number=x
    digits=len(str(number))
    if digits==3:
        digit_1=int(str(number)[0])
        digit_2=int(str(number)[1])
        digit_3=int(str(number)[2])
        if digit_2==0 and digit_3==0:
            word_string=word_string+(einer[digit_1]+'hundred')
        else:
            if digit_2==1 and digit_3==0:
                word_string = word_string + (einer[digit_1] + 'hundredandten')
            elif digit_2==1 and digit_3==1:
                word_string = word_string + (einer[digit_1] + 'hundredandeleven')
            elif digit_2==1 and digit_3==2:
                word_string = word_string + (einer[digit_1] + 'hundredandtwelve')
            elif digit_2==1 and digit_3==3:
                word_string = word_string + (einer[digit_1] + 'hundredandthirteen')
            elif digit_2==1 and digit_3==8:
                word_string = word_string + (einer[digit_1] + 'hundredandeighteen')
            elif digit_2==1 and digit_3==5:
                word_string = word_string + (einer[digit_1] + 'hundredandfifteen')
            else:
                word_string = word_string + (einer[digit_1]+'hundredand'+zehner[digit_2]+einer[digit_3])
    elif digits==2:
        digit_1=int(str(number)[0])
        digit_2=int(str(number)[1])
        if digit_1 == 1 and digit_2 == 1:
            word_string = word_string + ('eleven')
        elif digit_1 == 1 and digit_2 == 2:
            word_string = word_string + ('twelve')
        elif digit_1 == 1 and digit_2 == 0:
            word_string = word_string + ('ten')
        elif digit_1 == 1 and digit_2 == 3:
            word_string = word_string + ('thirteen')
        elif digit_1 == 1 and digit_2 == 8:
            word_string = word_string + ('eighteen')
        elif digit_1 == 1 and digit_2 == 5:
            word_string = word_string + ('fifteen')
        else:
            word_string = word_string + (zehner[digit_1]+einer[digit_2])
    elif digits==1:
        digit_1=int(str(number)[0])
        word_string = word_string + (einer[digit_1])
word_string=word_string+'onethousand'
print(len(word_string))
print(time.clock() - start_time, "seconds")