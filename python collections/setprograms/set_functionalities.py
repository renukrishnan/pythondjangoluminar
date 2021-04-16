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

students={"renu","sanoj","vedant","Rahul","veena"}
fail={"renu","veena"}
#pass=?
pas=students.difference(fail)
print(pas)