import time

# time.sleep(3)
# print("Hello Pranjal!!");

# my_time = int(input("Enter the Seconds: "));
# for x in reversed(range(0 , my_time)):
#     print(x)
#     time.sleep(3)
#     print("Yups! Time Up");

# for x in range(my_time , 0 , -1):
#    seconds = x % 60
#    minutes = int(x/60)%60
#    hours = int(x/3600)
#    print(f"{hours:02}:{minutes:02}:{seconds:02}");
#    time.sleep(1)# har ke sec ke liye code rokta hai 
# print("yups Time Up!");

times = int(input("Enter the Seconds : "))
for x in range(times , 0 , -1):
     hours = int(x / 3600);
     minutes = int(x/60)%60;
     seconds = x % 60;
     print(f"{hours:02}:{minutes:02}:{seconds:02}");
     time.sleep(1)
print("Yups times Up!!")
