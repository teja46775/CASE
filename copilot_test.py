import os
import platform
import subprocess

def get_uptime():
    system = platform.system()
    if system == "Linux":
        # Linux: uptime available directly
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
    elif system == "Windows":
        # Windows: use 'net stats srv' and parse output
        output = subprocess.check_output("net stats srv", shell=True, text=True)
        for line in output.splitlines():
            if "Statistics since" in line:
                # Parse the timestamp and compute uptime
                from datetime import datetime
                boot_time = line.split("Statistics since")[1].strip()
                boot_time = datetime.strptime(boot_time, "%m/%d/%Y %I:%M:%S %p")
                now = datetime.now()
                uptime_seconds = (now - boot_time).total_seconds()
                return uptime_seconds
        raise RuntimeError("Could not determine uptime on Windows.")
    elif system == "Darwin":
        # macOS: use 'sysctl -n kern.boottime'
        output = subprocess.check_output("sysctl -n kern.boottime", shell=True, text=True)
        import re
        match = re.search(r'sec = (\d+)', output)
        if match:
            boot_time = int(match.group(1))
            from datetime import datetime
            now = int(datetime.now().timestamp())
            uptime_seconds = now - boot_time
            return uptime_seconds
        else:
            raise RuntimeError("Could not determine uptime on macOS.")
    else:
        raise NotImplementedError(f"Uptime not implemented for OS: {system}")

if __name__ == "__main__":
    uptime = get_uptime()
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    print(f"System Uptime: {hours}h {minutes}m {seconds}s")
