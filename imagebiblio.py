linklist=[]
#appends each link to be used
with open('links.txt', 'r') as links:
    for line in links.readlines():
        linklist.append(line)

#formats and appends links to master
master=[]
def formt():
    for i in linklist:
        alt=input(f'''Current Link: {i}. What is the alternate text? 
        ''')
        master.append(f"<li><a href='{i}'> {alt}</a></li>")

formt()

#prints out each entry
for i in master:
    print(i)

#clears text file
with open('links.txt', 'w') as links:
    links.close

        