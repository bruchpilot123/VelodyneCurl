# Tool for checking LIDAR Settings

Maintainer: *Robert Scheffler*

Requirements:

- PyCurl

<code> pip install pycurl </code>

## Description
The tool establishes a connection with the Velodyne Puck 16 High- Res Lidar. It uses Curl for the Connection. The tools
shows at first different parameters and sets the correct rpm, as indicated in the code.
The connection.py script is not necessary to run the tool, but it is a useful example from Velodyne.

Important -  Velodyne Documentation says following:

_**Note: It is recommended to issue only one cURL command per second to the sensor._**
Take care of that for further development!!!

## ToDo:

There is a weird issue, that after the POST request it is not possible to obtain the status
anymore. Further Investigations have to be done here. But the setting of the parameter itself works.

In the example from Velodyne it works and they are using UrlOpen. But I could not figure out why and I do not want to 
use something I do not understand.

