import os

def print_mem(msg):
    print(msg)
    with open("/proc/" + str(os.getpid()) + "/status") as status:
        for line in status:
            if "VmRSS" in line:
                print("  " + line.strip())
            if "VmHWM" in line:
                print("  " + line.strip())
