prime=[]
forbidden=["'",",",":",";","?","!","-","/","&","#","@","*","."]
with open('x.txt') as obj:
    for string in obj.readlines():
        prime.append(string[:-2])
newp=[]
for i in prime:
    temp=[letter for letter in i]
    for n in temp:
        if n in forbidden:
            temp.remove(n)
    newp.append("".join(temp))
test="The quick brown fox jumps over the lazy dog"
b=[i for i in test]
sent={}
for i in newp:
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
for key,value in sent.items():
    print(key,value)