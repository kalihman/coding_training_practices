import copy

def solution(N):
    cnt = 0
    maxcnt = 0
    binary_int = format(N, 'b')
    #print(binary_int)
    for ind, i in enumerate(binary_int):
        #print("Index: %d"%(ind))
        if ind > 0:
           #print(i)
           if i == "0":
               cnt=cnt+1
               #print(cnt)
           else:
               #print("!")
               if(cnt > maxcnt):
                   maxcnt=copy.deepcopy(cnt)
               cnt=0
    return maxcnt

#for i in range(0,34):
#    print("Input: %d, Output: %d"%(i, solution(i)))
print(solution(1041))
