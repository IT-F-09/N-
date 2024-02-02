import psutil
def bytes_to_gb(bytes_size):
    gb_size = str(bytes_size / (1024**3))
    split_size=gb_size.split(".")
    gb_size = split_size[0] + "." + split_size[1][0]
    return gb_size

def Value():
    # メモリの使用状況を取得
    memory_info = psutil.virtual_memory()
    return bytes_to_gb(memory_info.total)
def Use_rate():
    memory_info = psutil.virtual_memory()
    return memory_info.percent
def useing_value():
    memory_info = psutil.virtual_memory()
    return bytes_to_gb(memory_info.used)

print(Value())