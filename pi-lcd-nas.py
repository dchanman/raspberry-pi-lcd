#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

df_cmd = "df -h | grep pidata | awk '{print $3 \"/\" $2}'"
uptime_cmd = "uptime | grep -ohe 'up .*' | sed 's/,//g' | awk '{ print $2\" \"$3 }'"
free_cmd = "free | awk 'FNR == 3 {print $4/($3+$4)*100}'"

lcd.begin(16,1)

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def print_nas_usage():
    lcd.clear()
    usage = run_cmd(df_cmd)
    lcd.message("PiData NAS\n")
    lcd.message("Used: " + usage)

def print_system():
    lcd.clear()
    uptime = run_cmd(uptime_cmd)
    free = run_cmd(free_cmd)
    lcd.message("Up: " + uptime + "\n")
    lcd.message("RAM Free: {0} M".format(free[0:4]))

def main():
    while True:
        print_nas_usage()
        sleep(5)
        print_system()
        sleep(5)

main()
