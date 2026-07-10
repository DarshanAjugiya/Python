s="DARSHAN AJUGIYA"
print(s[0])
print(s[4])
print(s[-3])
print(s[-5])
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])

s="DARSHAN"
for char in s:
    print(char)

s="dARSHAN"
s="D"+s[1:]
print(s)

s="DARSH"
del s
#print(s)

s="DARSH AN"
s1="K"+s[1:]
s2=s.replace("DARSH","darsh")
print(s1)
print(s2)

s="Ajugiya"
print(len(s))

s="Battle Through The Heavens"
print(s.upper())
print(s.lower())

s="  Welcome To My Domain  "
print(s.strip())

s="Game Of Thrones"
print(s.replace("Thrones","Hunting"))

s1="Battle Through"
s2="The Heavens"
print(s1+" "+s2)

s="Welcome  "
print(s  *3)      




