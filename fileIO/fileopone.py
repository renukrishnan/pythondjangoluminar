#read
#write
#append
#step 1: we have to create reference
#f=open("filepath","mode of operation")

f=open("demo","r")
for lines in f:
    print(lines)

#when i want to store this words in list
f=open("demo","r")
words=[]
for lines in f:
    words.append(lines.rstrip("\n").split(" "))
print(words)
mywords=[]
for lst in words:
    for wrd in lst:
        mywords.append(wrd)
print(mywords)

#assesment questions
# print students who pass by combining student anf fail file: set
# print highest repeating word from the file demo:dict




