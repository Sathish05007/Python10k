for i in range(1,15):
    # print(i) # it print 1 to 9
    if(i==9):
        break
    print(i) # ir prints 1 to 8


for i in range(1,14):
    # print(i) 
    if(1==10):
        continue
    print(i) 

for i in range(1,10):
    if(i==5):
        continue
    i+=1
    print(i)

stops=["kphb","srnagar","ameerpet","pground","paeasdie","sec"]
for stop in stops:
    if(stop=="srnagar"):
     print(stop)