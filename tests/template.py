import time
start_time = time.time()

def problem_function():
    a=["a","b","c"]
    for i,n in enumerate(a):
        print(i,n)



if __name__ ==  '__main__':
    print(problem_function())

    end_time = time.time()
    print(f"elapsed:{end_time-start_time:.6f}")
