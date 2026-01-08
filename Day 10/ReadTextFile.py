gghg6uhh
njuu88m
.m..m


nmmu7jh
yyhhh ..mjjnyubh
ny77
hjjnm.kinu7uh


file=open('TEXT.txt','r')
f=file.readlines()
newlist=[]
for line in f:
    if line[-1]=='\n':
        newlist.append(line[:-1])
    else:
        newlist.append(line)
print(newlist)


new=[]
for line in f:
    new.append(line.strip())
print(new)
