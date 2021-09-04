# HiLetgo DHT22/AM2302 Digital Temperature And Humidity Sensor 
Measure the Humitidty and Temperature



Important

## Resources ##

+ TDS Sensor
    + [Buy Sensor from Amzon](https://www.amazon.com/dp/B01N9BA0O4/ref=cm_sw_em_r_mt_dp_GFQYDDD35FYXMQRK9N6C) (~R410)
    + [Tutorial](https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/)

## Setup ##

- [X] A Raspberry Pi with VS Code and Python Environment 
- [ ] Connect the sensor with the Raspberry Pi
- [ ] Enable I2C in Interfaces
- [ ] Check the I2C Switch
- [ ] Run the files

### Connect the sensor with the Raspberry Pi ###



### Run the files ###

Install Adafruit Manually (Try PIP first):

```console
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get upgrade
sudo apt-get install build-essential python-dev python-openssl
sudo python3 setup.py install
```

