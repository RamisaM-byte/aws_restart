print ("Here is my diary: \n")
f1 = open("Diary.txt","r")
print(f1.read())
f1.close()
print("\nNow let's create another diary !")
f2 = open("files/diary2.txt", "w")
f2.write ("Writing in my diary file!")
f2.close()

