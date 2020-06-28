import random
prime=[]
forbidden=[",",":",";","?","!","-","/","&","#","@","*",".",'"',"_","(",")","-","“","”","-"]
with open('x.txt',encoding="utf8") as obj:
    temp=obj.readlines()
    for i in temp:
        prime.append(i.strip())
    prime=[i for i in prime if i!='']
newp=[]
for i in prime:
    temp=[letter for letter in i]
    for n in temp:
        if n in forbidden:
            temp.remove(n)
    newp.append("".join(temp))
newp2=[]
for i in newp:
    temp=[letter for letter in i]
    for n in temp:
        if n in forbidden:
            temp.remove(n)
    newp2.append("".join(temp))
sent={}
for i in newp2:
    a=i.lower().split()
    count=0
    while count<len(a)-1:
        if a[count] not in sent.keys():
            sent[a[count]]={a[count+1]:1}
        else:
            if a[count+1] in sent[a[count]].keys():
                sent[a[count]][a[count+1]]+=1
            else:
                sent[a[count]][a[count+1]]=1
        count+=1
print(sent)