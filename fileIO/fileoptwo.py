# print students who pass by combining student anf fail file: set
f=open("students","r")
f1=open("fail","r")
st=set()
st2=set()
for nam in f:
    st.add(nam)
for name in f1:
    st2.add(name)
result=st.intersection(st2)
print(result)
