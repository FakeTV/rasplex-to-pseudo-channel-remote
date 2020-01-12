## Rasplex to Pseudo Channel Remote
This is a script intended to allow simple control over Pseudo Channel using a remote connected to a RasPlex or OpenPHT device.

### Installation
 - Connect to your device and copy `config.py`, `remote-functions.py` and `leadbutton.txt` to a directory on your RasPlex device
 - Copy the contents of keymaps-template.xml to your custom keymaps xml in `/storage/.plexht/userdata/keymaps`
	 - If you don't have a custom keymaps xml, more information on creating one can be found [here:](https://kodi.wiki/view/HOW-TO:Modify_keymaps)
	 - You may need to change the file path in the command, when copying
 - Edit `config.py` with the name of your Client device, IP address of your Pseudo Channel device, file path to `leadbutton,txt` (this should be the same directory as `remote-functions.py`
	 - Also, if you are using 3-digit channel numbers instead of 2-digit, change the value of `channelDigits` to `3`
 - Restart RasPlex

### Usage
 - Once it's set up, and restarted, you'll be able to start channels by number, execute channel up and channel down commands, and stop the script. Make sure the buttons in the keymaps template correspond with the buttons on your remote (also keep in mind, many remotes are recognized as keyboards by the Raspberry Pi).

### Join us on Discord
For questions, comments or otherwise on this script or other scripts under FakeTV, join us on discord here: https://discord.gg/pCg38MN
