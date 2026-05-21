
def daily_tempreture(temps):
    n=len(temps)
    output=[0]*n #output[] len=len(temps) n
    stack_days=[]
    for i in range(n):
        while len(stack_days)>0 and temps[i] > temps[stack_days[-1]] :
            index=stack_days.pop()
            output[index]=i-index
        stack_days.append(i)
    return output

print(daily_tempreture([22,18,28,32,26,20,23]))