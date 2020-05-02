#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_botTwitter.py
#  
#  Copyright 2020  Krounet
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import tweepy
import auth
import time
import arduino_reading
import serial

def stateArduino(info='waiting...',api=0):
    action=''    
    if info == 'waiting...':
        action = 'nothing'        
    elif info == 'button_pressed\n':
        actiontime=time.localtime()        
        action = "Button presse at : "+time.strftime("%H:%M",actiontime)+". Wonderful isn't it ?"
        api.update_status(status=action)
        
    elif info == 'quit\n':
        action = 'quit'
    return action

if __name__ == '__main__':
    port='/dev/ttyACM0'
    debit=9600
    portSerialArduino=serial.Serial(port,debit)
    api,auth=auth.auth()
    time_launch=time.localtime()
    str_time_launch=time.strftime("%A %d %B %Y %H:%M",time_launch)
    api.update_status(status="Boot testing on : "+str_time_launch)
    stateinfo=''
   
    
    while stateinfo !='quit' :        
        dialogArduino=arduino_reading.arduino_reading(portSerialArduino)
        stateinfo=stateArduino(dialogArduino,api)
    time_ending=time.localtime()
    str_time_ending=time.strftime("%A %d %B %Y %H:%M",time_launch)
    api.update_status(status="Time to sleep on "+str_time_ending)
                
