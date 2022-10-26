# TwitchBot_EldenRing_FingerQuoteGenerator

A bot (usable on Twitch) which will generate a random sentance (from the "Messages" functionality of the "Elden Ring" game), and prononce it with Text to Speech. 

## Installation (Windows)

1. Install Python3.10 from https://www.python.org/downloads/release/python-3108/ (Windows Installer). Put the option "Add Python.exe to PATH" option, and click on "Install Now".
2. Download the project, or clone it with 
```
git clone https://github.com/NashulDev/EldenRing_FingerSentanceGenerator.git
```
3. Go into the folder and open Powershell in it (type "cd <FOLDER_PATH>", or from the Windows Explorer click on "File", and "Open a Powershell console")
4. Install dependencies with
```
python.exe -m pip install -r requirements.txt
```
5. Generate tokens for your bot with https://twitchtokengenerator.com > "Bot Chat Token" > Connect with your account or your Twitch Bot account
6. Copy "ACCESS TOKEN", "REFRESH TOKEN" and "CLIENT ID" and complete the "conf.py" file with it, as well as other fields. **Exemple** :
```
CONF_BOT_TWITCH = {
	"access_token" : "dqdjj8g411htd3", # Copy the ACCESS TOKEN from https://twitchtokengenerator.com/
	"refresh_token": "b7dnazdiondaoi987dazdzahduiazhdaumv", # Copy the REFRESH TOKEN from https://twitchtokengenerator.com/
	"client_id": "dus787h98hjg7jbcvxbvcxv897", # Copy the CLIENT ID from https://twitchtokengenerator.com/
	"nick": "MegaBot", # Name of the bot (variable not used in the scripts)
	"prefix": "!", # Prefix used for tchat command. Usually "!", but can be anything else
	"initial_channels" : "Nashul" # Name of the channel in which the bot will respond (your channel name)
}
``` 

## Usage (Windows)

Just start the bot from Powershell.
```
python.exe .\bot_FingerSentanceGenerator.py
```
