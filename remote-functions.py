import getopt, sys
import urllib2
import json
import tty
import os
import time
import StringIO
from config import *
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
def fileEmpty(leadButtonFileName):
	return os.path.isfile(leadButtonFileName) and os.path.getsize(leadButtonFileName) > 0

def stop():
	contents = urllib2.urlopen("http://" + controller_ip + "/control.php?action=stop&tv=" + client_name).read()
	url="http://127.0.0.1:3005/jsonrpc?request={\"jsonrpc\":\"2.0\",\"method\":\"GUI.ShowNotification\",\"params\":{\"title\":\"STOP\",\"message\":\""+client_name+"\",\"displaytime\":10000},\"id\":1}"
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	f = urllib2.urlopen(url)

def channel_up():
	contents = urllib2.urlopen("http://" + controller_ip + "/control.php?action=up&tv=" + client_name).read()
	url="http://127.0.0.1:3005/jsonrpc?request={\"jsonrpc\":\"2.0\",\"method\":\"GUI.ShowNotification\",\"params\":{\"title\":\"CHANNEL%20UP\",\"message\":\""+client_name+"\",\"displaytime\":10000},\"id\":1}"
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	f = urllib2.urlopen(url)

def channel_down():
	contents = urllib2.urlopen("http://" + controller_ip + "/control.php?action=down&tv=" + client_name).read()
	url="http://127.0.0.1:3005/jsonrpc?request={\"jsonrpc\":\"2.0\",\"method\":\"GUI.ShowNotification\",\"params\":{\"title\":\"CHANNEL%20DOWN\",\"message\":\""+client_name+"\",\"displaytime\":10000},\"id\":1}"
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	f = urllib2.urlopen(url)

def channel(channelNumber):
	contents = urllib2.urlopen("http://" + controller_ip + "/control.php?action=channel&num=" + channelNumber + "&tv=" + client_name).read()
	url="http://127.0.0.1:3005/jsonrpc?request={\"jsonrpc\":\"2.0\",\"method\":\"GUI.ShowNotification\",\"params\":{\"title\":\"Channel\",\"message\":\""+channelNumber+"\",\"displaytime\":10000},\"id\":1}"
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	f = urllib2.urlopen(url)

def channel_enter(buttonNumber):
		isFileNumber=str(fileEmpty(leadButtonFileName))
		if (time.time() - os.path.getmtime(leadButtonFileName) > 10 or isFileNumber == "False"):
			leadButtonFile = open(leadButtonFileName,"w+")
			leadButtonFile.write(buttonNumber)
			leadButtonFile.close()
			print(buttonNumber)
			url="http://127.0.0.1:3005/jsonrpc?request={\"jsonrpc\":\"2.0\",\"method\":\"GUI.ShowNotification\",\"params\":{\"title\":\"Channel\",\"message\":\""+buttonNumber+"-\",\"displaytime\":10000},\"id\":1}"
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			f = urllib2.urlopen(url)
		elif (time.time() - os.path.getmtime(leadButtonFileName) <= 10):
			leadButtonFile = open(leadButtonFileName,"r")
			leadButtonNumber = leadButtonFile.read()
			chars = leadButtonNumber.decode('utf8')
			leadButtonCount = len(chars)
			print(leadButtonCount)
			leadButtonFile.close()	
			if (channelDigits > 2) and (leadButtonCount < channelDigits - 1):
				leadButtonFile = open(leadButtonFileName,"a")
				leadButtonFile.write(buttonNumber)
				leadButtonFile.close()
				url="http://127.0.0.1:3005/jsonrpc?request={\"jsonrpc\":\"2.0\",\"method\":\"GUI.ShowNotification\",\"params\":{\"title\":\"Channel\",\"message\":\""+leadButtonNumber+buttonNumber+"-\",\"displaytime\":10000},\"id\":1}"
				headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
				f = urllib2.urlopen(url)
			else:
				leadButtonFile = open(leadButtonFileName,"r")
				leadButton = leadButtonFile.read(leadButtonCount)
				leadButtonFile.close()
				channelNumber = str(leadButton) + str(buttonNumber)
				print(channelNumber)
				url="http://127.0.0.1:3005/jsonrpc?request={\"jsonrpc\":\"2.0\",\"method\":\"GUI.ShowNotification\",\"params\":{\"title\":\"Channel\",\"message\":\""+channelNumber+"\",\"displaytime\":10000},\"id\":1}"
				headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
				f = urllib2.urlopen(url)
				contents = urllib2.urlopen("http://" + controller_ip + "/control.php?action=channel&num=" + channelNumber + "&tv=" + client_name).read()
			leadButtonFile = open(leadButtonFileName,"w+")
                        leadButtonFile.write("")
                        leadButtonFile.close()
if (argumentList[0] == "stop"):
	stop()
elif (argumentList[0] == "channel_up"):
	channel_up()
elif (argumentList[0] == "channel_down"):
	channel_down()
elif (argumentList[0] == "channel"):
	channelNumber = argumentList[1]
	channel(channelNumber)
elif (argumentList[0] == "debug"):
	print(argumentList)
	print(argumentList[0])
	print(argumentList[1])
elif (argumentList[0] == "channel_enter"):
	channel_enter(argumentList[1])
