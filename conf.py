CONF_BOT_TWITCH = {
	"access_token" : "TODO", # Copy the ACCESS TOKEN from https://twitchtokengenerator.com/
	"refresh_token": "TODO", # Copy the REFRESH TOKEN from https://twitchtokengenerator.com/
	"client_id": "TODO", # Copy the CLIENT ID from https://twitchtokengenerator.com/
	"nick": "Doigt", # Name of the bot (variable not used in the scripts)
	"prefix": "!", # Prefix used for tchat command. Usually "!", but can be anything else
	"initial_channels" : "TODO"	# Name of the channel in which the bot will respond (your channel name)
}

old_time = None
DELAI = 30				# Seconds number delay between 2 commands Nombre de secondes de délai entre chaque commande
remaining_time = True 	# The remaining_time variable will activate (True) or deactivate (False) 
						# the response from the Bot for the remaining time between 2 commands