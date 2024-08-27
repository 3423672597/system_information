import psutil
import platform
import os

def computer_hardware():
    system = platform.system()
    if system == "Windows":
        import subprocess
        os.system("color 0a")
        result = subprocess.run(["systeminfo"], capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Command failed with return code {result.returncode}")
    elif system == "Linux" or system == "Darwin":
        # 使用 psutil 获取硬件信息
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

        # 内存信息
        print("="*40, "Memory Information", "="*40)
        svmem = psutil.virtual_memory()
        print(f"Total: {svmem.total}")
        print(f"Available: {svmem.available}")
        print(f"Used: {svmem.used}")
        print(f"Percentage: {svmem.percent}%")

        # CPU信息
        print("="*40, "CPU Info", "="*40)
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # 打印每个核心的CPU使用率
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

        # 打印磁盘信息
        print("="*40, "Disk Information", "="*40)
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"\033[1;34mDevice: {partition.device}\033[0m")
            print(f"\033[1;34mMountpoint: {partition.mountpoint}\033[0m")
            print(f"\033[1;34mFile system type: {partition.fstype}\033[0m")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # 可能会因为没有权限而无法访问某些挂载点
                continue
            print(f"\033[1;32mTotal Size: {partition_usage.total}\033[0m")
            print(f"\033[1;33mUsed: {partition_usage.used}\033[0m")
            print(f"\033[1;33mFree: {partition_usage.free}\033[0m")
            print(f"\033[1;31mPercentage: {partition_usage.percent}%\033[0m")

if __name__ == "__main__":
    computer_hardware()
    input("按 Enter 键退出...")  # 添加这行代码以保持窗口打开
