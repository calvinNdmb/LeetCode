#easy_way
import time 

num = [i for i in range(100)]
target =150
print("prep over")
start_time= time.time()
def check(num,target):
    for i in range(len(num)):
        for j in num[i+1:]:
            if j>target:
                break
            if num[i]+j == target:
                return f"got it target:{target} = num[{i}] + num [{num.index(j)}]  ==> ({num[i]}+{j}) "


if __name__ == "__main__":
    print(check(num,target))
    end_time=time.time()
    print(f'run time: {end_time-start_time:.6f}')