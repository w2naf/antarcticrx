#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HPSDR MultiRX
# Author: Nathaniel Frissell W2NAF
# Description: Records multiple spectrum chunks to disk
# Generated: Sat Dec  1 19:33:19 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

def struct(data): return type('Struct', (object,), data)()

import os
from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from datetime import datetime
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import hpsdr
import numpy as np; import gr_digital_rf
import sip
import sys
from gnuradio import qtgui

rxs = []
rxs.append({'label': 'CHU_3300',  'frequency':  3.330e6})
rxs.append({'label': 'HAM_3596',  'frequency':  3.596e6})
rxs.append({'label': 'CHU_7850',  'frequency':  7.096e6})
rxs.append({'label': 'HAM_7096',  'frequency':  7.096e6})
rxs.append({'label': 'CHU_14670', 'frequency': 14.670e6})
rxs.append({'label': 'HAM_14096', 'frequency': 14.096e6})
rxs.append({'label': 'WWV_10050', 'frequency': 10.050e6})

rx_samp_rate    = 192000
working_dir     = "/media/icerx/icerx/hf_data/"
metadata        = {'call':'W2NAF','grid':'<6-digit-grid>','rx':'Red Pitaya','ant':'DXE RF-PRO-1B'}

if not os.path.exists(working_dir):
    os.makedirs(working_dir)

class hpsdr_multirx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "HPSDR MultiRX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("HPSDR MultiRX")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "hpsdr_multirx")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.timestamp_iso  = timestamp_iso = datetime.utcnow().isoformat()+"Z"
        self.file_stamp     = file_stamp    = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")

        ##################################################
        # Blocks
        ##################################################
        
        for rx_id,rx_dct in enumerate(rxs):
            self.add_waterfall(rx_id)

        self.add_frequency_display()

        freqs = [0]*7
        for rx_id,rx_dct in enumerate(rxs):
            freqs[rx_id]  = int(rx_dct['frequency'])

        self.hpsdr_hermesNB_0 = hpsdr.hermesNB(freqs[0],freqs[1],freqs[2],freqs[3],freqs[4],freqs[5],freqs[6],
                10000000, 10000000, 0, 0, 1, 1, 0, rx_samp_rate, "enp2s0", "0xF0", 0xa0, 0, 0x00, 0x10, 0, len(rxs), "*")

        channels    = ['']*len(rxs)
        for rx_id,rx_dct in enumerate(rxs):
            channels[rx_id] = rx_dct['label']

        self.gr_digital_rf_digital_rf_sink_0 = \
            gr_digital_rf.digital_rf_sink(
                working_dir,
                channels=channels,
                dtype=np.complex64,
                subdir_cadence_secs=3600,
                file_cadence_millisecs=1000,
                sample_rate_numerator=int(rx_samp_rate),
                sample_rate_denominator=1,
                start="nowish", ignore_tags=False,
                is_complex=True, num_subchannels=1,
                uuid_str=None if ''=='' else '',
                center_frequencies=None if () is () else (),
                metadata=metadata,
                is_continuous=True, compression_level=0,
                checksum=False, marching_periods=True,
                stop_on_skipped=False, debug=False,
                min_chunksize=None if 0==0 else 0,
            )

        self.analog_sig_source_x_1 = analog.sig_source_c(48000, analog.GR_COS_WAVE, -1000, 0.95, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.hpsdr_hermesNB_0, 0))

        for rx_id,rx_dct in enumerate(rxs):
            self.connect((self.hpsdr_hermesNB_0, rx_id), (self.gr_digital_rf_digital_rf_sink_0, rx_id))

        for rx_id,rx_dct in enumerate(rxs):
            self.connect((self.hpsdr_hermesNB_0, rx_id), (self.qtgui_freq_sink_x_0, rx_id))

        for rx_id,rx_dct in enumerate(rxs):
            self.connect((self.hpsdr_hermesNB_0, rx_id), (rx_dct['qtgui_waterfall'], 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hpsdr_multirx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def add_waterfall(self,rx_id):
        rx_frequency    = rxs[rx_id]['frequency']
        rx_label        = rxs[rx_id]['label']

        qtgui_waterfall = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_frequency, #fc
        	rx_samp_rate, #bw
        	rx_label, #name
                1 #number of inputs
        )
        qtgui_waterfall.set_update_time(0.10)
        qtgui_waterfall.enable_grid(False)
        qtgui_waterfall.enable_axis_labels(True)

        if not True:
          qtgui_waterfall.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          qtgui_waterfall.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                qtgui_waterfall.set_line_label(i, "Data {0}".format(i))
            else:
                qtgui_waterfall.set_line_label(i, labels[i])
            qtgui_waterfall.set_color_map(i, colors[i])
            qtgui_waterfall.set_line_alpha(i, alphas[i])

        qtgui_waterfall.set_intensity_range(-140, 10)

        _qtgui_waterfall_win = sip.wrapinstance(qtgui_waterfall.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(_qtgui_waterfall_win)

        rxs[rx_id]['qtgui_waterfall'] = qtgui_waterfall

    def add_frequency_display(self):
        labels      = ['']*10
        for rx_id,rx_dct in enumerate(rxs):
            labels[rx_id] = '{!s} MHz'.format(rx_dct['frequency']*1e-6)

        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	000000, #fc
        	rx_samp_rate, #bw
        	'Received Spectrum', #name
        	len(rxs) #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-160, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(7):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)

def main(top_block_cls=hpsdr_multirx, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
