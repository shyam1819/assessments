def solution(t,capacity,recharge):
    n = len(capacity)
    available_at = [0]*n
    current_time = 0
    batteries_used = 0
    current_idx = 0
    while current_time < t:
        found_battery = False
        for _ in range(n):
            if available_at[current_idx] <= current_time:
                time_needed = t - current_time
                time_provided = capacity[current_idx]
                actual_use = min(time_needed,time_provided)
                available_at[current_idx] = current_time+actual_use+recharge[current_idx]
                current_time+=actual_use
                if time_needed > actual_use:
                    batteries_used+=1
                current_idx = (current_idx+1)%n
                found_battery = True
                break
            else:
                current_idx = (current_idx+1)%n
                
        if not found_battery:
            return -1
            
    return batteries_used
                


if __name__ == "__main__":
    t = 16
    capacity = [1,5,7,4]
    recharge = [2,1,3,7]
    num_batteries = solution(t,capacity,recharge)
    print(num_batteries)
    t=10
    capacity = [100]
    recharge = [1]
    num_batteries = solution(t,capacity,recharge)
    print(num_batteries)
