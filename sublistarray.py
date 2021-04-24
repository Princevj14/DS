def Print(arr):
    B = [[]]
    
    for i in range(len(arr) + 1):
        
        for j in range(i+1,len(arr)+1):
            sub = arr[i:j]
            B.append(sub)
            
    return B       
            
arr = [1,2,3]
print("Sublist is ",Print(arr))