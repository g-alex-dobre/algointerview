phoneNumber = input("Please enter the phoneNumber: ")
print(phoneNumber)

i = input(" How many words you want to search: ")
print(i)
i = int(i)
wordlist = [] * i
for a in range(0, i):
    temp = input("Input word " + str(a) + ":")
    wordlist.append(temp)

print(wordlist)
# the following function transforms strings into phone keys
def transformtonum(wrd):
    newstring= ""
    for a in range(0, len(wrd)):
        # if wrd[a] == "a" or wrd[a] == "b" or wrd[a] == "c":
        if wrd[a] in "ABCabc":
            newstring =  newstring + "2"
        # elif wrd[a] == "d" or wrd[a] == "e" or wrd[a] == "f" or wrd[a] == "g":
        elif  wrd[a] in "DEFdef":
            newstring = newstring + "3"
        elif wrd[a] in "GHIghi":
            newstring = newstring + "4"
        elif wrd[a] in "JKLjkl":
            newstring = newstring + "5"
        elif wrd[a] in "MNOmno":
            newstring = newstring + "6"
        elif wrd[a] in "PQRSpqrs":
            newstring = newstring + "7"
        elif wrd[a] in "TUVtuv":
            newstring =  newstring + "8"
        elif wrd[a] in "WXYZwxyz":
            newstring = newstring + "9"
    return newstring

# wordtonum is a list, initialize the list and then assign strings that are transformed with the transformtonum function
wordtonum = [] * i
for a in range(0, i):
    wordtonum.append(transformtonum(wordlist[a]))
print (wordtonum)

#check if the "word" is in the phone number and then output the word
print("The following words are part of the Phone number: ")
for b in range(0, i):
    if wordtonum[b] in phoneNumber:
        print(wordlist[b])

