def access(*args):
    def wrap(func):
        # print(args)
        for i in args:
            if i=="admin":
                func()
                print("admin has permission")
            else:
                func()
                print("not allowed")
    return wrap
# list=["admin", "ronak"]
@access("admin")
def increment():
    print("access by admin")

user=["ronak","tejas","abhijeet"]
@access(user)
def addEmp():
    print("access by user")


# calculating time of a function using decorators
# import time

# def calculate_time(func):
#     def wrapper_timer(*args, **kwargs):
#         begin=time.time()
#         start=time.perf_counter()
#         value=func(*args, **kwargs)
#         last=time.time()
#         end=time.perf_counter()
#         runTime=last-begin
#         totalTime=end-start
#         print(f"finished in {runTime:.6f} secs (time.time())")
#         print(f"finished in {totalTime:.6f} secs (time.perf_counter())")
#         return value
#     return wrapper_timer

# @calculate_time
# def printTop10(num):
#     time.sleep(2)
#     sum=0
#     for i in range(num):
#         sum+=num

# printTop10(100000)
