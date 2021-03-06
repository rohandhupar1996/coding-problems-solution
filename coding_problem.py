from collections import defaultdict
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        new_list=defaultdict(list)
        a=['e' if i%2==0 else 'o' for i in A]
        for i , j in zip(a,A):
            new_list[i].append(j)
        
        b=new_list['o']
        c=new_list['e']
        
        for i in b:
            c.append(i)
        return c

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic={}
        a=sorted(nums)
        for i , j in enumerate(a):
            if j not in dic:
                dic[j]=i
        return [ dic[n] for n in nums]

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start=len(nums)
        end=0
        if nums==sorted(nums):
            return 0
        else:
            for i in range(0,len(nums)-1):
                for j in range(i+1,len(nums)):
                    if nums[i]>nums[j]:
                        start=min(start,i)
                        end=max(end,j)
            return((end-start+1))
a = list(map(int, input().rstrip().split()))
leaders=[]
for i in range(len(a)-1):
    first=a[i]
    max_ele=max(a[i+1:])
    if first > max_ele:
        leaders.append(a[i])
leaders.append(a[-1])

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        for i in range(len(nums)):
            if target in nums:
                return nums.index(target)
            else : 
                return -1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=nums
        low=0
        high=len(arr)-1
        mid=0
        while(mid<=high):
            if(arr[mid]==0):
                arr[mid],arr[low]=arr[low],arr[mid]
                low+=1
                mid+=1
            elif(arr[mid]==1):
                mid+=1
            else:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
        nums=arr
        return nums
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        
        ### every local inversion is global inversion 
        ### using a concept where you can find minmum and take whole left 
        ### values from minimum won't work because if case comes like 0,2,1
        ### then concept will fail 
        
        ### every local inversion is gobal inversion but vice and versa is not true
        
        for i ,j in enumerate(A):
            if abs(i-j)>1:
                return False
        return True
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        count=0
        for i in range(1,len(nums)-1):
            if nums[i]>min(nums[:i]) and nums[i]<max(nums[i+1:]):
                count+=1
                
        if count>=1:
            return True
        else :
            return False
def removeX(string):
    if len(string)==0:
        return string 
    smallstring=removeX(string[1:])
    
    if string[0]=="x":
        return smallstring    
    else :
        return string[0]+smallstring 

# Main
string = input()
print(removeX(string))
def mergeSort(arr):
    if len(arr)>1:
        mid_value=len(arr)//2
        left=arr[:mid_value]
        right=arr[mid_value:]
        left=mergeSort(left)
        right=mergeSort(right)
        
        arr=[]
        
        while len(left)>0 and len(right)>0:
            if left[0]<right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)
                
        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)
    return arr 

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
arr=mergeSort(arr)
print(*arr)

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        
        
        
        

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0,len(arr)-1)
print(*arr)

def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n==0:
        return
    elif n==1:
        print(source,dest)
    else:
        towerofhanoi(n-1,source,dest,aux)
        print(source,dest)
        towerofhanoi(n-1,aux,source,dest)
        
        
        

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')
def palindrome_check(s,si,ei):
    if si<=ei:
        if len(s)==0:
            return 'false'
        if len(s)==1:
            return 'true'
        elif s[si]==s[ei]:
            return palindrome_check(s,si+1,ei-1)
        else:
            return 'false'
    return 'true'

## Read input as specified in the question.
## Print output as specified in the question.


def geometric_sum(n):
    if n==0:
        return 1
        
    return (1/2**(n)+geometric_sum(n-1))



n=float(input())
geo_sum=geometric_sum(n)
print("{0:.5f}".format(geo_sum))
## Read input as specified in the question.
## Print output as specified in the question.
def multi_rec(m,n):
    if m==0 or n==0:
        return 0
    if m==1 :
        return n
    elif n==1:
        return m 
    elif m>n:
        return m+multi_rec(m,n-1)
    else:
        return n+multi_rec(n,m-1)



m=int(input())
n=int(input())
ans=multi_rec(m,n)
print(ans) 

def pairstar(string):
    if len(string)==1:
        return string
    elif string[0]==string[1]:
        return "".join(string[0]+"*"+pairstar(string[1:]))
    else:
        return "".join(string[0]+pairstar(string[1:]))



string=input()
answer=pairstar(string)
print(answer)
def checkab(string):
    if len(string)==0:
        return "true"
    if string[0]=="a":
        if len(string[1:])>1 and string[1:3]=="bb":
            return checkab(string[3:])
        else:
            return checkab(string[1:])

    return "false" 



string=input()
answer=checkab(string)
print(answer)


stepsarray=[1,2,4]
def fibsteps(n):
    if n<=len(stepsarray):
        return stepsarray[n-1]
    else:
        steps=fibsteps(n-3)+fibsteps(n-1)+fibsteps(n-2)
        stepsarray.append(steps)
        return steps

n=int(input())
answer=fibsteps(n)
print(answer)

## Read input as specified in the question.
## Print output as specified in the question.

### dynamic programming solution
stepsarray=[1,2,4]
def fibsteps(n):
    if n<=len(stepsarray):
        return stepsarray[n-1]
    else:
        steps=fibsteps(n-3)+fibsteps(n-1)+fibsteps(n-2)
        stepsarray.append(steps)
        return steps

n=int(input())

answer=fibsteps(n)
print(answer) 

def equilibriumIndex(arr):
    # Please add your code here
    if len(arr)==1:
        return 0
    elif len(arr)==2:
        return -1
    left=0
    right=sum(arr[1:])
    for i in range(len(arr)):
        if i<len(arr):
            if left==right:
                return i
                break
            elif left!=right:
                right=right-arr[i+1]
                left=left+arr[i]
        else:
            return -1
            break
        

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))

def intersection(arr1, arr2):
    hs=dict((x,arr1.count(x)) for x in set(arr1))
    for j in range(len(arr2)):
        if arr2[j] in hs:
            if hs[arr2[j]]!=0:
                print(arr2[j])
                hs[arr2[j]]-=1

            

# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
arr1.sort()
arr2.sort()
intersection(arr1, arr2) 

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNode(head, pos) :
    count=0
    prev=None
    curr=head
    
    if pos==0:
        head=head.next
        curr=None
        return head

    while count < pos :
        prev=curr
        if curr.next is None:
            break 
        curr=curr.next
        count+=1
    prev.next=curr.next
    curr.next=None
    return head
        

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteRec(head, i):
    #  a linked list and a position i, delete the node of ith position from
    # Linked List recursively. If position i is greater than length of LL,
    # then:
    # you should return the same LL without any change.
    #############################
    if head is None:
        return None 
    if i==0:
        head=head.next
        return head
    smallhead=deleteRec(head.next,i-1)
    head.next=smallhead
    return head
    
    
    #############################
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = deleteRec(l, i)
printll(l)


from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def reversell(head):
    if head is None:
        return
    reversell(head.next)
    
def lenll(head):
    count=0
    while head is not None:
        head=head.next
        count+=1
    return count

def reversell(head1):
    prev = None
    current = head1
    while(current is not None): 
        next = current.next
        current.next = prev 
        prev = current 
        current = next
        head1 = prev
    return head1
        
def isPalindrome(head):
    curr=head
    head1=head
    len=lenll(head)
    if len == 0 or len==1:
        return True
    else:
        if len%2==0:
            mid=len//2
            count=0
            while count<mid:
                curr=curr.next
                head1=head1.next
                count+=1
            curr.next=None
            head1=reversell(head1)
            while head1 is not None and head is not None:
                if head1.data==head.data:
                    head1=head1.next
                    head=head.next
                    return True
                else :
                    return False
        else:
            mid=len//2
            count=0
            while count<mid:
                curr=curr.next
                head1=head1.next
                count+=1
            head1=head1.next
            curr.next=None
            head1=reversell(head1)
            while head1 is not None and head is not None:
                if head1.data==head.data:
                    head1=head1.next
                    head=head.next
                    return True
                else :
                    return False
            

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1   