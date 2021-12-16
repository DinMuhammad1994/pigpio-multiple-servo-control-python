# pigpio-multiple-servo-control-python
This code demonstrates the control of 6 servo motor without jitters using this python code  Note:  The pin configuration of GPIO.BCM should be used for pinout connection.



Install pigpio
If you're working with the rpi3's gpio, the pigpio library can be very handy.


sudo apt-get update
sudo apt-get install pigpio 

If you also want to access pigpio from python, install: sudo apt-get install python-pigpio python3-pigpio

Setup pigpiod service to run at boot

sudo systemctl enable pigpiod

You can also start pigpiod immediately by doing: sudo systemctl start pigpiod

After reboot, verify with: sudo service pigpiod status
