from collections import Counter

filename = '.\input.txt'  

with open(filename) as fn:  

# Read each line
   ln = fn.readline()

# Keep count of lines
   lncnt = 1
   while ln:
       print("Line {}: {}".format(lncnt, ln.strip()))
       ln = fn.readline()
       lncnt += 1

#Counting Word Frequency
with open(r'pathinput2.txt') as f:
               p = Counter(f.read().split())
               print(p)