# System Health Monitor Script (Bash)
  - It demonstrates how to monitor system health using a Bash script that can be scheduled and executed automatically.

## Objective

- Create a Bash script to collect system diagnostics.
- Log the output to timestamped files.
- Schedule the script using cron to run daily.
- Enable running the script by typing a custom alias (`atharvapurushe`).

## Script Overview (`health_check.sh`)

```bash
#!/bin/bash

LOGFILE=~/Learning-List/Linux/SystemHealthMonitor/system_health_$(date +%Y-%m-%d_%H-%M-%S).log

{
echo "==================== System Health Report ===================="
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "---------------------------------------------------------------"

echo -e "\n>>> CPU Load:"
uptime

echo -e "\n>>> Memory Usage:"
free -h

echo -e "\n>>> Disk Usage:"
df -h

echo -e "\n>>> Top 5 Memory-Consuming Processes:"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6

echo -e "\n>>> Network Connections (listening ports):"
ss -tuln

echo -e "\n>>> Who is Logged In:"
who

echo -e "\n>>> System Uptime:"
uptime -p

echo -e "\n==================== End of Report ==========================="
} > "$LOGFILE"

## Run the Script
 - Manually ./health_check.sh
 - alias atharvapurushe='~/health_check.sh'


## Automating with cron
 - Open Ubuntu WSL Terminal. Launch Ubuntu from the Start Menu or type wsl in PowerShell or CMD.
 - Edit Your Crontab File with crontab -e. If prompted, choose nano as the default editor.
 - Add a Cron Entry
   Add 0 9 * * * /home/atharva/health_check.sh


