import subprocess
import psutil
def name():
    data = subprocess.check_output("lscpu", shell=True, text=True)
    split_data=data.split("\n")
    words = split_data[7].split()[-7:]
    CPU_name = ' '.join(words)
    return CPU_name
def Use_rate():
    cpu = psutil.cpu_percent(interval=1)
    return cpu

print(Use_rate())