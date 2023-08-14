# dont know how but i did this in first attempt :')


arr1=[4,3,7,5,6,1,8,15,11]

def partition(arr):
    pivot=arr[0]
    start=1
    end=len(arr)-1
    while start<=end:
        if arr[start]>pivot and arr[end]<pivot:
            arr[start], arr[end]=arr[end], arr[start]
            start+=1
            end-=1
        elif arr[start]<pivot:
            start+=1
        if arr[end]>pivot:
            end-=1
    arr[0], arr[end]=arr[end], arr[0]
    return end

            

def sortArr(arr):
    if len(arr)>1:
        part_index=partition(arr)   
        sortArr(arr[:part_index])
        sortArr(arr[part_index+1:]) 

print('before quick sorting:', arr1)
sortArr(arr1)
print('after quick sorting:',arr1)