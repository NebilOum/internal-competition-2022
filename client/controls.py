# import all needed libraries
import json
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

#left side motor
m1_input1 = 16
m1_input2 = 20
m1_enable = 19

GPIO.setup(m1_input1, GPIO.OUT)
GPIO.setup(m1_input2, GPIO.OUT)
GPIO.setup(m1_enable, GPIO.OUT)

m1_pwm = GPIO.PWM(m1_enable, 1000)
m1_pwm.start(0)

#right side motor
m2_input1 = 6
m2_input2 = 26
m2_enable = 13

GPIO.setup(m2_input1, GPIO.OUT)
GPIO.setup(m2_input2, GPIO.OUT)
GPIO.setup(m2_enable, GPIO.OUT)

m2_pwm = GPIO.PWM(m2_enable, 1000)
m2_pwm.start(0)

#sucker motor
sucker_input1 = 14
sucker_input2 = 15
sucker_enable = 18

GPIO.setup(sucker_input1, GPIO.OUT)
GPIO.setup(sucker_input2, GPIO.OUT)
GPIO.setup(sucker_enable, GPIO.OUT)

sucker_pwm = GPIO.PWM(sucker_enable, 1000)
sucker_pwm.start(0)

#main
def intakeControl(spinIn):
    if spinIn == "spinInward" :
        GPIO.output(sucker_input1, GPIO.HIGH)
        GPIO.output(sucker_input2, GPIO.LOW)
        sucker_pwm.ChangeDutyCycle(100) #spin to intake
    if spinIn == "spinOutward":
        GPIO.output(sucker_input1, GPIO.LOW)
        GPIO.output(sucker_input2, GPIO.HIGH)
        sucker_pwm.ChangeDutyCycle(100) #spin to output
    if (spinIn == "noSpin"):
        GPIO.output(sucker_input1, GPIO.LOW)
        GPIO.output(sucker_input2, GPIO.LOW)
        sucker_pwm.ChangeDutyCycle(0) #intake does not spin

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
