#Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for
#Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
#taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
#restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes.
#The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it
#is impossible to decrypt the message.

#Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
#If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
#The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt
#(right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
#plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original
#text.
import time
start_time = time.clock()
file=open("C:\\Users\\Florian Habenstein\\PycharmProjects\\Project Euler\\p059_cipher.txt","r")
cipher_str=str(file.read())
file.close()

#Extract ascii characters from text file into list
cip_ascii_list=[]
ascii=""
for character in cipher_str:
    if character==",":
        cip_ascii_list.append(int(ascii))
        ascii=""
    else:
        ascii = ascii + character
cip_ascii_list.append(73)

#Slice ciphered message into lists of elements decipherd with different characters of the key
def slice_cip_message(cip_message):
    sliced_cip_1 = []
    sliced_cip_2 = []
    sliced_cip_3 = []
    index_1=0
    index_2=1
    index_3=2
    len_key=3
    for times in range(int(len(cip_message)/len_key)+1):
        try:
            sliced_cip_1.append(cip_message[index_1])
            index_1 += 3
        except:
            pass
        try:
            sliced_cip_2.append(cip_message[index_2])
            index_2 += 3
        except:
            pass
        try:
            sliced_cip_3.append(cip_message[index_3])
            index_3+=3
        except:
            sliced_message=[sliced_cip_1,sliced_cip_2,sliced_cip_3]
            return(sliced_message)

def decipher_XOR(submessage,key_character):
    deciphered_submessage_clear=[]
    deciphered_submessage_ascii=[]
    for character in submessage:
        deciphered_submessage_clear.append(chr(character^key_character))
        deciphered_submessage_ascii.append(character ^ key_character)
    return([deciphered_submessage_clear,deciphered_submessage_ascii])

def get_letter_freq(text):
    letter_freq={"a":0,"e":0,"i":0,"o":0,"u":0}
    for element in text:
        try:
            letter_freq[element.lower()]+=1
        except:
            pass
    for letter in letter_freq:
        letter_freq[letter]=(letter_freq[letter]/len(text))*100
    return(letter_freq)

def is_string_english(lett_freq):
    freq_a=8.167
    freq_e=12.702
    freq_i=6.966
    freq_o=7.507
    freq_u=2.758
    error_term=0.6
    if (lett_freq["a"]>freq_a-(freq_a*error_term) and lett_freq["a"]<freq_a+(freq_a*error_term)
        and lett_freq["e"]>freq_e-(freq_e*error_term) and lett_freq["e"]<freq_e+(freq_e*error_term)
        and lett_freq["i"]>freq_i-(freq_i*error_term) and lett_freq["i"]<freq_i+(freq_i*error_term)
        and lett_freq["o"]>freq_o-(freq_o*error_term) and lett_freq["o"]<freq_o+(freq_o*error_term)
        and lett_freq["u"]>freq_u-(freq_u*error_term) and lett_freq["u"]<freq_u+(freq_u*error_term)):
        return(True)
    else:
        return(False)

sliced_message=slice_cip_message(cip_ascii_list)

#decipher the submessages
for key_character in range(97,122):
    x=decipher_XOR(sliced_message[0],key_character)[0]
    if is_string_english(get_letter_freq(x))==True:
        key_1=(chr(key_character))
        sum_1=sum(decipher_XOR(sliced_message[0],key_character)[1])
        sub_1=(decipher_XOR(sliced_message[0],key_character)[0])
        break
for key_character in range(97,122):
    x=decipher_XOR(sliced_message[1],key_character)[0]
    if is_string_english(get_letter_freq(x))==True:
        key_2=(chr(key_character))
        sum_2=sum(decipher_XOR(sliced_message[1],key_character)[1])
        sub_2=(decipher_XOR(sliced_message[1],key_character)[0])
        break
for key_character in range(97,122):
    x=decipher_XOR(sliced_message[2],key_character)[0]
    if is_string_english(get_letter_freq(x))==True:
        key_3=(chr(key_character))
        sum_3=sum(decipher_XOR(sliced_message[2],key_character)[1])
        sub_3=(decipher_XOR(sliced_message[2],key_character)[0])
        break

message=""
for x in range(len(sub_1)-1):
    try:
        message=message+sub_1[x]
    except:
        break
    try:
        message=message+sub_2[x]
    except:
        break
    try:
        message=message+sub_3[x]
    except:
        break

print("The encrypted message is:",message)
print("The key to decipher the message is ", key_1,key_2,key_3,"!")
print("The sum of the deciphered ascii characters is", sum_1+sum_2+sum_3,".")
print(time.clock() - start_time, "seconds")

