pattern="ABABBAC"
#find the first recursive character, here it is A(A is the first repeating character in this string
dict={}
for ch in pattern:# A B A ..
    if ch not in dict:# a is not in dict then increment value
        dict[ch]=1
    else:
        print(ch,"is the first recursive character")
        break