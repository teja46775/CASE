## Experience Using Copilot

### What code did it generate?

I used GitHub Copilot to generate a Python script that reports the system uptime across different operating systems (Linux, Windows, macOS). The generated `copilot_test.py` script contains:

- A function `get_uptime()` that:
  - Detects the operating system using the `platform` module.
  - For **Linux**, reads `/proc/uptime` to get uptime in seconds.
  - For **Windows**, runs `net stats srv` and parses the "Statistics since" line to compute uptime.
  - For **macOS (Darwin)**, executes `sysctl -n kern.boottime` and parses the output to retrieve the boot time, then calculates uptime.
- A main block that:
  - Calls `get_uptime()` and converts the result into hours, minutes, and seconds.
  - Prints the system uptime in a human-readable format.

### Did you modify the script? If so, why?

Yes, I made a few modifications after Copilot's initial suggestion:

- **Error Handling:** I improved error messages in the Windows and macOS branches to provide clearer feedback if uptime could not be determined.
- **Datetime Parsing:** I made sure the datetime parsing format for Windows matched the actual output of `net stats srv`.
- **Import Location:** I moved some imports (like `datetime` and `re`) to the top of the file for better readability and performance, though this is optional in Python.
- **Formatting:** I added comments to clarify the purpose of each OS branch and improved code readability.

### How did you test it?

I tested the script on:

- **Linux:** I ran the script on an Ubuntu machine. The uptime matched the value reported by the `uptime` command.
- **Windows:** I tested it on a Windows 10 system. The script successfully parsed the "Statistics since" line and computed the correct uptime.
- **macOS:** I ran the script on a MacBook. It correctly retrieved the boot time using `sysctl` and computed the uptime.

For each platform, I compared the script’s output with the system’s built-in uptime utilities to ensure accuracy.

#### Sample Output

```
System Uptime: 12h 41m 32s
```

### Summary

Copilot provided a solid starting point and generated most of the cross-platform logic for retrieving uptime. Some minor edits were needed for robustness and clarity, but overall Copilot made the process faster and easier.
