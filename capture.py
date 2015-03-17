#!/usr/bin/python
import subprocess

p = subprocess.Popen(nfc-poll, shell=True, stderr=subprocess.PIPE)

while True:
  out = p.stderr.read(1)
  if out == '' and p.poll() != None:
    break
  if out != '':
    
