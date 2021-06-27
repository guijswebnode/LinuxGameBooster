#!/bin/bash
core=0
maxcore="$(nproc --all)"
governor="ondemand"
while [ $core != $maxcore ]; do
sudo echo $governor > /sys/devices/system/cpu/cpu$core/cpufreq/scaling_governor
echo -e "\e[1;35m Processor core number $core is now $governor \e[0m"
let core=core+1
done
