import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import time    #calling time to provide delays in program

DEW_HEATER_PIN = 35
AMBIENT_DHT_PIN = 4

DEW_HEATER_STEP = 10

def main(args):
    print("Starting dew heater module")
    GPIO.setmode(GPIO.BOARD);

    GPIO.setwarnings(False)           #do not show any warnings
    GPIO.setup(DEW_HEATER_PIN,GPIO.OUT)           # initialize GPIO35 as an output.
    dewHeater = GPIO.PWM(DEW_HEATER_PIN,100)          #GPIO35 as PWM output, with 100Hz frequency
    dewHeater.start(0)                              #generate PWM signal with 0% duty cycle

    while True:                               #execute loop forever
        # *** Get all sensor data ***
        # Get abmient temperature and realitive humidity
        humidity, ambientTemperatureC = DHT.read_retry(DHT.AM2302, AMBIENT_DHT_PIN)
        ambientTemperatureF = (ambientTemperatureC * (9.0/5.0)) + 32
        
        # Get tube temperature
        # <Insert Code to Read tube temp>
        
        # Calculate dew heater setting
        # <Insert calculation code>
	# tempDiff = tubeTemperature - ambientTemperatureF

	tubeSetPoint = ambientTemperature + 5
	tempDiff = tubeSetPoint - tubeTemperature
	heaterIntensity = 0 if tempDiff <= 0 else tempDiff*DEW_HEATER_STEP

        tempValue = ambientTemperatureF - 76

	
        if tempValue < 0:
            tempValue = 0
        elif tempValue > 10:
            tempValue = 10;
            
        print(f'Temperature: {ambientTemperatureC:.2f}C {ambientTemperatureF:.2f}F\tHumidity: {humidity:.2f}\tTempValue: {tempValue:.2f}')
        
        # Set Dew Heater value
        dewHeater.ChangeDutyCycle(tempValue * 10)
        time.sleep(2)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
