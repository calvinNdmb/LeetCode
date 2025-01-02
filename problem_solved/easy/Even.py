import time
start_time = time.time()

def problem_function(num):
    even=True
    for i in range(num):
        if even:
            even=False
        else:
            even=True
    return even


num=100000003
if __name__ ==  '__main__':
    print(problem_function(num))

    end_time = time.time()
    print(f"elapsed:{end_time-start_time:.6f}")
