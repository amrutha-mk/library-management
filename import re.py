import re
S="The country is spain"
x=re.search("^The.*spain$",S)
if x:
    print('Match Found')
else:
    print('Match not found')
