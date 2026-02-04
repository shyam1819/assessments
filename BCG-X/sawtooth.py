def solution(arr):
    if not arr:
        return 0
    total_sawtooth_count = 1
    current_streak = 1
    
    for i in range(1,len(arr)):
        if arr[i]%2 != arr[i-1]%2:
            current_streak+=1
        else:
            current_streak = 1
        total_sawtooth_count += current_streak
        
    return total_sawtooth_count


if __name__ == "__main__":
    arr = [1,3,5,7,9]
    result = solution(arr)
    print(result)
    
