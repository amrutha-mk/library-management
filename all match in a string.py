import re
s="India is an asian country"
l=re.findall("ia",s)
print(l)
m=re.sub("\s"," ",s)
print(m)