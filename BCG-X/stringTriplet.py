def solution(string):
    n = len(string)
    if n < 2:
        return -1
    i,j = 0, 2
    count=0
    while j<n:
        if string[i].lower()==string[j].lower():
            count+=1
        i+=1
        j+=1
    return count

if __name__ == "__main__":
    print(solution("axAxjBhTHRh"))
