st1={10,20,30,40}
st2={30,40,50,60,70,80}

#union set
#10 20 30 40 50 60 70 80
unset=st1.union(st2)
print(unset)

#intersection(common values)
inter=st1.intersection(st2)
print(inter)

#difference (st1 -st2)
diff=st1.difference(st2)
print(diff)
#10,20

#assesment

students=["name1","name2","name3"]
fail=["name1","nqme2"]
pass=?