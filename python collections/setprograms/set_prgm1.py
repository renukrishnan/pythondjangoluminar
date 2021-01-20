#how to define s set
#st={}  # empty curly braces will be taken as dictionary, if you want to create an empty set, you have to use set()
#print(type(st))

st=set()
st={10,11,12,"hello",13,13}
print(type(st))
print(st)
# insertion ordee is preserved or not? not preserved
#indexing is not possible, st[0] like this is not possible ,because insertion order is not preserved

#updation is possible only with othet set
st2={50,60}
st.update(st2)
print(st)

#dulpicates are not allowed
