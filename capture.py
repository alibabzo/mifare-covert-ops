#!/usr/bin/python
from commands import *    # import lib to send shell commands
import RPi.GPIO as GPIO   # import lib to interact with GPIO
import time               # import lib to pause
import csv                # import lib to add line to table

GPIO.setmode(GPIO.BCM)    # tell the GPIO lib what pin naming we are using

GPIO.setup(18, GPIO_IN, pull_up_down=GPIO.PUD_UP) # setup pin 18 as input with built-in pull up resistor

c = csv.writer(open('uid.csv','a')) # open our csv file in append mode

def run_command(cmd): # define run command function
  print 'Running: "%s"' % cmd # tell console what command we're running
  text = getoutput(cmd) # get output from command
  uid = text[204:225] # get uid from output
  uid = ''.join(uid.split()) # remove spaces
  print uid
  c.writerow([uid]) # write uid to file

while True:
  input_state = GPIO.input(18)  # define input_state as the pushbutton state
  if input_state == False:  # if the pushbutton is pressed
    run_command('nfc-list') # run this command
    time.sleep(1) # pause for a second
