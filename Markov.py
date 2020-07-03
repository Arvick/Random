import random
forbidden=[",",":",";","?","!","/","&","#","@",".",'"',"_","(",")","-","“","”","-","[","]","'","’",'‘']
prime=[]
with open('y.txt',encoding='utf-8') as obj:
    temp=obj.readlines()
    for i in temp:
        prime.append(i.strip())
    prime=[i for i in prime if i!='']

for char in forbidden:
    while char in "".join(prime):
        temple=[]
        for i in prime:
            temp=[letter for letter in i]
            for n in temp:
                if n in forbidden:
                    temp.remove(n)
            temple.append("".join(temp))
        prime=temple

sent={}
for i in prime:
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
for i in prime:
    a=i.lower().split()
    if a!=[]:
        if a[-1] not in sent.keys():
            sent[a[-1]]={random.choice(list(sent.keys())):1}

        

def generate(num,dicti):
    tem=[]
    keys=list(dicti.keys())
    values=list(dicti.values())
    tem.append(random.choice(keys))
    while len(tem)<num:
      if tem[-1] not in keys:
        tem.append(random.choice(keys))
      else:
        valuedict=dicti[tem[-1]]
        templist=[]
        if len(valuedict.items())==1:
            tem.append(random.choice(list(dicti.keys())))
        else:
            for key,value in valuedict.items():
                count=0
                while count<value:
                    templist.append(key)
                    count+=1
            tem.append(random.choice(templist))
      if tem[-1]==tem[-2]:
        tem.append(random.choice(keys))
      keys=list(dicti[tem[-1]].keys())
    return(" ".join(tem))

      

for i in range(1,11):
    print(generate(random.randrange(10,20),sent),"\n")
#for key,value in sent.items():
#    print((key,value),"\n")