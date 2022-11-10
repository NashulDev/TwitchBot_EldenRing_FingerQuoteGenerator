# FR - TwitchBot_EldenRing_FingerQuoteGenerator

Un bot (répondant à des commandes d'un Tchat Twitch) qui va générer des citations aléatoires (issues de la fonctionnalité d'écriture de message d'Elden Ring) et les prononcer à voix haute.

Si vous souhaitez me remercier, hésitez pas à venir me faire un coucou en stream : https://twitch.tv/nashul :)

## Installation (Windows)

1. Installez Python3.10 depuis https://www.python.org/downloads/release/python-3108/ (Windows Installer). Choisissez l'option "Add Python.exe to PATH" puis cliquez sur "Install Now".
2. Téléchargez le projet (Code > Download zip) ou clonez le via la commande :  
```
git clone https://github.com/NashulDev/EldenRing_FingerSentanceGenerator.git
```
3. Allez dans le dossier et ouvez l'utilitaire Powershell (tapez la commande "cd <FOLDER_PATH>" avec le bon dossier, ou cliquez dans l'explorateur de fichier Windows sur "Fichier" > "Ouvrir Windows Powershell"
4. Installez les dépendances via la commande :
```
python.exe -m pip install -r requirements.txt
```
5. Générez les jetons pour votre bot avec https://twitchtokengenerator.com > "Bot Chat Token" > Connect with your account or your Twitch Bot account
6. Copiez  "ACCESS TOKEN", "REFRESH TOKEN" and "CLIENT ID" et complétez le fichier "conf/conf.py" avec ces données. Complétez également les autres variables du fichier. 
**Exemple** :
```
CONF_BOT_TWITCH = {
	"access_token" : "dqdjj8g411htd3", # Copy the ACCESS TOKEN from https://twitchtokengenerator.com/
	"refresh_token": "b7dnazdiondaoi987dazdzahduiazhdaumv", # Copy the REFRESH TOKEN from https://twitchtokengenerator.com/
	"client_id": "dus787h98hjg7jbcvxbvcxv897", # Copy the CLIENT ID from https://twitchtokengenerator.com/
	"nick": "MegaBot", # Name of the bot 
	"prefix": "!", # Prefix used for tchat command. Usually "!", but can be anything else
	"initial_channels" : "Nashul" # Name of the channel in which the bot will respond (your channel name)
}
``` 

## Configuration optionelle

D'autres variables peuvent être modifiés dans le fichier "conf/conf.py".
```
commandDoigt = 'doigt' # Name of the command in the Twitch Tchat, used with the prefix
delay_between_commands = 30	# Seconds number delay between 2 commands Nombre de secondes de délai entre chaque commande
remaining_time = True 	# The remaining_time variable will activate (True) or deactivate (False) the response from the Bot for the delay_between_commands between 2 commands
```

## Utilisation (Windows)

Exécutez la commande suivante depuis Powershell. 
```
python.exe .\bot_FingerSentanceGenerator.py
```
Vous pouvez tester en écrivant "!doigt" dans votre tchat.

# EN - TwitchBot_EldenRing_FingerQuoteGenerator

A bot (which will respond to Twitch Tchat commands) which will generate a random sentance (from the "Messages" functionality of the "Elden Ring" game), and prononce it with Text to Speech.

Note : English language is not available right now, but will be added if anyone is interested.

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

## Optionnal configuration

D'autres variables peuvent être modifiés dans le fichier "conf/conf.py".
```
commandDoigt = 'doigt' # Name of the command in the Twitch Tchat, used with the prefix
delay_between_commands = 30	# Seconds number delay between 2 commands Nombre de secondes de délai entre chaque commande
remaining_time = True 	# The remaining_time variable will activate (True) or deactivate (False) the response from the Bot for the delay_between_commands between 2 commands
```

## Usage (Windows)

Just start the bot from Powershell.
```
python.exe .\bot_FingerSentanceGenerator.py
```
