import threading

def jobs(name,num):
    print(name)
    print(num)

def theard():
    theards=[]
    job="test"
    for i in range(1,5):
        name=job+str(i)
        theards.append(
            threading.Thread(target=jobs,args=(name,i))
        )
    for t in theards:
         t.start()
    for t in theards:
        t.join()

theard()