import time
start_time = time.time()
strings=["test","sett","ttse","USA","ASU","a"]

def problem_function(strings):
    dic={}
    for i in strings:
        a="".join(sorted(i))
        if a in dic.keys():
            dic[a].append(i)
        else:
            dic[a]=[i]
    return list(dic.values())


if __name__ ==  '__main__':
    print(problem_function(strings))
    end_time = time.time()
    print(f"elapsed:{end_time-start_time:.6f}")
