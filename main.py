from queue import Queue
import random
#FCFS
x = int(input("Enter number of processes: "))
d = dict()


for i in range(x):
   key = "p"+str(i+1)
   a = random.randint(0,25)
   print("Arrival time of process: " + str(a))
   b = random.randint(0,25)
   print("Burst time of process: " + str(b))
   l = []
   l.append(a)
   l.append(b)
   d[key] = l




''' generowanie losowych wartości dla algorytmów FIFO i LRU
x = int(input('Enter number of elements: '))
pages = []
for i in range(x):
   a = random.randint(0, 9)
   pages.append(a)
'''


def FCFS(d):




   d = sorted(d.items(), key=lambda item: item[1][0])


   ET = []
   for i in range(len(d)):
       if i == 0:
           ET.append(d[i][1][1])
       else:
           ET.append(ET[i-1] + d[i][1][1])


   TAT = []
   for i in range(len(d)):
       TAT.append(ET[i] - d[i][1][0])


   WT = []
   for i in range(len(d)):
       WT.append(TAT[i] - d[i][1][1])


   AVG_WT = 0
   for i in WT:
       AVG_WT += i
   AVG_WT = (AVG_WT/x)


   print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
   for i in range(x):
       print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
   print("Average Waiting Time: ",AVG_WT)




#FCFS()


def LCFS(d):


   d = sorted(d.items(), key=lambda item: item[1][0], reverse=True)


   ET = []
   for i in range(len(d)):
       if i == 0:
           ET.append(d[i][1][0] + d[i][1][1])
       else:
           ET.append(ET[i-1] + d[i][1][1])


   TAT = []
   for i in range(len(d)):
       TAT.append(ET[i] - d[i][1][0])


   WT = []
   for i in range(len(d)):
       WT.append(TAT[i] - d[i][1][1])


   AVG_WT = 0
   for i in WT:
       AVG_WT += i
   AVG_WT = (AVG_WT/x)


   print("Process | Arrival | Burst | Exit | Turn Around | Wait |")
   for i in range(x):
       print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
   print("Average Waiting Time: ",AVG_WT)




#algorytmy zastępwywania stron
#FIFO




def FIFO():
   def pageFaults(pages, n, capacity):
       print("Incoming \t pages")
       # Using Hashset to quickly check if a given
       # incoming stream item in set or not
       s = set()


       # Queue created to store pages in FIFO manner
       # since set will not store order or entry
       # we will use queue to note order of entry of incoming page
       indexes = Queue()


       page_faults = 0
       for i in range(n):


           # if set has lesser item than frames
           # i.e. set can hold more items
           if (len(s) < capacity):


               # If incoming item is not present, add to set
               if (pages[i] not in s):
                   s.add(pages[i])


                   # increment page fault
                   page_faults += 1


                   # Push the incoming page into the queue
                   indexes.put(pages[i])


           # If the set is full then we need to do page replacement
           # in FIFO manner that is remove first item from both
           # set and queue then insert incoming page
           else:


               # If incoming item is not present
               if (pages[i] not in s):
                   # remove the first page from the queue
                   val = indexes.queue[0]


                   indexes.get()


                   # Remove from set
                   s.remove(val)


                   # insert incoming page to set
                   s.add(pages[i])


                   # push incoming page to queue
                   indexes.put(pages[i])


                   # Increment page faults
                   page_faults += 1


           print(pages[i], end="\t\t")
           for q_item in indexes.queue:
               print(q_item, end="\t")


           print()
       return page_faults


   # Driver code
   #pages = [0,2,1,6,4,0,1,0,3,1,2,1]
   print(str(pages))
   n = len(pages)
   frames = 4
   page_faults = pageFaults(pages, n, frames)
   hits = n - page_faults


   print("\nPage Faults: " + str(page_faults))
   print("Hit: " + str(hits))






#LRU
def LRU():
   def pageFaults(pages,n, capacity):
       s = set()
       indexes = {}
       page_faults = 0
       for i in range(n):
           if len(s) < capacity:
               if pages[i] not in s:
                   s.add(pages[i])
                   page_faults += 1
               indexes[pages[i]] = i
           else:
               if pages[i] not in s:
                   lru = float('inf')
                   for page in s:
                       if indexes[page] < lru:
                           lru = indexes[page]
                           val = page


                   s.remove(val)
                   s.add(pages[i])
                   page_faults +=1
               indexes[pages[i]] = i


       return page_faults
   #pages = [1, 2, 1, 0, 3, 0, 4, 2, 4]
   n = len(pages)
   capacity = 4
   hits = n - pageFaults(pages,n,capacity)
   print("Page Faults: " + str(pageFaults(pages, n, capacity)))
   print("Hit: " + str(hits))






FCFS(d)
LCFS(d)
#FIFO()
#LRU()
