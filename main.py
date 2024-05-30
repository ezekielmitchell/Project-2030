import time
from datetime import datetime
import threading
from envirophat import light, weather


# collect date/time data
def dateTime():
	while True:
		now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(f'Time logged: {now}')
		time.sleep(1)



# collect light data
def lightData():
	while True:
		lighting = light.light()
		print(f'Light level: {lighting}')
		time.sleep(1)
	

# collect temperature data
def tempData():
	while True:
		temp = weather.temperature()
		print(f'Temperature: {temp}')
		time.sleep(1)


# collect data
def collectData():
		

collect_data()
