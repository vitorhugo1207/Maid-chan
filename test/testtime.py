from datetime import datetime
import time

start = datetime.now().second
time.sleep(5)
end = datetime.now().second

second = int(end) - int(start)
min = second // 60
hour = min // 60

print(f'h:{hour}, m:{min}, s:{second}')
