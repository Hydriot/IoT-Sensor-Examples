# Liquid Level Sensor - CQRobotics #
Measure if the sensor is in contact with liquid

![](https://raw.githubusercontent.com/Hydriot/IoT-Sensor-Examples/main/XXXX/sensor.jpg)


## Resources ##

* [Buy from Amzon](https://www.amazon.com/CQRobot-Consumption-Resistance-Temperature-Properties/dp/B07ZMGW3QJ) (~R270)
* [Product Wiki](http://www.cqrobot.wiki/index.php/Liquid_Level_Sensor)

## Setup ##

- [X] A Raspberry Pi with VS Code and Python Environment 
- [X] Connect the sensor with the Raspberry Pi
- [X] Install WiringPI (CPP Library)
- [X] Run the sample python script

### Connect the sensor with the Raspberry Pi ###

![](https://raw.githubusercontent.com/Hydriot/IoT-Sensor-Examples/main/connection.jpg)

### Install WiringPI ###

```console
sudo apt-get update
sudo apt-get install python-dev python-pip
sudo pip install wiringpi2
sudo pip3 install wiringpi
```

```console
sudo python
import wiringpi
wiringpi.piBoardRev()
```

### Run the sample_python.py file ###

![](https://raw.githubusercontent.com/Hydriot/IoT-Sensor-Examples/main//running.png)

