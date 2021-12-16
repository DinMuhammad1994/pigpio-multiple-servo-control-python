import pigpio
import time

pi = pigpio.pi()
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
pi.set_mode(24, pigpio.OUTPUT)
pi.set_mode(17, pigpio.OUTPUT)
pi.set_mode(27, pigpio.OUTPUT)
pi.set_mode(22, pigpio.OUTPUT)



print ("mode: ", pi.get_mode(18))
print ("mode: ", pi.get_mode(23))
print ("mode: ", pi.get_mode(24))
print ("mode: ", pi.get_mode(17))
print ("mode: ", pi.get_mode(27))
print ("mode: ", pi.get_mode(22))

#inititally all motors at back positions
pi.set_servo_pulsewidth(18, 1500)
pi.set_servo_pulsewidth(23, 1500)
pi.set_servo_pulsewidth(24, 1700)
pi.set_servo_pulsewidth(17, 1500)
pi.set_servo_pulsewidth(27, 1800)
pi.set_servo_pulsewidth(22, 1800)


for i in range(0,2): 
    #-----------servo 1---------------
    print("drop...!")
    pi.set_servo_pulsewidth(18, 650)          #pin # , pwm as required
    time.sleep(2)
    print("return")
    pi.set_servo_pulsewidth(18, 1500)
    time.sleep(2)

    
    #-----------servo 2---------------
    print("drop...!")
    pi.set_servo_pulsewidth(23, 650)
    time.sleep(2)
    print("return")
    pi.set_servo_pulsewidth(23, 1500)
    time.sleep(2)

  
    #-----------servo 3---------------
    print("drop...!")
    pi.set_servo_pulsewidth(24, 650)
    time.sleep(2)
    print("return")
    pi.set_servo_pulsewidth(24, 1700)
    time.sleep(2)

   
    #-----------servo 4---------------
    print("drop...!")
    pi.set_servo_pulsewidth(17, 500)
    time.sleep(2)
    print("return")
    pi.set_servo_pulsewidth(17, 1500)
    time.sleep(2)


    
    #-----------servo 5---------------
    print("drop...!")
    pi.set_servo_pulsewidth(27, 500)
    time.sleep(2)
    print("return")
    pi.set_servo_pulsewidth(27, 1800)
    time.sleep(2)


    
    #-----------servo 6---------------
    print("drop...!")
    pi.set_servo_pulsewidth(22, 500)
    time.sleep(2)
    print("return")
    pi.set_servo_pulsewidth(22, 1800)
    time.sleep(2)


    
pi.stop()
