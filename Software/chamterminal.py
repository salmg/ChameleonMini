#!/usr/bin/env python3
#
# Command line tool to control the Chameleon through command line
#
# Modified - new terminal style: Salvador Mendoza (salmg.net) 
#
# Authors: Simon K. (simon.kueppers@rub.de)


import argparse
import Chameleon
import sys
import datetime
from cmd import Cmd
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def verboseLog(text):
    formatString = "[{}] {}"
    timeString = datetime.datetime.utcnow()
    print(formatString.format(timeString, text), sys.stderr)

# Command funcs
def cmdInfo(chameleon, arg):
    return "{}".format(chameleon.cmdVersion()['response'])

def cmdSetting(chameleon, arg):
    result = chameleon.cmdSetting(arg)

    if (arg is None or arg == '?' or arg == ''):
        return "Current Setting: {}".format(result['response'])
    else:
        if (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Setting has been changed to {}".format(chameleon.cmdSetting()['response'])
        else:
            return "Change setting to {} failed: {}".format(arg, result['statusText'])
    return

def cmdUID(chameleon, arg):
    result = chameleon.cmdUID(arg)

    if (arg is None):
        return "{}".format(result['response'])
    else:
        if (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "UID has been changed to {}".format(chameleon.cmdUID()['response'])
        else:
            return "Setting UID to {} failed: {}".format(arg, result['statusText'])

def cmdGetUID(chameleon, arg):
    return "{}".format(chameleon.cmdGetUID()['response'])

def cmdIdentify(chameleon, arg):
    return "{}".format(chameleon.cmdIdentify()['response'])

def cmdDumpMFU(chameleon, arg):
    return "{}".format(chameleon.cmdDumpMFU()['response'])

def cmdConfig(chameleon, arg):
    result = chameleon.cmdConfig(arg)

    if (arg is None or arg == ''):
        return "Current configuration: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible configurations: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Configuration has been changed to {}".format(chameleon.cmdConfig()['response'])
        else:
            return "Changing configuration to {} failed: {}".format(arg, result['statusText'])

def cmdUpload(chameleon, arg):
    if (os.path.isfile(arg)):
        with open(arg, 'rb') as fileHandle:
            bytesSent = chameleon.cmdUploadDump(fileHandle)
            return "{} Bytes successfully read from {}".format(bytesSent, arg)
    else:
        print("File not exist")

def cmdDownload(chameleon, arg):
    with open(arg, 'wb') as fileHandle:
        bytesReceived = chameleon.cmdDownloadDump(fileHandle)
        return "{} Bytes successfully written to {}".format(bytesReceived, arg)

def cmdLog(chameleon, arg):
    with open(arg, 'wb') as fileHandle:
        bytesReceived = chameleon.cmdDownloadLog(fileHandle)
        return "{} Bytes successfully written to {}".format(bytesReceived, arg)

def cmdLogMode(chameleon, arg):
    result = chameleon.cmdLogMode(arg)

    if (arg is None or arg == ''):
        return "Current logmode is: {}".format(result['response'])
    else:
        if (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "logmode have been set to {}".format(arg)
        else:
            return "Setting logmode failed: {}".format(arg, result['statusText'])

def cmdLButton(chameleon, arg):
    result = chameleon.cmdLButton(arg)

    if (arg is None or arg == ''):
        return "Current left button action: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible left button actions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Left button action has been set to {}".format(chameleon.cmdLButton()['response'])
        else:
            return "Setting left button action to {} failed: {}".format(arg, result['statusText'])

def cmdLButtonLong(chameleon, arg):
    result = chameleon.cmdLButtonLong(arg)

    if (arg is None or arg == ''):
        return "Current long press left button action: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible long press left button actions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Long press left button action has been set to {}".format(chameleon.cmdLButtonLong()['response'])
        else:
            return "Setting long press left button action to {} failed: {}".format(arg, result['statusText'])

def cmdRButton(chameleon, arg):
    result = chameleon.cmdRButton(arg)

    if (arg is None or arg == ''):
        return "Current right button action: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible right button actions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Right button action has been set to {}".format(chameleon.cmdRButton()['response'])
        else:
            return "Setting right button action to {} failed: {}".format(arg, result['statusText'])

def cmdRButtonLong(chameleon, arg):
    result = chameleon.cmdRButtonLong(arg)

    if (arg is None or arg == ''):
        return "Current long press right button action: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible long press right button actions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Long press right button action has been set to {}".format(chameleon.cmdRButtonLong()['response'])
        else:
            return "Setting long press right button action to {} failed: {}".format(arg, result['statusText'])

def cmdGreenLED(chameleon, arg):
    result = chameleon.cmdGreenLED(arg)

    if (arg is None or arg == ''):
        return "Current green LED function: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible green LED functions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Green LED function has been set to {}".format(chameleon.cmdGreenLED()['response'])
        else:
            return "Setting green LED function to {} failed: {}".format(arg, result['statusText'])

def cmdField(chameleon, arg):
    result = chameleon.cmdField(arg)

    if (arg is None or arg == '' or arg == '?'):
        return "Current FIELD function: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible FIELD functions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "FIELD function has been set to {}".format(chameleon.cmdGreenLED()['response'])
        else:
            return "Setting FIELD function to {} failed: {}".format(arg, result['statusText'])

def cmdReadonly(chameleon, arg):
    result = chameleon.cmdReadOnly(arg)

    if (arg is None or arg == '' or arg == '?'):
        return "Current FIELD function: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible FIELD functions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "FIELD function has been set to {}".format(chameleon.cmdReadOnly()['response'])
        else:
            return "Setting FIELD function to {} failed: {}".format(arg, result['statusText'])


def cmdRedLED(chameleon, arg):
    result = chameleon.cmdRedLED(arg)

    if (arg is None or arg == ''):
        return "Current red LED function: {}".format(result['response'])
    else:
        if (arg == chameleon.SUGGEST_CHAR):
            return "Possible red LED functions: {}".format(", ".join(result['suggestions']))
        elif (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Red LED function has been set to {}".format(chameleon.cmdRedLED()['response'])
        else:
            return "Setting red LED function to {} failed: {}".format(arg, result['statusText'])

def cmdThreshold(chameleon, arg):
    result = chameleon.cmdThreshold(arg)

    if (arg is None or arg == ''):
        return "Current threshold is: {}".format(result['response'])
    else:
        if (result['statusCode'] in chameleon.STATUS_CODES_SUCCESS):
            return "Threshold have been set to {}".format(arg)
        else:
            return "Setting threshold failed: {}".format(arg, result['statusText'])

def cmdUpgrade(chameleon, arg):
    if(chameleon.cmdUpgrade() == 0):
        print ("Device changed into Upgrade Mode")
    exit(0)

class MyChamelon(Cmd):
    prompt = bcolors.BOLD + 'Chameleon> '+ bcolors.ENDC
    intro = bcolors.WARNING + "Warning! Type ? to list commands - before any command, establish the Chameleon port!" + bcolors.ENDC
    verboseFunc = None
    chameleon = Chameleon.Device(verboseFunc)
    port = ""

    def connect(self):
        if (self.port):
            self.chameleon.connect(self.port)
            return 1
        else:
            print(">Set Chamelon-mini device!")
            self.help_port()
            return 0

    def disconnect(self):
        if (self.port):
            self.chameleon.disconnect()

    def do_shell(self, line):
        print (">Running shell command: "+ line)
        output = os.popen(line).read()
        print output
        self.last_output = output

    def help_shell(self):
        print(">Run a shell command")

    def do_exit(self, inp):
        print("Bye baby!")
        return True

    def help_exit(self):
        print('>Exit the application. Shorthand: x q Ctrl-D.')

    def do_verbose(self, inp):
        if (self.verboseFunc == verboseLog):
            self.verboseFunc = None
            print(">Null output verbose")
        else:
            self.verboseFunc = verboseLog
            print(">Set output verbose")
        self.chameleon = Chameleon.Device(self.verboseFunc)

    def help_verbose(self):
        print('>Output verbose')

    def do_port(self, inp):
        if (inp):
            print(">Setting Chameleon-mini Device: "+inp)
            self.port = inp
        else:
            print(">Need a port, example: port /dev/tty.XXXX")

    def help_port(self):
        print('>Specify port, example: port /dev/tty.XXXX')

    def executeCmd(self,func1,cmd1):
        if (self.connect()):
            result = func1(self.chameleon,cmd1)
            print("{}".format(result))
            self.disconnect()

    def do_info(self,inp):
        self.executeCmd(cmdInfo,0)

    def help_info(self):
        print('>Retrieve the Chameleon version')

    def do_rled(self, inp):
        self.executeCmd(cmdRedLED,inp)

    def help_rled(self):
        print('>Retrieve or set the current red led function')

    def do_gled(self, inp):
        self.executeCmd(cmdGreenLED,inp)

    def help_gled(self):
        print('>Retrieve or set the current green led function')

    def do_setting(self, inp):
        self.executeCmd(cmdSetting,inp)

    def help_setting(self):
        print('>Retrieve or set the current setting')
        print(Chameleon.VALID_SETTINGS)

    def do_download(self, inp):
        self.executeCmd(cmdDownload,inp)

    def help_download(self):
        print('>Download a card dump, example: download file.dump')

    def do_upload(self, inp):
        self.executeCmd(cmdUpload,inp)

    def help_upload(self):
        print('>Upload a card dump, example: download file.dump')

    def do_log(self, inp):
        self.executeCmd(cmdLog,inp)

    def help_log(self):
        print('>Download the device log, example: log file.log')

    def do_uid(self, inp):
        self.executeCmd(cmdUID,'?')
 
    def help_uid(self):
        print('>Retrieve or set the current UID')

    def do_getuid(self, inp):
        self.executeCmd(cmdGetUID,'?')
 
    def help_getuid(self):
        print('>Retrieve UID of device in range')

    def do_identify(self, inp):
        self.executeCmd(cmdIdentify,'?')

    def help_identify(self):
        print('>Identify device in range')

    def do_config(self, inp):
        self.executeCmd(cmdConfig,inp)

    def help_config(self):
        print('>Retrieve or set the current configuration: NONE,MF_ULTRALIGHT,MF_CLASSIC_1K,MF_CLASSIC_1K_7B,MF_CLASSIC_4K,MF_CLASSIC_4K_7B,ISO14443A_SNIFF,ISO14443A_READER')

    def do_logmode(self, inp):
        self.executeCmd(cmdLogMode,'?')

    def help_logmode(self):
        print('>Retrieve or set the current log mode')

    def do_dumpmfu(self, inp):
        self.executeCmd(cmdDumpMFU,'?')

    def help_dumpmfu(self):
        print('>Dump information about card in range')

    def do_lbuttonlong(self, inp):
        self.executeCmd(cmdLButtonLong,inp)

    def help_lbuttonlong(self):
        print('>Retrieve or set the current left button long press action')

    def do_rbuttonlong(self, inp):
        self.executeCmd(cmdRButtonLong,inp)

    def help_rbuttonlong(self, inp):
        print('>Retrieve or set the current right button long press action')

    def do_rbutton(self, inp):
        self.executeCmd(cmdRButton,inp)

    def help_rbutton(self):
        print('>Retrieve or set the current right button action')

    def do_lbutton(self, inp):
        self.executeCmd(cmdLButton,inp)

    def help_lbutton(self):
        print('>Retrieve or set the current left button action')

    def do_threshold(self, inp):
        self.executeCmd(cmdThreshold,inp)

    def help_threshold(self):
        print('>Retrieve or set the threshold')

    def do_upgrade(self, inp):
        self.executeCmd(cmdThreshold,'?')

    def help_upgrade(self):
        print('>Set the micro Controller to upgrade mode')

    def do_field(self, inp):
        self.executeCmd(cmdField,inp)

    def help_field(self):
        print('>Enables/disables the reader field')

    def do_readonly(self, inp):
        self.executeCmd(cmdReadonly,inp)

    def help_readonly(self):
        print('>Returns the current state of the read-only mode')

    def default(self, inp):
        if (inp == 'x' or inp == 'q'):
            return self.do_exit(inp)

    do_EOF = do_exit
    help_EOF = help_exit

if __name__ == '__main__':
    MyChamelon().cmdloop()
