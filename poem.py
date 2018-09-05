import sys

''' This programme will take keywords as input from user and will display poem relaed to their input keywords  '''

print("poems of your favorite words")
name = input("enter your name")
print("dear" , name , "you have to choose from following keywords")
print('''keywords\nalone\ncrazy\ndream\nfriend\nfuture\ngirl\nhope\njoy\nkiss\nmemory\nmoney\nnature\nnight\nsun\ntrust''')
print("Enter keywords")

#taking input from user and storing it into a list
inputkeywords = input().split()

#taking number of characters from user
charinpoem = int(input("enter how many characters you want in you poem"))
charinpoem //= 2;
#finding length of list
n=inputkeywords.__len__()

#runnning a loop upto the last index of list and checking weather the input given by the user is present in list or not
#if input keyword is present in present in list  then opening the file of that keyword and reading its content

for i in range(len(inputkeywords)):
    if inputkeywords[i] == "alone":
       with open("alone.txt","r") as fp1:
           #reeading the contents of file from o to range of characters given  by user
           content1 = fp1.read(charinpoem - 0)
           print(content1)

    elif inputkeywords[i] == "crazy":
        with open("crazy.txt","r") as fp2:
            content2 = fp2.read(charinpoem - 0)
            print(content2)

    elif inputkeywords[i] == "dream":
        with open("dream.txt", "r") as fp3:
            content3 = fp3.read(charinpoem - 0)
            print(content3)

    elif inputkeywords[i] == "friend":
        with open("friend.txt", "r") as fp4:
            content4 = fp4.read(charinpoem - 0)
            print(content4)

    elif inputkeywords[i] == "future":
        with open("future.txt", "r") as fp5 :
            content5 = fp5.read(charinpoem - 0)
            print(content5)

    elif inputkeywords[i] == "girl":
        with open("girl.txt", "r") as fp6:
            content6 = fp6.read(charinpoem - 0)
            print(content6)


    elif inputkeywords[i] == "hope":
        with open("hope.txt", "r") as fp7:
            content7 = fp7.read(charinpoem - 0)
            print(content7)

    elif inputkeywords[i] == "joy":
        with open("joy.txt", "r") as fp8:
            content8 = fp8.read(charinpoem - 0)
            print(content8)

    elif inputkeywords[i] == "kiss":
        with open("kiss.txt", "r") as fp9:
            content9 = fp9.read(charinpoem - 0)
            print(content9)

    elif inputkeywords[i] == "memory":
        with open("memory.txt", "r") as fp10:
            content10 = fp10.read(charinpoem - 0)
            print(content10)

    elif inputkeywords[i] == "money":
        with open("money.txt", "r") as fp11:
            content11 = fp11.read(charinpoem - 0)
            print(content11)

    elif inputkeywords[i] == "nature":
        with open("nature.txt", "r") as fp12:
            content12 = fp12.read(charinpoem - 0)
            print(content12)

    elif inputkeywords[i] == "night":
        with open("night.txt", "r") as fp13:
            content13 = fp13.read(charinpoem - 0)
            print(content13)

    elif inputkeywords[i] == "sun":
        with open("sun.txt", "r") as fp14:
            content14 = fp14.read(charinpoem - 0)
            print(content14)

    elif inputkeywords[i] == "trust":
        with open("trust.txt", "r") as fp15:
            content15 = fp15.read(charinpoem - 0)
            print(content15)
    else:
        print("KEYWORD NOT FOUND")
















