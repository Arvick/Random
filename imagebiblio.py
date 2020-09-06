linklist=[]
with open('links.txt', 'r') as links:
    for line in links.readlines():
        linklist.append(line)

master=[]
def formt():
    for i in linklist:
        alt=input(f'''Current Link: {i}. What is the alternate text? 
                  ''')
        master.append(f"<li><a href='{i}'> {alt}</a></li>")

formt()

for i in master:
    print(i)

        