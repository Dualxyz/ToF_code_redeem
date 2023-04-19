import pyautogui;
from random import *;
import time;
import pyperclip;

# coordinates - hardcoded
x_or_cp_coordinates_up_x = 3646;
x_or_cp_coordinates_up_y = 450;
x_or_cp_coordinates_down_x = 3668;
x_or_cp_coordinates_down_y = 469;

confirm_up_x = 3249;
confirm_up_y = 585;
confirm_down_x = 3478;
confirm_down_y = 628;

ok_up_x = 3015;
ok_up_y = 546;
ok_down_x = 3358;
ok_down_y = 613;

def load_codes():
    with open('codes.txt','r') as f:
        code_list = [];
        lines = f.readlines();
        for smt in lines:
            code_list.append(smt.strip("\n"));
            
    return code_list;
    
#Nearly useless function. 1920 is my resolution and since it's on the 2nd monitor I needed to do this (=
def check_x(x):
    if x >= 1920:
        return x - 1920;
    return x;
    
def obfuscate_and_click(x_up, y_up, x_down, y_down):    
    random_x = randrange(check_x(x_up), check_x(x_down));
    random_y = randrange(y_up, y_down);
    
    # pyautogui code
    pyautogui.moveTo(random_x, random_y, uniform(0.4, 1.7), pyautogui.easeInOutQuad);
    pyautogui.click();
    # end pyautogui code
    
    #print(str(random_x) + " " + str(random_y));
    

if __name__ == "__main__":
    code_list = load_codes();
    print(code_list);
    
    for code in code_list:
        pyperclip.copy(code);

        obfuscate_and_click(x_or_cp_coordinates_up_x, x_or_cp_coordinates_up_y, x_or_cp_coordinates_down_x, x_or_cp_coordinates_down_y);    #click on the paste button
        obfuscate_and_click(confirm_up_x, confirm_up_y, confirm_down_x, confirm_down_y);                                                    #comfirm button
        time.sleep(2);                                                                                                                      #Sleep cz I'm too lazy to do img scanning
        obfuscate_and_click(ok_up_x, ok_up_y, ok_down_x, ok_down_y);                                                                        #click on ok button
        obfuscate_and_click(x_or_cp_coordinates_up_x, x_or_cp_coordinates_up_y, x_or_cp_coordinates_down_x, x_or_cp_coordinates_down_y);    #remove the code from input field
    