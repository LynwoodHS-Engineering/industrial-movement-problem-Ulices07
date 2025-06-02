#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
motor393_a = Motor29(brain.three_wire_port.a, True)
motor393_b = Motor29(brain.three_wire_port.b, False)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
motor_4 = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
motor393_g = Motor29(brain.three_wire_port.g, False)
motor393_h = Motor29(brain.three_wire_port.h, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      Industrial Movement Problem Project
#	Author:       Ulices Ayala, Aldo Torres
#	Created:  05/26/25
#	Description:  Robot is programmed to travel to container, collect balls, and travel back to put balls in another container
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
brain.screen.clear_screen()  
brain.screen.set_cursor(1,1)
brain.screen.print("Linear Slide Up")
motor_3.spin(FORWARD)                     #linear slide goes up
motor_4.spin(FORWARD)
wait(0.8,SECONDS)
motor_3.stop()
motor_4.stop()
wait(2,SECONDS)

brain.screen.set_cursor(2,1)
brain.screen.print("run straight")       #runs the straightway
motor_1.spin(FORWARD)
motor_2.spin(FORWARD)
motor393_a.spin(FORWARD)
motor393_b.spin(FORWARD)    
wait(10.4,SECONDS)                
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(2,SECONDS)

brain.screen.set_cursor(3,1)
brain.screen.print("pickerupper collects balls")       #pickerupper rises 
motor393_g.spin(FORWARD)    
motor393_h.spin(FORWARD)  
wait(1.5,SECONDS)

brain.screen.set_cursor(4,1)
brain.screen.print("go backwards")  
motor_1.spin(REVERSE)       #goes back to spin
motor_2.spin(REVERSE)
motor393_a.spin(REVERSE)
motor393_b.spin(REVERSE)
wait(1.5,SECONDS)             
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(1,SECONDS)

brain.screen.set_cursor(5,1)
brain.screen.print("360 spin")  
motor_1.spin(REVERSE)
motor_2.spin(FORWARD)      #spins 360 degrees
motor393_a.spin(REVERSE)
motor393_b.spin(FORWARD)
wait(2.4,SECONDS)                
motor_1.stop() 
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(1.5,SECONDS)


brain.screen.set_cursor(6,1)
brain.screen.print("runs straight")       #runs the straightway
motor_1.spin(FORWARD)
motor_2.spin(FORWARD)
motor393_a.spin(FORWARD)
motor393_b.spin(FORWARD)    
wait(8.5,SECONDS)              
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(2, SECONDS)

brain.screen.set_cursor(7,1)
brain.screen.print("Linear Slide Up")
motor_3.spin(FORWARD)                     #linear goes up
motor_4.spin(FORWARD)
wait(5,SECONDS)
motor_3.stop()
motor_4.stop()
wait(1.5, SECONDS)


brain.screen.set_cursor(8,1)
brain.screen.print("runs straight")       # movdds forawrd to meet container
motor_1.spin(FORWARD)
motor_2.spin(FORWARD)
motor393_a.spin(FORWARD)
motor393_b.spin(FORWARD)    
wait(0.5,SECONDS)              
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(2, SECONDS)


brain.screen.set_cursor(9,1)
brain.screen.print("pcikerupper sets balls down")
motor393_g.spin(REVERSE)
motor393_h.spin(REVERSE)
wait(1.5,SECONDS)
motor393_g.stop()            #pickerupper releases; dropping balls in container 
motor393_h.stop()
wait(2,SECONDS)

brain.screen.set_cursor(10,1)
brain.screen.print("runs straight")       #runs the straightway backwards
motor_1.spin(REVERSE)
motor_2.spin(REVERSE)
motor393_a.spin(REVERSE)
motor393_b.spin(REVERSE)    
wait(9.7,SECONDS)              
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(2, SECONDS)


motor_1.spin(REVERSE)
motor_2.spin(FORWARD)      #spins 360 degrees
motor393_a.spin(REVERSE)
motor393_b.spin(FORWARD)
wait(2.4,SECONDS)                 
motor_1.stop() 
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(1.5,SECONDS)

motor_3.spin(REVERSE)                     #linear goes down to reach balls
motor_4.spin(REVERSE)
wait(5,SECONDS)
motor_3.stop()
motor_4.stop()
wait(1.5, SECONDS)

motor_1.spin(FORWARD)
motor_2.spin(FORWARD)
motor393_a.spin(FORWARD)   #forward to reach balls
motor393_b.spin(FORWARD)    
wait(1,SECONDS)                
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(2, SECONDS)

motor_1.spin(REVERSE)       #goes back  to spin
motor_2.spin(REVERSE)
motor393_a.spin(REVERSE)
motor393_b.spin(REVERSE)
wait(1.5,SECONDS)             
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(1,SECONDS)


motor_1.spin(REVERSE)
motor_2.spin(FORWARD)      #spins 360 degrees
motor393_a.spin(REVERSE)
motor393_b.spin(FORWARD)
wait(2.4,SECONDS)                 #360 spin for 2.5seconds
motor_1.stop() 
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(1.5,SECONDS)


motor_1.spin(FORWARD)
motor_2.spin(FORWARD)
motor393_a.spin(FORWARD)    # runs back to container
motor393_b.spin(FORWARD)    
wait(8.5,SECONDS)              
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(2, SECONDS)


motor_3.spin(FORWARD)                     #linear goes up
motor_4.spin(FORWARD)
wait(5,SECONDS)
motor_3.stop()
motor_4.stop()
wait(1.5, SECONDS)


motor_1.spin(FORWARD)
motor_2.spin(FORWARD)
motor393_a.spin(FORWARD)             #forawrd to reach container
motor393_b.spin(FORWARD)    
wait(0.5,SECONDS)              
motor_1.stop()
motor_2.stop()
motor393_a.stop()
motor393_b.stop()
wait(2, SECONDS)



motor393_g.spin(REVERSE)
motor393_h.spin(REVERSE)
wait(1.5,SECONDS)
motor393_g.stop()            #pickerupper releases
motor393_h.stop()
wait(2,SECONDS)
