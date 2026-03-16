import pyautogui
import time
import random
import schedule

# Editable Config
cooldown = 7  # seconds between command cycles
remind_after_cycles = 60  # Remind to check huntbot after 60 cycles

# Track cycles
cycle_count = 0

# Command set to run
commands = ["owo hunt", "owo battle", "owo sell all "]

def send_command(cmd):
    pyautogui.typewrite(cmd)
    pyautogui.press("enter")
    time.sleep(random.uniform(1.5, 2.5))

def owo_cycle():
    global cycle_count
    for cmd in commands:
        send_command(cmd)
    cycle_count += 1
    print(f"[Cycle {cycle_count}] Complete")
    if cycle_count % remind_after_cycles == 0:
        print(f"🔔 Time to check your [HUNTBOT] and upgrades!")

# Scheduler
schedule.every(cooldown).seconds.do(owo_cycle)

print("Switch to Discord in 5 seconds...")
time.sleep(5)

while True:
    schedule.run_pending()
    time.sleep(1)