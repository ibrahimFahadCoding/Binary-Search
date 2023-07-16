# main.py

def binary_search(l,v):
  
  low = 0
  high = len(l) - 1
  while low <= high:
    i = l[(low+high)//2] 
    if v > i:
      low = ((low + high)//2) + 1
    elif v < i:
      high = ((low + high)//2) - 1
    else:
      return True
  return False
  
#O(log(N))  
  
def binary_search2(alist,key):
    end = len(alist) - 1
    if end < 0:
        return -1
 
    mid = (end)//2
    if alist[mid] < key:
        return binary_search2(alist[mid+1:], key)
    elif alist[mid] > key:
        return binary_search2(alist[:mid], key) 
    else:
        return mid
 
 


listtocheck = []
whattoadd = ""
while whattoadd != "q":
  whattoadd = input("Enter a number: ")
  if whattoadd == "q":
    target_value = int(input("Enter a value: "))
    print(binary_search(listtocheck, target_value)) 
  else:
    listtocheck.append(int(whattoadd))
    

alist = [int(x) for x in listtocheck]

 
index = binary_search2(listtocheck,target_value)
if index < 0:
  print("False")
else:
  print("True")

    

  
 

      


