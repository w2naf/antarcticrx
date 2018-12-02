#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# Modified by Nathaniel Frissell December 2018
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading

from antarcticrx.config import working_dir
sleep_secs  = 5

outdir  = os.path.join(working_dir,'gps_data')
if not os.path.exists(outdir):
    os.makedirs(outdir)
outfile = os.path.join(outdir,'gps.csv')
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)

def pline(line):
  """Records line to datafile and print to screen."""
  with open(outfile,'a') as fl:
    print(line)
    fl.write(line+'\n')
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread

  pline('#### GPS LOGGING STARTED {!s} ####'.format(datetime.datetime.now()))
  pline('# Polling every {!s} seconds to {!s}'.format(sleep_secs,outfile))
  pline('# datetime_ut, lat, lon')

  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
#      os.system('clear')
 
#      print
#      print ' GPS reading'
#      print '----------------------------------------'
#      print 'latitude    ' , gpsd.fix.latitude
#      print 'longitude   ' , gpsd.fix.longitude
#      print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
#      print 'altitude (m)' , gpsd.fix.altitude
#      print 'eps         ' , gpsd.fix.eps
#      print 'epx         ' , gpsd.fix.epx
#      print 'epv         ' , gpsd.fix.epv
#      print 'ept         ' , gpsd.fix.ept
#      print 'speed (m/s) ' , gpsd.fix.speed
#      print 'climb       ' , gpsd.fix.climb
#      print 'track       ' , gpsd.fix.track
#      print 'mode        ' , gpsd.fix.mode
#      print
#      print 'sats        ' , gpsd.satellites

      pline('{!s},{!s},{!s}'.format(gpsd.fix.utc,gps.fix.latitude,gps.fix.longitude))
 
      time.sleep(sleep_secs) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
