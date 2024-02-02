import shutil
total, used, free = shutil.disk_usage('/')
print(f'Total: {total / (2**30)} GiB')
print(f'Used: {used / (2**30)} GiB')
print(f'Free: {free / (2**30)} GiB')
def Value():
    total, used, free = shutil.disk_usage('/')
    return total / (2**30)
def useing_value():
    total, used, free = shutil.disk_usage('/')
    return used / (2**30)