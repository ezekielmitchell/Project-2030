import time
from datetime import datetime
import threading
from envirophat import light, weather
import csv


# data collection
dataFile = 'envirophat_data.csv'
fields = ['Date/time', 'Temperature', 'Lighting']

def writing():
	with open(dataFile, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['Date-Time', 'Temperature', 'Lighting'])

# collect date/time data
def dateTime():
	while True:
		global now 
		now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(f'Time: {now}')
		time.sleep(1)



# collect light data
def lightData():
	while True:
		global lighting 
		lighting = light.light()
		print(f'Light level: {lighting}')
		time.sleep(1)
	

# collect temperature data
def tempData():
	while True:
		global temp 
		temp = weather.temperature()
		print(f'Temperature: {temp}')
		time.sleep(1)


# collect data
def dataCollect():
	
	while True:
		with open(dataFile, mode='a', newline='') as file:
			writer = csv.writer(file)
			writer.writerow([now, temp, lighting])

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
