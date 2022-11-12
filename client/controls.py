# import all needed libraries
import json
import RPi.GPIO as GPIO
from time import sleep

# set the pin configuration mode to BCM
GPIO.setmode(GPIO.BCM)

#left motors
rM_inPin1 = 6
rM_inPin2 = 26
rM_enable = 19

GPIO.setup(rM_inPin1, GPIO.OUT)
GPIO.setup(rM_inPin2, GPIO.OUT)
GPIO.setup(rM_enable, GPIO.OUT)
pwmRM = GPIO.PWM(rM_enable, 1000)
pwmRM.start(0)

#right motors
lM_inPin1 = 16
lM_inPin2 = 20
lM_enable = 13

GPIO.setup(lM_inPin1, GPIO.OUT)
GPIO.setup(lM_inPin2, GPIO.OUT)
GPIO.setup(lM_enable, GPIO.OUT)
pwmLM = GPIO.PWM(lM_enable, 1000)
pwmLM.start(0)

#intake motor
iM_inPin1 = 14
iM_inPin2 = 15
iM_enable = 18
GPIO.setup(iM_inPin1, GPIO.OUT)
GPIO.setup(iM_inPin2, GPIO.OUT)
GPIO.setup(iM_enable, GPIO.OUT)
GPIO.output(iM_enable, GPIO.LOW)

 #servo to clear intake
s1_enable = 12 #servo 1
GPIO.setup(s1_enable, GPIO.OUT)
pwmS1 = GPIO.PWM(s1_enable, 50)
pwmS1.start(0)

def intakeControl(spinIn):
    if spinIn =="spinInward" :
        GPIO.output(iM_inPin1, GPIO.HIGH)
        GPIO.output(iM_inPin2, GPIO.LOW)
        GPIO.output(iM_enable, GPIO.HIGH) #spin to intake
    if spinIn =="spinOutward":
        GPIO.output(iM_inPin1, GPIO.LOW)
        GPIO.output(iM_inPin2, GPIO.HIGH)
        GPIO.output(iM_enable, GPIO.HIGH)#spin to output
    if (spinIn == "noSpin"):
        GPIO.output(iM_inPin1, GPIO.LOW)
        GPIO.output(iM_inPin2, GPIO.LOW)
        GPIO.output(iM_enable, GPIO.LOW) #intake does not spin

def tankDrive(xSpeed,ySpeed,direction):
    # GPIO.output(rM_inPin1, GPIO.LOW)
    # GPIO.output(rM_inPin2, GPIO.HIGH)
    # pwmRM.ChangeDutyCycle(100)
    # GPIO.output(lM_inPin1,GPIO.HIGH)
    # GPIO.output(lM_inPin2,GPIO.LOW)
    # pwmLM.ChangeDutyCycle(100)
    # pwmLM.ChangeDutyCycle(100)
    # GPIO.output(iM_inPin1, GPIO.HIGH)
    # GPIO.output(iM_inPin2, GPIO.LOW)
    # GPIO.output(iM_enable, GPIO.HIGH)

    # if (direction == "posDirection"): 
        if(xSpeed == 0):#drive foward
            GPIO.output(rM_inPin1,GPIO.HIGH)
            GPIO.output(rM_inPin2,GPIO.LOW)
            GPIO.output(lM_inPin1,GPIO.HIGH)
            GPIO.output(lM_inPin2,GPIO.LOW)
            pwmRM.ChangeDutyCycle(ySpeed)
            pwmLM.ChangeDutyCycle(ySpeed)
        if (ySpeed == 0):#drive right
            GPIO.output(rM_inPin1,GPIO.LOW)
            GPIO.output(rM_inPin2,GPIO.HIGH)
            GPIO.output(lM_inPin1,GPIO.HIGH)
            GPIO.output(lM_inPin2,GPIO.LOW)
            pwmLM.ChangeDutyCycle(xSpeed*0.5)
            pwmRM.ChangeDutyCycle(xSpeed*0.5)
    # if (direction == "negDirection"):
    #     if (xSpeed == 0):#dirve backwards
    #         GPIO.output(rM_inPin1,GPIO.HIGH)
    #         GPIO.output(rM_inPin2,GPIO.LOW)
    #         GPIO.output(lM_inPin1,GPIO.LOW)
    #         GPIO.output(lM_inPin2,GPIO.HIGH)
    #         pwmRM.ChangeDutyCycle(ySpeed)
    #         pwmLM.ChangeDutyCycle(ySpeed)
    #     if (ySpeed == 0):#drive left
    #         GPIO.output(rM_inPin1,GPIO.LOW)
    #         GPIO.output(rM_inPin2,GPIO.HIGH)
    #         GPIO.output(lM_inPin1,GPIO.LOW)
    #         GPIO.output(lM_inPin2,GPIO.HIGH)
    #         pwmRM.ChangeDutyCycle(xSpeed*0.5)
    #         pwmLM.ChangeDutyCycle(xSpeed*0.5)

def arcadeDrive(xSpeed,ySpeed,direction):
    left = ySpeed + xSpeed
    right = ySpeed - xSpeed
    if (direction == "posDirection"): 
        if(xSpeed == 0):#drive foward
            GPIO.output(rM_inPin1,GPIO.HIGH)
            GPIO.output(rM_inPin2,GPIO.LOW)
            GPIO.output(lM_inPin1,GPIO.HIGH)
            GPIO.output(lM_inPin2,GPIO.LOW)
            pwmRM.ChangeDutyCycle(right)
            pwmLM.ChangeDutyCycle(left)
    if (direction == "negDirection"):
        if (xSpeed == 0):#dirve backwards
            GPIO.output(rM_inPin1,GPIO.HIGH)
            GPIO.output(rM_inPin2,GPIO.LOW)
            GPIO.output(lM_inPin1,GPIO.LOW)
            GPIO.output(lM_inPin2,GPIO.HIGH)
            pwmRM.ChangeDutyCycle(right)
            pwmLM.ChangeDutyCycle(left)
        
def main():
    print("now running!")
    try:
        #command = json.loads(input())
        tankDrive(0,50,"Direction")
        while True:
            command = json.loads(input())
            #pastX = "50"
            #if()
            # intakeControl(command["intake"])
            # if(command["driveType"] == "tank") :
            #tankDrive(command["xJoystickPos"],command["yJoystickPos"],command["driveDirection"])
    except KeyboardInterrupt:
        pass 
    finally:
        GPIO.cleanup()

main()