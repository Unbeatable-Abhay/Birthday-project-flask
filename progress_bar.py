import time
import sys

def progress_bar(total):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '█' * int(percent / 2) + '-' * (50 - int(percent / 2))
        sys.stdout.write(f'\r|{bar}| {percent:.2f}%')
        sys.stdout.flush()
        time.sleep(0.1)  # simulate work

progress_bar(100)
