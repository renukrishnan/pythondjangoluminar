#string is a sequence of characters
# how we can represent it in python

name="TTluminar TechnolabTT"
print(name)#'' single quotes can also used to represent string
print(name[0])

#""" is used to represent more lines or sentense to print
name1=""" luminar technolab
            kakkanad
            kochi"""
print(name1)

# to split words,use split method
nam="luminar technolab software training Institute"
words=nam.split(" ")
print(words)

# convert string into uppercase
print(name.upper())

#convert string into lowerecase
print(name.lower())

#to remove character from begining
name=name.lstrip("TT")
print("name=",name)

#to remove character from end
name=name.rstrip("TT")
print("name=",name)

