
#!/bin/bash

LOGFILE=~/Learning-List/Linux/SystemHealthMonitor/system_health_$(date +%Y-%m-%d_%H-%M-%S).log

(
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
) | tee "$LOGFILE"
