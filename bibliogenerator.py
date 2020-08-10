a=[]
#put links in a

def generate(lis):
  b=[]
  for i in lis:
    b.append(f"<li><a href='{i}'>{i}</a></li>")
  return(b)

c=generate(a)

for i in c:
  print(i)