x=int(input("How many lines?"))


a=[]
#put links in a
def quote(num):
  temp=0
  while temp<x:
    y=input("Enter line here: ")
    a.append(str(y))
    temp+=1
  return("Finished.")

quote(x)

def generate(lis):
  b=[]
  for i in lis:
    b.append(f"<li><a href='{i}'>{i}</a></li>")
  return(b)


c=generate(a)

for i in c:
  print(i)