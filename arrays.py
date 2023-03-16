################LARGEST 3 ELEMENTS IN AN ARRAY#############
#APPROACH-1
#time complexity: O(n^2)
#space complexity:O(1)
arr=[10, 4, 3, 50, 23, 90]
n=len(arr)
#selection sort but can also use quick or merge sort as their time complexities are better
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            swap=arr[i]
            arr[i]=arr[j]
            arr[j]=swap
print(arr[n-1:n-4:-1])

#APPROACH-2
#time complexity:O(n)
#space complexity:O(1)
arr=[10, 4, 3, 50, 23, 90]
n=len(arr)
first,second,third=0,0,0
if n<3:
    print("Invalid ouput")
else:
    for i in range(0,n):
        if(arr[i]>first):
            third=second
            second=first
            first=arr[i]
        elif(arr[i]>second and arr[i]!=first):
            third=second
            second=arr[i]
        elif(arr[i]>third and arr[i]!=second and arr[i]!=first):
            third=arr[i]
print(first,second,third)



#########################2nd LARGEST ELEMENT IN THE ARRAY##############
#APPROACH-1
#time complexity: according to the sorting algorithm u taken
#space complexity: according to the sorting algorithm u taken
# As I took selection sort------time complexity:O(n^2)
#                               Space Complexity:O(1)
arr=[12, 35, 1, 10, 34, 1]
n=len(arr)
#selection sort but can also use quick or merge sort as their time complexities are better
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            swap=arr[i]
            arr[i]=arr[j]
            arr[j]=swap
print(arr[-2])

#APPROACH-2
#Time complexity: O(n)
#space Complexity:O(1)
arr=[12, 35, 1, 10, 34, 1]
n=len(arr)
if (n < 2):
    print(" Invalid Input ")
first ,second=0,0 
for i in range(0,n):
    first=max(first,arr[i])
for i in range(0,n):
    if arr[i]!=first:
        second= max(second,arr[i])
print(second)

#APPROACH:3
#Time Complexity:O(n)
#SC:O(1)
arr=[12, 35, 1, 10, 34, 1]
n=len(arr)
if (n< 2):
    print(" Invalid Input ");
first,second=0,0 
for i in range(0,n):
    if arr[i]>first:
        second=first
        first=arr[i]
    if arr[i]>second and arr[i]!=first:
        second=arr[i]
print(second)



################MOVE ALL 0'S TO END OF THE ARRAY####################
#APPROACH-1
#tc: O(N)
#SC: O(n)
arr=[1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
li1=[]
li2=[]
n=len(arr)
for i in range(n):
    if arr[i]==0:
        li1.append(arr[i])
    else:
        li2.append(arr[i])
print(li2+li1)

#APPROACH 2:
#tc: O(N^2)
#SC: O(1)
arr=[1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
n=len(arr)
count=0
for i in range(n):
    if arr[i]==0:
        count+=1
for i in range(count):
    for i in range(n-1):
        if arr[i]==0 and arr[i+1]!=0:
            swap=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=swap
print(arr)  



