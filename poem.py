import sys

''' This programme will take keywords as input from user and will display poem relaed to their input keywords  '''

print("POEMS OF YOUR FAVOURITE KEYWORDS\n")
name = input("enter your name\n")
print("dear" , name , "you have to choose from following keywords")
print("\n")
print('''keywords :\n\nalone\ncrazy\ndream\nfriend\nfuture\ngirl\nhope\njoy\nkiss\nmemory\nmoney\nnature\nnight\nsun\ntrust''')
print("\n")
print("Enter keywords")
print("\n")

#taking input from user and storing it into a list
inputkeywords = input().split()

#taking number of characters from user
lineinpoem = int(input("enter how many lines you want in you poem\n"))
#finding length of list
n=inputkeywords.__len__()
lineinpoem = lineinpoem//n + 1
#runnning a loop upto the last index of list and checking weather the input given by the user is present in list or not
#if input keyword is present in present in list  then opening the file of that keyword and reading its content line by line

for i in range(len(inputkeywords)):

    if inputkeywords[i] == "alone":
        with open("alone.txt","r") as fp1:
            counter = 0
            for line in fp1:
                print(line)
                counter += 1
                if counter == lineinpoem: break



    elif inputkeywords[i] == "crazy":
        with open("crazy.txt","r") as fp2:
            counter = 0
            for line in fp2:
                print(line)
                counter += 1
                if counter == lineinpoem: break



    elif inputkeywords[i] == "dream":
        with open("dream.txt", "r") as fp3:
            counter = 0
            for line in fp3:
                print(line)
                counter += 1
                if counter == lineinpoem: break


    elif inputkeywords[i] == "friend":
        with open("friend.txt", "r") as fp4:
            counter = 0
            for line in fp4:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "future":
        with open("future.txt", "r") as fp5 :
            counter = 0
            for line in fp5:
                print(line)
                counter += 1
                if counter == lineinpoem: break


    elif inputkeywords[i] == "girl":
        with open("girl.txt", "r") as fp6:
            counter = 0
            for line in fp6:
                print(line)
                counter += 1
                if counter == lineinpoem: break


    elif inputkeywords[i] == "hope":
        with open("hope.txt", "r") as fp7:
            counter = 0
            for line in fp7:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "joy":
        with open("joy.txt", "r") as fp8:
            counter = 0
            for line in fp8:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "kiss":
        with open("kiss.txt", "r") as fp9:
            counter = 0
            for line in fp9:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "memory":
        with open("memory.txt", "r") as fp10:
            counter = 0
            for line in fp10:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "money":
        with open("money.txt", "r") as fp11:
            counter = 0
            for line in fp11:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "nature":
        with open("nature.txt", "r") as fp12:
            counter = 0
            for line in fp12:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "night":
        with open("night.txt", "r") as fp13:
            counter = 0
            for line in fp13:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "sun":
        with open("sun.txt", "r") as fp14:
            counter = 0
            for line in fp14:
                print(line)
                counter += 1
                if counter == lineinpoem: break

    elif inputkeywords[i] == "trust":
        with open("trust.txt", "r") as fp15:
            counter = 0
            for line in fp15:
                print(line)
                counter += 1
                if counter == lineinpoem: break
    else :
        print("ERROR KEYWORD NOT FOUND")

















