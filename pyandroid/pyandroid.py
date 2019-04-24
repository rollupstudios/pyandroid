#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

Global functions implemented ::

Locks the screen
Bringing Home screen
Executing Back command
Typing Number/Letter
Typing Paragraph
Deleting text with count of letters
Volume Up/Down/Mute
Brightness Up/Down
Finds device screen brightness level
Device Sleep/Wakeup/Power/Restart
To find device in restart mode or come to normal mode
Applying Swipe/Tap
Getting Device Properties
Getting Device Resolution
Keep Device Screen in Portrait mode
Bringing Settings Screen
Creates a directory in device
Clearing/Fetching adb log from device
Deletes all the files in a directory
Pushes a file from Test PC into dev directory
Pulls a file from device to Test PC
Take screenshot of device and saves in device
Records screen of device and saves in device
Pulls down notification in device
Finds model number of a device
Dumps audio playback log

Bluetooth Enable/Disable/Screen Bringing/Kill Process

WiFi Enable/Disable

Voice Call Initiate/Terminate/Attend

Camera Open
Camera Close

Music Play Single Song
Music Player Open/Play/Pause/Stop/Play Next Song
VLC Player Open

Open a URL

Open sound recorder



'''

import os, sys, time, datetime
import subprocess, signal
from datetime import *
from time import *

pyAndroid_SUCCESS_CODE    = 0
pyAndroid_ERROR_CODE      = -1
pyAndroid_WAIT_CODE       = 2

# lookup keywords for getting device properties
pyAndroid_DeviceDisplayDimension = "mUnrestrictedScreen"

# assigns execution wait period in seconds
pyAndroid_DUT_ACTION_WAIT_SECS = 3

# assigns execution wait period in seconds, for DUT to come to normal mode after restart.
pyAndroid_DUT_RESTART_SECS = 60

# assigns task number. used for counting the tasks performed in the log file
pyAndroid_TASK_NO = 1

pyAndroid_ACTION_WAIT_SECONDS = 3
pyAndroid_ACTION_WAIT_SECONDS_NOTIFICATION = 1

# declares log file.
TestFwkExecLogFile = "TestFwkExecLogFile.txt"

# assigns log file path to BT_Auto_log_file.
TestFwkLogFileHandle = open(TestFwkExecLogFile, "a")


'''    
# ******
Function           :    LogFileWrite
Purpose            :    Called to write logs in the log file
Input Arguments    :    msg        : log to be written in the log file
Return             :    pyAndroid_SUCCESS_CODE : if all tasks complete as expected
# ******
'''

'''
def LogFileWrite(msg):
    global pyAndroid_TASK_NO
    TestFwkLogFileHandle.write(str(pyAndroid_TASK_NO)+"\t"+str(datetime.now())+"\t\t"+msg+"\n")
    TestFwkLogFileHandle.flush()
    pyAndroid_TASK_NO += 1
    return pyAndroid_SUCCESS_CODE
'''

class GlobalAndroidFunctions(object):

    def __init__(self):
        pass
    
    def log_file_test_init(self, msg):
        TestFwkLogFileHandle.write(msg+"\n")
        TestFwkLogFileHandle.flush()
        return pyAndroid_SUCCESS_CODE

	def LogFileWrite(msg):
    	global pyAndroid_TASK_NO
    	TestFwkLogFileHandle.write(str(pyAndroid_TASK_NO)+"\t"+str(datetime.now())+"\t\t"+msg+"\n")
    	TestFwkLogFileHandle.flush()
    	pyAndroid_TASK_NO += 1
    	return pyAndroid_SUCCESS_CODE    

    def LockScreen(self, device_id):
        home_cmd_device = "adb -s "+device_id+" shell input keyevent 26"
        try:
            LogFileWrite("Start Action:: SUCCESS : Locks Screen on Device with Device id: "+ device_id)
            os.system(home_cmd_device)            
            LogFileWrite("End Action:: SUCCESS : Locks Screen on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Locks Screen on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE


    def ShowHomeScreen(self, device_id):
        home_cmd_device = "adb -s "+device_id+" shell input keyevent KEYCODE_HOME"
        try:
            LogFileWrite("Start Action:: SUCCESS : Brings HOME Screen on Device with Device id: "+ device_id)
            os.system(home_cmd_device)            
            LogFileWrite("End Action:: SUCCESS : Brings HOME Screen on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Brings HOME Screen on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def ExecuteBackCommand(self, device_id):
        adb_cmd_device_back = "adb -s "+device_id+" shell input keyevent KEYCODE_BACK"
        try:
            LogFileWrite("Start Action:: SUCCESS : Back command on Device with Device id: "+ device_id)
            os.system(adb_cmd_device_back)            
            LogFileWrite("End Action:: SUCCESS : Back command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Back command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
        
    def PressNumberLetter(self, device_id, character):

        character_adbCharacter = {
            "0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9",

            "a":"A", "b":"B", "c":"C", "d":"D", "e":"E", "f":"F", "g":"G", "h":"H", "i":"I", "j":"J",
            "k":"K", "l":"L", "m":"M", "n":"N", "o":"O", "p":"P", "q":"Q", "r":"R", "s":"S", "t":"T",
            "u":"U", "v":"V", "w":"W", "x":"X", "y":"Y", "z":"Z",

            "+" : "PLUS", "-" : "MINUS", "*" : "STAR", "/" : "SLASH",  
            
            "," : "COMMA", "." : "PERIOD", "=" : "EQUALS", "`" : "GRAVE", ";" : "SEMICOLON", 
            "#" : "POUND", "]" : "RIGHT_BRACKET", "[" : "LEFT_BRACKET", "\\": "BACKSLASH",
            "'" : "APOSTROPHE",
            
            " " : "SPACE",  "BACKSPACE" : "DEL", "DEL" : "FORWARD_DEL",
            "ENTER" : "ENTER", "TAB" : "TAB",
            }
        
        
        adb_cmd_type ="adb -s "+device_id+" shell input keyevent KEYCODE_"+character_adbCharacter[character]
        try:
            LogFileWrite("Start Action:: SUCCESS : Types "+character+" on Device with Device id: "+ device_id)
            os.system(adb_cmd_type)
            LogFileWrite("End Action:: SUCCESS : Types "+character+" on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Types "+character+" on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def TypeText(self, device_id, text):
        printable_text = text.replace(" ", "%s")
        adb_cmd_type = "adb -s "+device_id+" shell input text "+ printable_text
        try:
            LogFileWrite("Start Action:: SUCCESS : Types "+text+" on Device with Device id: "+ device_id)
            os.system(adb_cmd_type)
            LogFileWrite("End Action:: SUCCESS : Types "+text+" on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Types "+text+" on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def DeleteText(self, device_id, text_chars_count):
        adb_cmd_del1 = "adb -s "+device_id+" shell input keyevent KEYCODE_MOVE_END"
        try:
            LogFileWrite("Start Action:: SUCCESS : Moves cursor at end of textarea on Device with Device id: "+ device_id)
            os.system(adb_cmd_del1)
            LogFileWrite("End Action:: SUCCESS : Moves cursor at end of textarea on Device with Device id: "+ device_id+"\n")
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Moves cursor at end of textarea on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

        adb_cmd_del2 = "adb -s "+device_id+" shell input keyevent KEYCODE_DEL"
        try:
            for i in range(int(text_chars_count)):
                LogFileWrite("Start Action:: SUCCESS : Deletes "+str(i)+" character on Device with Device id: "+ device_id)
                os.system(adb_cmd_del2)
                LogFileWrite("End Action:: SUCCESS : Deletes "+str(i)+" character on Device with Device id: "+ device_id+"\n")                
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Deletes "+str(i)+" character on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE


    def VolumeUp(self, device_id):
        adb_cmd_volume_up = "adb -s "+device_id+" shell input keyevent KEYCODE_VOLUME_UP"
        try:
            LogFileWrite("Start Action:: SUCCESS : Increases Volume on Device with Device id: "+ device_id)
            os.system(adb_cmd_volume_up)            
            LogFileWrite("End Action:: SUCCESS : Increases Volume on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:        	
            LogFileWrite("End Action:: FAILED : Increases Volume on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def VolumeDown(self, device_id):
        adb_cmd_volume_down = "adb -s "+device_id+" shell input keyevent KEYCODE_VOLUME_DOWN"
        try:
            LogFileWrite("Start Action:: SUCCESS : Decreases Volume on Device with Device id: "+ device_id)
            os.system(adb_cmd_volume_down)            
            LogFileWrite("End Action:: SUCCESS : Decreases Volume on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Decreases Volume on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def VolumeMute(self, device_id):
        adb_cmd_volume_mute = "adb -s "+device_id+" shell input keyevent KEYCODE_VOLUME_MUTE"
        try:
            LogFileWrite("Start Action:: SUCCESS : Mutes Volume on Device with Device id: "+ device_id)
            os.system(adb_cmd_volume_mute)            
            LogFileWrite("End Action:: SUCCESS : Mutes Volume on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Mutes Volume on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def BrightnessUp(self, device_id):
        adb_cmd_brightness_up = "adb -s "+device_id+" shell input keyevent KEYCODE_BRIGHTNESS_UP"
        try:
            LogFileWrite("Start Action:: SUCCESS : Increases Brightness on Device with Device id: "+ device_id)
            os.system(adb_cmd_brightness_up)            
            LogFileWrite("End Action:: SUCCESS : Increases Brightness on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Increases Brightness on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def BrightnessDown(self, device_id):
        adb_cmd_brightness_down = "adb -s "+device_id+" shell input keyevent KEYCODE_BRIGHTNESS_DOWN"
        try:
            LogFileWrite("Start Action:: SUCCESS : Decreases Brightness on Device with Device id: "+ device_id)
            os.system(adb_cmd_brightness_down)            
            LogFileWrite("End Action:: SUCCESS : Decreases Brightness on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Decreases Brightness on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def GetBrightnessLevel(self, device_id):
        adb_cmd_get_brightness_level = "adb -s "+device_id+" shell cat /sys/devices/platform/pwm-backlight.0/backlight/pwm-backlight.0/brightness"
        try:
            LogFileWrite("Start Action:: SUCCESS : Gets Brightness level on Device with Device id: "+ device_id)            
            ret = subprocess.check_output(adb_cmd_get_brightness_level, shell=True)
            ret = ret.decode('ascii')
            ret = ((ret.rstrip()).lstrip()).split(" ")             
            LogFileWrite("End Action:: SUCCESS :Gets Brightness level  on Device with Device id: "+ device_id+"\n")
            return [pyAndroid_SUCCESS_CODE, int(ret[0])]
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Gets Brightness level  on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def DeviceSleep(self, device_id):
        adb_cmd_device_sleep = "adb -s "+device_id+" shell input keyevent KEYCODE_SLEEP"
        try:
            LogFileWrite("Start Action:: SUCCESS : Sleep command on Device with Device id: "+ device_id)
            os.system(adb_cmd_device_sleep)            
            LogFileWrite("End Action:: SUCCESS : Sleep command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Sleep command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def DeviceWakeUp(self, device_id):
        adb_cmd_device_wakeup = "adb -s "+device_id+" shell input keyevent KEYCODE_WAKEUP"
        try:
            LogFileWrite("Start Action:: SUCCESS : Wakeup command on Device with Device id: "+ device_id)
            os.system(adb_cmd_device_wakeup)            
            LogFileWrite("End Action:: SUCCESS : Wakeup command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Wakeup command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
    
    def DevicePower(self, device_id):
        adb_cmd_device_power = "adb -s "+device_id+" shell input keyevent KEYCODE_POWER"
        try:
            LogFileWrite("Start Action:: SUCCESS : Power command on Device with Device id: "+ device_id)
            os.system(adb_cmd_device_power)            
            LogFileWrite("End Action:: SUCCESS : Power command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Power command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def DeviceRestart(self, device_id):
        adb_cmd_reboot = "adb -s "+device_id+" reboot"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Reboot command on Device with Device id: "+ device_id)
            os.system(adb_cmd_reboot)
            sleep(pyAndroid_DUT_RESTART_SECS)
            LogFileWrite("End Action:: SUCCESS : Reboot command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Reboot command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def DeviceRestartRoot(self, device_id):
        adb_cmd_reboot_root = "adb -s "+device_id+" root"
        get_dev_state_cmd_dut = "adb -s "+device_id+" shell dumpsys battery"
        
        try:
            LogFileWrite("Start Action:: SUCCESS : Reboot in root mode command on Device with Device id: "+ device_id)
            os.system(adb_cmd_reboot_root)
            sleep(pyAndroid_DUT_RESTART_SECS)            
            LogFileWrite("End Action:: SUCCESS : Reboot in root mode command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Reboot in root mode command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def DeviceCheckAfterReboot(self, device_id):
        adb_cmd_after_reboot = "adb -s "+device_id+" shell dumpsys battery"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Checks after reboot state on Device with Device id: "+ device_id)            
            dev_status_after_reboot = subprocess.check_output(adb_cmd_after_reboot, shell=True)
            sleep(pyAndroid_DUT_RESTART_SECS)
            if 'USB powered' in dev_status_after_reboot:
                LogFileWrite("End Action:: SUCCESS : Checks after reboot state on Device with Device id: "+ device_id+"\n")
                return pyAndroid_SUCCESS_CODE
            else:
                return pyAndroid_WAIT_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Checks after reboot state on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE


    def ApplySwipe(self, device_id, x_one, y_one, x_two, y_two, printable_text, duration_ms=100):
        adb_cmd_apply_swipe = "adb -s "+device_id+" shell input swipe "+str(x_one)+" "+str(y_one)+" "+str(x_two)+" "+str(y_two)+" "+str(duration_ms)        
        try:
            LogFileWrite("Start Action:: SUCCESS : Applying swipe command on Device with Device id: "+ device_id +" from ("+str(x_one)
                           +" , "+str(y_one)+") to ("+str(x_two)+" , "+str(y_two)+") co-ordinates within "+str(duration_ms)+" ms time"+printable_text)
            os.system(adb_cmd_apply_swipe)            
            LogFileWrite("End Action:: SUCCESS : Applying swipe command on Device with Device id: "+ device_id +" from ("+str(x_one)
                           +" , "+str(y_one)+") to ("+str(x_two)+" , "+str(y_two)+") co-ordinates within "+str(duration_ms)+" ms time"+printable_text+"\n")

            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Applying swipe command on Device with Device id: "+ device_id +" from ("+str(x_one)
                           +" , "+str(y_one)+") to ("+str(x_two)+" , "+str(y_two)+") co-ordinates within "+str(duration_ms)+" ms time"+printable_text+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
        

    def ApplyTap(self, device_id, x_pos, y_pos, printable_text):
        adb_cmd_apply_tap = "adb -s "+device_id+" shell input tap "+str(x_pos)+" "+str(y_pos)
        try:
            LogFileWrite("Start Action:: SUCCESS : Applying tap command on Device with Device id: "+ device_id +" at ("+str(x_pos)
                           +" , "+str(y_pos)+")"+printable_text)
            os.system(adb_cmd_apply_tap)            
            LogFileWrite("End Action:: SUCCESS : Applying tap command on Device with Device id: "+ device_id +" at ("+str(x_pos)
                           +" , "+str(y_pos)+")"+printable_text+"\n")

            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Applying tap command on Device with Device id: "+ device_id +" at ("+str(x_pos)
                           +" , "+str(y_pos)+")"+printable_text+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")

            return pyAndroid_ERROR_CODE

    def GetDeviceProperties(self, device_id):
        cmd = "adb -s "+device_id+" shell dumpsys window > deviceProperties_"+device_id+".txt"
        try:
            LogFileWrite("Start Action:: SUCCESS : Getting Device Properties for Device with Device id: "+ device_id)
            os.system(cmd)
            LogFileWrite("End Action:: SUCCESS : Getting Device Properties for Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Getting Device Properties for Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
        
    def GetDeviceResolution(self, device_id):
        cmd = "adb -s "+device_id+" shell dumpsys window | grep \"mOverscanScreen\""
        try:
            LogFileWrite("Start Action:: SUCCESS : Getting Device Properties for Device with Device id: "+ device_id)            
            dev_resolution_out = subprocess.check_output(cmd, shell=True)                
            dev_resolution_out = dev_resolution_out.decode('ascii')
            list_dev_res = ((dev_resolution_out.rstrip()).lstrip()).split(" ")            
            LogFileWrite("End Action:: SUCCESS : Getting Device Properties for Device with Device id: "+ device_id+"\n")
            return list_dev_res[1].split("x")
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Getting Device Properties for Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def MakeScreenPortrait(self, device_id):
        adb_cmd_keep_portrait ="adb -s "+device_id+" shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0"
        try:
            LogFileWrite("Start Action:: SUCCESS : Force screen to portrait mode on Device with Device id: "+ device_id)
            os.system(adb_cmd_keep_portrait)
            LogFileWrite("End Action:: SUCCESS : Force screen to portrait mode on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE                        
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Force screen to portrait mode on Device with Device id: "+ device_id)
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def ShowSettingsScreen(self, device_id):
        settings_cmd_device = "adb -s "+device_id+" shell am start -a android.settings.SETTINGS"
        try:
            LogFileWrite("Start Action:: SUCCESS : Brings SETTINGS Screen on Device with Device id: "+ device_id)
            os.system(settings_cmd_device)            
            LogFileWrite("End Action:: SUCCESS : Brings SETTINGS Screen on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Brings SETTINGS Screen on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def CreateDir(self, device_id, directory_path):
        adb_cmd_createdir = "adb -s "+device_id+" shell mkdir "+ directory_path
        try:
            LogFileWrite("Start Action:: SUCCESS : Creates the directory "+directory_path+" on Device with Device id: "+ device_id)
            os.system(adb_cmd_createdir)
            LogFileWrite("End Action:: SUCCESS : Creates the directory "+directory_path+" on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Creates the directory "+directory_path+" on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
        
        
    def ClearsDevLog(self, device_id):
        clears_log_device = "adb -s "+device_id+" shell logcat -c"
        try:
            LogFileWrite("Start Action:: SUCCESS : Clears log on Device with Device id: "+ device_id)
            os.system(clears_log_device)
            LogFileWrite("End Action:: SUCCESS : Clears log on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Clears log on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def FetchesDevLog(self, device_id, out_file, dict_tag_priority=None):
        fetch_log_adb_cmd = "adb -s "+device_id+" shell logcat -d "
        fetch_log_adb_cmd_suffix = " > "+out_file

        if dict_tag_priority != None:
            for key, value in dict_tag_priority.iteritems():
                fetch_log_adb_cmd += " "+key+":"+value

        fetch_log_adb_cmd += fetch_log_adb_cmd_suffix
        
        try:
            LogFileWrite("Start Action:: SUCCESS : Fetches log on Device with Device id: "+ device_id+" to write on "+out_file)
            os.system(fetch_log_adb_cmd)            
            LogFileWrite("End Action:: SUCCESS : Fetches log on Device with Device id: "+ device_id+" to write on "+out_file+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Fetches log on Device with Device id: "+ device_id+" to write on "+out_file+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def DeleteFilesinDev(self, device_id, directory_path):
        clears_log_device = "adb -s "+device_id+" shell rm -r "+ directory_path
        try:
            LogFileWrite("Start Action:: SUCCESS : Deletes all the files on Device with Device id: "+ device_id+" in directory "+directory_path)
            os.system(clears_log_device)
            LogFileWrite("End Action:: SUCCESS : Deletes all the files on Device with Device id: "+ device_id+" in directory "+directory_path+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Deletes all the files on Device with Device id: "+ device_id+" in directory "+directory_path+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def PushFiletoDev(self, device_id, file_path, dev_directory_path):
        push_file_dev = "adb -s "+device_id+" push "+file_path+" "+dev_directory_path        
        try:
            LogFileWrite("Start Action:: SUCCESS : Pushes "+file_path+" on Device with Device id: "+ device_id+" in directory "+dev_directory_path)
            os.system(push_file_dev)
            LogFileWrite("End Action:: SUCCESS : Pushes "+file_path+" on Device with Device id: "+ device_id+" in directory "+dev_directory_path+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Pushes "+file_path+" on Device with Device id: "+ device_id+" in directory "+dev_directory_path+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def PullFilefromDev(self, device_id, dev_file_path, test_pc_directory_path):
        pull_file_dev = "adb -s "+device_id+" pull "+dev_file_path+" "+test_pc_directory_path
        try:
            LogFileWrite("Start Action:: SUCCESS : Pulls "+dev_file_path+" on Device with Device id: "+ device_id+" to directory "+test_pc_directory_path)
            os.system(pull_file_dev)
            LogFileWrite("End Action:: SUCCESS : Pulls "+dev_file_path+" on Device with Device id: "+ device_id+" to directory "+test_pc_directory_path+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Pulls "+dev_file_path+" on Device with Device id: "+ device_id+" to directory "+test_pc_directory_path+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def RenameTestPCFolder(self, folder_old_name, folder_new_name):
        try:
            LogFileWrite("Start Action:: SUCCESS : Renames folder "+folder_old_name+" into "+folder_new_name)
            os.rename(folder_old_name, folder_new_name)
            LogFileWrite("End Action:: SUCCESS : Renames folder "+folder_old_name+" into "+folder_new_name+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Renames folder "+folder_old_name+" into "+folder_new_name+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
        
    def ScreenCaptureDevice(self, device_id, directory_path):
        captures_screen_device = "adb -s "+device_id+" shell screencap -p "+directory_path
        try:
            LogFileWrite("Start Action:: SUCCESS : Captures screen on Device with Device id: "+ device_id+" in directory "+directory_path)
            os.system(captures_screen_device)
            LogFileWrite("End Action:: SUCCESS : Captures screen on Device with Device id: "+ device_id+" in directory "+directory_path+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Captures screen on Device with Device id: "+ device_id+" in directory "+directory_path+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def ScreenRecordDevice(self, device_id, directory_path):
        records_screen_device = "adb -s "+device_id+" shell screenrecord -p "+directory_path
        try:
            LogFileWrite("Start Action:: SUCCESS : Records screen on Device with Device id: "+ device_id+" in directory "+directory_path)
            os.system(records_screen_device)
            LogFileWrite("End Action:: SUCCESS : Records screen on Device with Device id: "+ device_id+" in directory "+directory_path+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Records screen on Device with Device id: "+ device_id+" in directory "+directory_path+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def ShowNotification(self, device_id, size_x, size_y):
        adb_cmd_show_notification = "adb -s "+device_id+" shell input swipe "+str(int(size_x)/2)+" 0 "+str(int(size_x)/2)+" "+size_y
        try:
            LogFileWrite("Start Action:: SUCCESS : Brings notification on Device with Device id: "+ device_id)
            os.system(adb_cmd_show_notification)
            LogFileWrite("End Action:: SUCCESS : Brings notification on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Brings notification on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def FindModelNumbers(self):
        adb_model_no_cmd = "adb devices -l"
        try:
            LogFileWrite("Start Action:: SUCCESS : Tries to find out model numbers of all connected devices")
            dev_info_out = subprocess.check_output(adb_model_no_cmd, shell=True)            
            LogFileWrite("End Action:: SUCCESS : Tries to find out model numbers of all connected devices")            
            l1 = dev_info_out.split('\n')

            listx = [x for x in l1 if x != ""]
            listy = [x for x in listx if x != "\r"]
            only_dev = listy[1:]

            dev_model_no = {}
            
            for i in range(len(only_dev)):
                dev_info = only_dev[i]                
                l_dev_info = ((dev_info.rstrip()).lstrip()).split(" ")
                m_no = [x for x in l_dev_info if x != ""][-2].split(':')[-1]
                dev_model_no[[x for x in l_dev_info if x != ""][0]] = m_no
                
            return [dev_model_no, pyAndroid_SUCCESS_CODE]
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Tries to find out model numbers of all connected devices")         
            LogFileWrite("Exception message: "+ str(e)+".\n")   
            return [{}, pyAndroid_ERROR_CODE]

    

    def FindAudioPlayback(self, device_id, dump_log_file):
        adb_dumps_audio_playback_cmd = "adb -s "+device_id+" shell dumpsys audio"
        try:
            LogFileWrite("Start Action:: SUCCESS : Tries to find out audio is playing or not with Device id: "+device_id+"\n")
            audio_playback_dump = subprocess.check_output(adb_dumps_audio_playback_cmd, shell=True)
            LogFileWrite("End Action:: SUCCESS : Tries to find out audio is playing or not with Device id: "+device_id+"\n")
            
            file_in = open(dump_log_file, "w")
            file_in.write(audio_playback_dump)
            file_in.close()

            return pyAndroid_SUCCESS_CODE
            
            #if "com.google.android.music" in audio_playback_dump:
                #return ["PLAYING", pyAndroid_SUCCESS_CODE]
            #else:
                #return ["NOT_PLAYING", pyAndroid_SUCCESS_CODE]
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Tries to find out audio is playing or not with Device id: "+device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
            #return ["ERROR", pyAndroid_ERROR_CODE]

        
        
        
    ### BLUETOOTH OPERATIONS
    
    def BluetoothEnable(self, device_id):
        adb_cmd_bt_enable = "adb -s "+device_id+" shell service call bluetooth_manager 6"        
        try:
            LogFileWrite("Start Action:: SUCCESS : BT Enable command on Device with Device id: "+ device_id)
            os.system(adb_cmd_bt_enable)            
            LogFileWrite("End Action:: SUCCESS : BT Enable command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : BT Enable command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def BluetoothDisable(self, device_id):
        adb_cmd_bt_disable = "adb -s "+device_id+" shell service call bluetooth_manager 8"        
        try:
            LogFileWrite("Start Action:: SUCCESS : BT Disable command on Device with Device id: "+ device_id)
            os.system(adb_cmd_bt_disable)            
            LogFileWrite("End Action:: SUCCESS : BT Disable command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : BT Disable command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def BluetoothScreenBringup(self, device_id):
        adb_cmd_bt_screen_bringup = "adb -s "+device_id+" shell am start -a android.settings.BLUETOOTH_SETTINGS"        
        try:
            LogFileWrite("Start Action:: SUCCESS : BT Screen bringup command on Device with Device id: "+ device_id)
            os.system(adb_cmd_bt_screen_bringup)            
            LogFileWrite("End Action:: SUCCESS : BT Screen bringup command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : BT Screen bringup command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def BluetoothKill(self, device_id):
        adb_cmd_bt_kill = "adb -s "+device_id+" shell am force-stop com.android.bluetooth"        
        try:
            LogFileWrite("Start Action:: SUCCESS : BT kill command on Device with Device id: "+ device_id)
            os.system(adb_cmd_bt_kill)            
            LogFileWrite("End Action:: SUCCESS : BT kill command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : BT kill command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE


    ### WIFI OPERATIONS
    
    def WifiEnable(self, device_id):
        adb_cmd_wifi_enable = "adb -s "+device_id+" shell svc wifi enable"        
        try:
            LogFileWrite("Start Action:: SUCCESS : WiFi Enable command on Device with Device id: "+ device_id)
            os.system(adb_cmd_wifi_enable)            
            LogFileWrite("End Action:: SUCCESS : WiFi Enable command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : WiFi Enable command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def WifiDisable(self, device_id):
        adb_cmd_wifi_disable = "adb -s "+device_id+" shell svc wifi disable"        
        try:
            LogFileWrite("Start Action:: SUCCESS : WiFi Disable command on Device with Device id: "+ device_id)
            os.system(adb_cmd_wifi_disable)            
            LogFileWrite("End Action:: SUCCESS : WiFi Disable command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : WiFi Disable command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE


    ### CALL OPERATIONS

    def CallInitiate(self, device_id, external_number):
        adb_cmd_call_initiate = "adb -s "+device_id+" shell am start -a android.intent.action.CALL tel:"+external_number        
        try:
            LogFileWrite("Start Action:: SUCCESS : Initiating call command by Device with Device id: "+ device_id+" to "+external_number)
            os.system(adb_cmd_call_initiate)            
            LogFileWrite("End Action:: SUCCESS : Initiating call command by Device with Device id: "+ device_id+" to "+external_number+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Initiating call command by Device with Device id: "+ device_id+" to "+external_number+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def CallAttend(self, device_id):
        adb_cmd_incoming_call_attend = "adb -s "+device_id+" shell input keyevent KEYCODE_CALL"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Attending incoming call command on Device with Device id: "+ device_id)
            os.system(adb_cmd_incoming_call_attend)            
            LogFileWrite("End Action:: SUCCESS : Attending incoming call command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Attending incoming call command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
        
    def CallTerminate(self, device_id):
        adb_cmd_call_terminate = "adb -s "+device_id+" shell input keyevent KEYCODE_ENDCALL"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Terminating on-going call command on Device with Device id: "+ device_id)
            os.system(adb_cmd_call_terminate)            
            LogFileWrite("End Action:: SUCCESS : Terminating on-going call command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Terminating on-going call command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE


    def CheckCalliscoming(self, device_id):
        adb_cmd_check_call_coming = "adb -s "+device_id+" shell dumpsys telephony.registry | findstr \"mCallState\""
        try:
            LogFileWrite("Start Action:: SUCCESS : Checking WAN call is coming on Device with Device id: "+ device_id)
            callstatedut = subprocess.check_output(adb_cmd_check_call_coming, shell=True)
            LogFileWrite("End Action:: SUCCESS : Checking WAN call is coming on Device with Device id: "+ device_id+"\n")
            return [callstatedut, pyAndroid_SUCCESS_CODE]
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Checking WAN call is coming on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return [-1, pyAndroid_ERROR_CODE]

    ### CAMERA OPERATIONS

    def OpenCamera(self, device_id):
        adb_cmd_camera = "adb -s "+device_id+" shell input keyevent KEYCODE_CAMERA"
        try:
            LogFileWrite("Start Action:: SUCCESS : Brings Camera on Device with Device id: "+ device_id)
            os.system(adb_cmd_camera)            
            LogFileWrite("End Action:: SUCCESS : Brings Camera on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Brings Camera on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE        

    def CloseCamera(self, device_id):
        adb_cmd_camera = "adb -s "+device_id+" shell am force-stop org.codeaurora.snapcam"
        try:
            LogFileWrite("Start Action:: SUCCESS : Closes Camera on Device with Device id: "+ device_id)
            os.system(adb_cmd_camera)            
            LogFileWrite("End Action:: SUCCESS : Closes Camera on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Closes Camera on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE        

    ### MUSIC OPERATIONS

    # This method opens the audio stream in 'view' mode and not in 'play'mode.
    # So, the audio will not be played in player, but in a separate app.
    # The difference is, we can't play more than one song in the viewer app and can't be looped.
    # So, for a single audio playback and for only one time, we call this method.
    
    def MusicPlaySingleSong(self, device_id, music_path, music_type):
        adb_cmd_play_single_song = "adb -s "+device_id+" shell am start -a android.intent.action.VIEW -d file:"+music_path+" -t audio/"+music_type
        try:
            LogFileWrite("Start Action:: SUCCESS : Playing single song command on Device with Device id: "+ device_id+" for song "+ music_path)
            os.system(adb_cmd_play_single_song)            
            LogFileWrite("End Action:: SUCCESS : Playing single song command on Device with Device id: "+ device_id+" for song "+ music_path+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Playing single song command on Device with Device id: "+ device_id+" for song "+ music_path+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    # This method opens the default Google Play Music app.
    # The pre-condition is some audio streams should be present in the internal or SDCard memory, beforehand.
    # So, when we give the Play command, the recently played stream will start playing.
    
    def MusicOpenPlayer(self, device_id):
        adb_cmd_open_music_player = "adb -s "+device_id+" shell am start -a android.intent.action.MUSIC_PLAYER"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Opening Music Player command on Device with Device id: "+ device_id)
            os.system(adb_cmd_open_music_player)            
            LogFileWrite("End Action:: SUCCESS : Opening Music Player command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Opening Music Player command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def MusicOpenNewPlayer(self, device_id):
        adb_cmd_open_music_player = "adb -s "+device_id+" shell monkey -p media.audioplayer.musicplayer -c android.intent.category.LAUNCHER 1"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Opening Music Player command on Device with Device id: "+ device_id)
            os.system(adb_cmd_open_music_player)            
            LogFileWrite("End Action:: SUCCESS : Opening Music Player command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Opening Music Player command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def MusicPlayOnPlayer(self, device_id):
        adb_cmd_play_music_player = "adb -s "+device_id+" shell input keyevent KEYCODE_MEDIA_PLAY"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Playing Music Player command on Device with Device id: "+ device_id)
            os.system(adb_cmd_play_music_player)            
            LogFileWrite("End Action:: SUCCESS : Playing Music Player command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Playing Music Player command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def MusicPauseOnPlayer(self, device_id):
        adb_cmd_pause_music_player = "adb -s "+device_id+" shell input keyevent KEYCODE_MEDIA_PAUSE"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Pausing Music Player command on Device with Device id: "+ device_id)
            os.system(adb_cmd_pause_music_player)            
            LogFileWrite("End Action:: SUCCESS : Pausing Music Player command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Pausing Music Player command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def MusicStopOnPlayer(self, device_id):
        adb_cmd_stop_music_player = "adb -s "+device_id+" shell input keyevent KEYCODE_MEDIA_STOP"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Stopping Music Player command on Device with Device id: "+ device_id)
            os.system(adb_cmd_stop_music_player)            
            LogFileWrite("End Action:: SUCCESS : Stopping Music Player command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Stopping Music Player command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE
        
    def MusicNextSongOnPlayer(self, device_id):
        adb_cmd_next_song_music_player = "adb -s "+device_id+" shell input keyevent KEYCODE_MEDIA_NEXT"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Playing Next Song on Music Player command on Device with Device id: "+ device_id)
            os.system(adb_cmd_next_song_music_player)            
            LogFileWrite("End Action:: SUCCESS : Stopping Music Player command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Stopping Music Player command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def MusicOpenVLCPlayer(self, device_id):
        adb_cmd_open_music_player = "adb -s "+device_id+" shell monkey -p org.videolan.vlc -c android.intent.category.LAUNCHER 1"        
        try:
            LogFileWrite("Start Action:: SUCCESS : Opening Music Player command on Device with Device id: "+ device_id)
            os.system(adb_cmd_open_music_player)            
            LogFileWrite("End Action:: SUCCESS : Opening Music Player command on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Opening Music Player command on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    # browser and website related
    def OpenURL(self, device_id, url_full):
        adb_cmd_open_url = "adb -s "+device_id+" shell am start -a \"android.intent.action.VIEW\" -d "+url_full
        try:
            LogFileWrite("Start Action:: SUCCESS : opening "+url_full+" on Device with Device id: "+ device_id)
            os.system(adb_cmd_open_url)            
            LogFileWrite("End Action:: SUCCESS : opening "+url_full+" on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE
        except Exception as e:
            LogFileWrite("End Action:: FAILED : opening "+url_full+" on Device with Device id: "+ device_id+"\n")
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

    def fOpenSoundRecorder(self, device_id):
        adb_cmd_open_csip = "adb -s "+device_id+" shell monkey -p com.android.soundrecorder -c android.intent.category.LAUNCHER 1"
        try:
            LogFileWrite("Start Action:: SUCCESS : Opening Sound Recorder on Device with Device id: "+ device_id)
            os.system(adb_cmd_open_csip)
            LogFileWrite("End Action:: SUCCESS : Opening Sound Recorder on Device with Device id: "+ device_id+"\n")
            return pyAndroid_SUCCESS_CODE             
        except Exception as e:
            LogFileWrite("End Action:: FAILED : Opening Sound Recorder on Device with Device id: "+ device_id)
            LogFileWrite("Exception message: "+ str(e)+".\n")
            return pyAndroid_ERROR_CODE

