expenses={"jan20":30000,"feb20":25000,"march20":30000,"april20":24000,"may20":22000}
print(expenses["march20"])

#value stored in dict in the form of key value pair
#how do we fetch value from dictionary--> using key value
# is it possible to store duplicate key, no -->key must be unique,
# chcek whether key is there, check for jun key
print("jun20" in expenses)#false
print("march20" in expenses)#true

# adding new key value pair
expenses["june20"]=25000
print(expenses)

