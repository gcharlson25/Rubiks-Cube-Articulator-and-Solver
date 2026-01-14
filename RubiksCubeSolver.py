#importing the random library to use the random method 
from vex import * 
import random 
 
#setting all the motor positions to 0 and creating an array to memorize the action history of the 
#cube after the scramble method 
motor_14_top.set_velocity(100,PERCENT); 
motor_16_bottom.set_velocity(100,PERCENT); 
motor_5_right.set_velocity(100,PERCENT); 
motor_6_left.set_velocity(100,PERCENT); 
motor_10_front.set_velocity(100,PERCENT); 
motor_8_end.set_velocity(100,PERCENT); 
motor_14_top.set_position(0,DEGREES); 
motor_14_top.set_position(0,DEGREES); 
motor_14_top.set_position(0,DEGREES); 
motor_14_top.set_position(0,DEGREES); 
motor_10_front.set_position(0,DEGREES); 
motor_8_end.set_position(0,DEGREES); 
indexT = 90; 
indexB = 90; 
indexR = 90; 
indexL = 90; 
indexF = 90; 
indexE = 90; 
actionHistory = []; 
ind = 0; 
 
 
while True: 
 
    #Code that allows the controller to rotate each side of the cube 
    if (controller_1.buttonLeft.pressing()): 
        motor_6_left.spin_for(FORWARD,90,DEGREES,wait=False); 
        brain.screen.set_cursor(6,6); 
        brain.screen.print("6 left"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonRight.pressing()): 
        motor_6_left.spin_for(REVERSE,90,DEGREES,wait=False); 
        brain.screen.set_cursor(6,6); 
        brain.screen.print("6 left"); 
        wait(0.5,SECONDS);    
    if (controller_1.buttonUp.pressing()): 
        motor_14_top.spin_for(REVERSE,90,DEGREES,wait=False); 
        brain.screen.set_cursor(2,2); 
        brain.screen.print("14 top"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonDown.pressing()): 
        motor_14_top.spin_for(FORWARD,90,DEGREES,wait=False); 
        brain.screen.set_cursor(2,2); 
        brain.screen.print("14 top"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonX.pressing()): 
        motor_16_bottom.spin_for(FORWARD,90,DEGREES,wait=False); 
        brain.screen.set_cursor(4,4); 
        brain.screen.print("16 bottom"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonB.pressing()): 
        motor_16_bottom.spin_for(REVERSE,90,DEGREES,wait=False); 
        brain.screen.set_cursor(4,4); 
        brain.screen.print("16 bottom"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonY.pressing()): 
        motor_5_right.spin_for(REVERSE,90,DEGREES,wait=False); 
        brain.screen.set_cursor(8,8); 
        brain.screen.print("5 right"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonA.pressing()): 
        motor_5_right.spin_for(FORWARD,90,DEGREES,wait=False); 
        brain.screen.set_cursor(8,8); 
        brain.screen.print("5 right"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonL1.pressing()): 
        motor_8_end.spin_for(FORWARD,90,DEGREES,wait=False); 
        brain.screen.set_cursor(10,10); 
        brain.screen.print("10 Front"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonL2.pressing()): 
        motor_8_end.spin_for(REVERSE,90,DEGREES,wait=False); 
        brain.screen.set_cursor(10,10); 
        brain.screen.print("10 Front"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonR1.pressing()): 
        motor_10_front.spin_for(REVERSE,90,DEGREES,wait=False); 
        brain.screen.set_cursor(10,10); 
        brain.screen.print("10 Front"); 
        wait(0.5,SECONDS); 
    if (controller_1.buttonR2.pressing()): 
        motor_10_front.spin_for(FORWARD,90,DEGREES,wait=False); 
        brain.screen.set_cursor(10,10); 
        brain.screen.print("10 Front"); 
        wait(0.5,SECONDS);  
 
    # Code that allows each button to slightly correct the position of the motor in case it is slightly 
offset after a turn 
    if (bumper_a_top.pressing()): 
        motor_14_top.spin_for(FORWARD,10,DEGREES,wait=False); 
    if (bumper_d_bottom.pressing()): 
        motor_16_bottom.spin_for(FORWARD,10,DEGREES,wait=False); 
    if (bumper_b_left.pressing()): 
        motor_6_left.spin_for(FORWARD,10,DEGREES,wait=False);   
    if (bumper_c_right.pressing()): 
        motor_5_right.spin_for(FORWARD,10,DEGREES,wait=False); 
    if (bumper_e_front.pressing()): 
        motor_10_front.spin_for(FORWARD,10,DEGREES,wait=False); 
    if (bumper_f_end.pressing()): 
        motor_8_end.spin_for(FORWARD,10,DEGREES,wait=False); 
 
    #Code that randomly scrambles the cube so that a random side is rotated a random direction 
# every time the button is pressed. It finds a random number and matches it to an if statement 
    if (bumper_g_scramble.pressing()): 
        rand = random.randint(1,12); 
        if (rand == 1): 
            motor_14_top.spin_for(FORWARD,90,DEGREES,wait=False); 
            actionHistory.insert(ind,1); 
            ind += 1; 
            wait(0.5,SECONDS); 
        elif (rand == 2): 
            motor_14_top.spin_for(REVERSE,90,DEGREES,wait=False); 
            actionHistory.insert(ind,2); 
            ind += 1; 
            wait(0.5,SECONDS); 
        elif (rand == 3): 
            motor_16_bottom.spin_for(FORWARD,90,DEGREES,wait=False); 
            actionHistory.insert(ind,3); 
            ind += 1; 
            wait(0.5,SECONDS); 
        elif (rand == 4): 
            motor_16_bottom.spin_for(REVERSE,90,DEGREES,wait=False); 
            actionHistory.insert(ind,4); 
            ind += 1; 
            wait(0.5,SECONDS); 
        elif (rand == 5): 
            motor_8_end.spin_for(FORWARD,90,DEGREES,wait=False); 
            actionHistory.insert(ind,5); 
            ind += 1; 
            wait(0.5,SECONDS);   
        elif (rand == 6): 
            motor_8_end.spin_for(REVERSE,90,DEGREES,wait=False); 
            actionHistory.insert(ind,6); 
            ind += 1; 
            wait(0.5,SECONDS);  
        elif (rand == 7): 
            motor_5_right.spin_for(FORWARD,90,DEGREES,wait=False); 
            actionHistory.insert(ind,7); 
            ind += 1; 
            wait(0.5,SECONDS); 
        elif (rand == 8): 
            motor_5_right.spin_for(REVERSE,90,DEGREES,wait=False); 
            actionHistory.insert(ind,8); 
            ind += 1; 
            wait(0.5,SECONDS);      
        elif (rand == 9): 
            motor_6_left.spin_for(FORWARD,90,DEGREES,wait=False); 
            actionHistory.insert(ind,9); 
            ind += 1; 
            wait(0.5,SECONDS); 
        elif (rand == 10): 
            motor_6_left.spin_for(REVERSE,90,DEGREES,wait=False); 
            actionHistory.insert(ind,10); 
            ind += 1; 
            wait(0.5,SECONDS);    
        elif (rand == 11): 
            motor_10_front.spin_for(FORWARD,90,DEGREES,wait=False); 
            actionHistory.insert(ind,11); 
            ind += 1; 
            wait(0.5,SECONDS); 
        elif (rand == 12): 
            motor_10_front.spin_for(REVERSE,90,DEGREES,wait=False); 
            actionHistory.insert(ind,12); 
            ind += 1; 
            wait(0.5,SECONDS); 
        else: 
            pass; 
 
    #The scramble code adds each scramble number to an array and the solve method reads the 
#array then does the opposite of what each number movement corresponds to, to undo what 
#the scramble method did and “solve” the cube. It reads from the array then removes the 
#number. 
    if (bumper_h_solve.pressing()): 
        if (actionHistory[0] == 1): 
            motor_14_top.spin_for(REVERSE,90,DEGREES,wait=False); 
            del actionHistory[0];  
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 2): 
            motor_14_top.spin_for(FORWARD,90,DEGREES,wait=False);  
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 3): 
            motor_16_bottom.spin_for(REVERSE,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 4): 
            motor_16_bottom.spin_for(FORWARD,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 5): 
            motor_8_end.spin_for(REVERSE,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 6): 
            motor_8_end.spin_for(FORWARD,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 7): 
            motor_5_right.spin_for(REVERSE,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 8): 
            motor_5_right.spin_for(FORWARD,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 9): 
            motor_6_left.spin_for(REVERSE,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 10): 
            motor_6_left.spin_for(FORWARD,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 11): 
            motor_10_front.spin_for(REVERSE,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS); 
        elif (actionHistory[0] == 12): 
            motor_10_front.spin_for(FORWARD,90,DEGREES,wait=False); 
            del actionHistory[0]; 
            wait(0.5,SECONDS);                                     
 
    #This clears the screen of the brain from everything if nothing is happening because when     
# each button is pressed it displays on the screen saying it is being pressed. 
    else: 
        brain.screen.clear_screen();