import time
start_time = time.time()
liste=[1,1,1,2,2,3]
k=2
def problem_function(liste,k):
    dic={}
    for i in liste:
        if i in dic:
            dic[i].append(i)
        else:
            dic[i]=[i]
    return [i[0] for i in sorted (list(dic.values()), key=len, reverse=True)[:k]]

if __name__ ==  '__main__':
    print(problem_function(liste,k))

    end_time = time.time()
    print(f"elapsed:{end_time-start_time:.6f}")
