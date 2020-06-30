import random
forbidden=[",",":",";","?","!","-","/","&","#","@","*",".",'"',"_","(",")","-","“","”","-","[","]"]
prime=[]
with open('x.txt') as obj:
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

def generate(num,dict):
    tem=[]
    keys=list(dict.keys())
    values=list(dict.values())
    tem.append(random.choice(keys))
    while len(tem)<num:
      if tem[-1] not in keys:
        tem.append(random.choice(keys))
      else:
        valuedict=dict[tem[-1]]
        tem.append(random.choice(list(valuedict.keys())))
      if tem[-1]==tem[-2]:
        tem.append(random.choice(keys))
    for i in tem:
      i.capitalize()
    return(" ".join(tem))

      


for i in range(1,41):
  print(generate(random.randrange(1,101),sent),"\n")
#for key,value in sent.items():
 # print(key,value)