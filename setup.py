#!/usr/bin/env python

from distutils.core import setup

setup(name='AntarcticRx',
      version='0.0.1',
      description='NJIT Antarctic HF Receiver',
      author='Nathaniel A. Frissell W2NAF',
      author_email='nathaniel.a.frissell@njit.edu',
      url='https://github.com/w2naf/antarcticrx',
      packages=['antarcticrx'],
      scripts=['start_rx_all.py',
               'scripts/rx_recorder.py', 'scripts/start_rx.py',
               'scripts/gps_recorder.py','scripts/start_gps.py',
               'scripts/start_ringbuffer.py']
     )
