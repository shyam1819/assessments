def solution(arr):
    """
    1. Find the non zero number from left called 'x'.
    2. Subtract the rest of the numbers to the right with 'x'.
        a. If the number is less than 'x' stop and jump to 3rd step.
        b. If there are no non zero numbers jump to 3rd step.
    3. Add 'x' to the sum.
    4. Start with the next non zero number from left.
    """
    n = len(arr)
    res = 0
    while True:
        i = -1
        for idx in range(n):
            if arr[idx]!=0:
                i = idx
                break
        if i== -1:
            break
        curr = arr[i]
        for j in range(i,n):
            if arr[j]<curr:
                break
            arr[j]-=curr
        res+=curr
        print(arr,res)
    return res
        
    

if __name__ == "__main__":
    print(solution([2,1,3,4,5,7]))
