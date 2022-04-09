import connection as CN
import time

"""
Main Class which  only calls the functions
main.py
Maintainer: Robert Scheffler 
Date: 09.04.22

Important: Remember the 1s timeoutsm, as suggested by Velodyne

"""

if __name__ == '__main__':
    connection = CN.EstablishLidarConnection()
    connection.connect()
    time.sleep(1)
    connection.showstatus()
    time.sleep(1)
    connection.setrpm()