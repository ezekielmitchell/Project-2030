import time
from datetime import datetime
import threading
from envirophat import light, weather
import csv

# global variables
now = None
lighting = None
temp = None

# data collection
dataFile = 'envirophat_data.csv'
fields = ['Date/time', 'Temperature', 'Lighting']
dataLock = threading.Lock()

def writing():
	with open(dataFile, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Date-Time', 'Temperature', 'Lighting'])

# collect date/time data
def dateTime():
	global now 
	while True:
		currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		with dataLock:
			now = currentTime
		print(f'Time: {now}')
		time.sleep(3)



# collect light data
def lightData():
	global lighting
	while True: 
		currentLight = light.light()
		with dataLock:
			lighting = currentLight
		print(f'Light level: {lighting}')
		time.sleep(3)
	

# collect temperature data
def tempData():
	global temp
	while True: 
		currentTemp = weather.temperature()
		with dataLock:
			temp = currentTemp
		print(f'Temperature: {temp}')
		time.sleep(3)


# collect data
def dataCollect():
	while True:
		with dataLock:
			if now is not None and temp is not None and lighting is not None:
				with open(dataFile, mode='a', newline='') as file:
					writer = csv.writer(file)
					writer.writerow([now, temp, lighting])
		time.sleep(3)

if __name__ == "__main__":
	
	writing()
	
	# thread creation
	timeThread = threading.Thread(target=dateTime)
	tempThread = threading.Thread(target=tempData)
	lightThread = threading.Thread(target=lightData)
	dataThread = threading.Thread(target=dataCollect)
	
	# run threads
	timeThread.start()
	tempThread.start()
	lightThread.start()
	dataThread.start()
	
	# join threads to main
	timeThread.join()
	tempThread.join()
	lightThread.join()
	dataThread.join()
