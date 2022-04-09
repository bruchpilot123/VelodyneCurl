"""
connection.py
Maintainer: Robert Scheffler
Date: 09.04.22
"""

from io import StringIO as BytesIO
from urllib.parse import urlencode

import pycurl

lidar = pycurl.Curl()
buffer = BytesIO()


class EstablishLidarConnection:
    # Set the LIDAR Ip Address
    Base_URL = 'http://192.168.1.201/cgi/'
    buffer = BytesIO()

    def __init__(self):
        pass

    def connect(self):
        """
        Function to Show Some Electric Information about the Lidar
        :return: NONE
        """

        print("\nSome Electricity Information:\n")
        lidar.setopt(pycurl.URL, self.Base_URL + "diag.json")
        lidar.perform()
        print("\nConnection Established!!!\n")

    def showstatus(self):
        """
        Function to show GPS, Motor and Laser State
        :return: NONE
        """
        lidar.setopt(pycurl.URL, self.Base_URL + "status.json")
        lidar.perform()

    def setrpm(self):
        """
        Function to Set the RPM Parameter
        :return: NONE
        """
        lidar.setopt(pycurl.URL, self.Base_URL + "setting")
        lidar.setopt(lidar.POSTFIELDS, urlencode({'rpm': '300'}))
        lidar.setopt(lidar.WRITEDATA, self.buffer)
        lidar.perform()
