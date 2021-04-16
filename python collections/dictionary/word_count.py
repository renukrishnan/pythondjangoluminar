text="hai hello hai hello"
#outout hai=2, hello=2
#step1: slpit words by space and make it as a list.
words=text.split(" ")
#words=[hai,hello,hai,hello]
dict={}
#key   value
#hai    2
#hello  2
for word in words:# word=hai , hello
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)