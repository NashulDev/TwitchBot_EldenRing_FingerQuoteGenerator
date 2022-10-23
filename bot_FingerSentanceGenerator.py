from gtts import gTTS
from io import BytesIO
from pygame import mixer
import time
import os
import io
from twitchio.ext import commands
from random import seed
from random import randint
import conf

file_path = os.getcwd()
seed()

bot = commands.Bot(
	# set up the bot : https://twitchtokengenerator.com
	token="oauth:" + conf.CONF_BOT_TWITCH["access_token"],
	client_secret=conf.CONF_BOT_TWITCH["refresh_token"],
	client_id=conf.CONF_BOT_TWITCH["client_id"],
	nick=conf.CONF_BOT_TWITCH["nick"],
	prefix=conf.CONF_BOT_TWITCH["prefix"],
	initial_channels=[conf.CONF_BOT_TWITCH["initial_channels"]]
)


def randnum(fname):
	lines=open(fname, 'r').read().splitlines()
	print(lines)
	return random.choice(lines)


def generate_random_quote():
	conjonction_bool = randint(0, 2)
	word = ""
	conj = ""
	chosen_conj=""
	chosen_quote=""
	tab_line_quotes = []
	tab_line_words = []
	tab_line_conj = []
	list_quotes = "lists/doigts.txt"
	list_words = "lists/mots.txt"
	list_conjonctions = "lists/conjonctions.txt"

	with io.open(list_quotes,  mode='r', encoding='utf-8') as f_quotes:
			lines_quotes = f_quotes.readlines()
			for line_quote in lines_quotes:
				tab_line_quotes.append(line_quote.strip())

	with io.open(list_words, mode='r', encoding='utf-8') as f_words:
		
		lines_words = f_words.readlines()
		for line_word in lines_words:
			tab_line_words.append(line_word.strip())

	with io.open(list_conjonctions,  mode='r', encoding='utf-8') as f_conjonctions:
		
		lines_conj = f_conjonctions.readlines()
		for line_conj in lines_conj:
			tab_line_conj.append(line_conj.strip())

	# conjonction_bool = 1
	while(conjonction_bool >= 0):

		conjonction_bool = conjonction_bool - 1
		if chosen_conj != "":
			chosen_quote = chosen_quote + " " + chosen_conj + " "
		chosen_quote = chosen_quote + tab_line_quotes[randint(0, len(tab_line_quotes) - 1)]
		while "XXX" in chosen_quote.upper():
			chosen_word = ""
			while chosen_word == "" or '#' in chosen_word or chosen_word == "\n":
				chosen_word = tab_line_words[randint(0, len(tab_line_words) - 1)]
			chosen_quote = chosen_quote.replace("XXX", chosen_word, 2).capitalize()

		index=randint(0, len(tab_line_conj) - 1)
		chosen_conj = tab_line_conj[index]

	print("chosen_quote = " + chosen_quote)
	return chosen_quote


def speak(text="Texte par défaut"):
	mp3_fp = BytesIO()
	tts = gTTS(text, lang='fr', slow=True)
	tts.write_to_fp(mp3_fp)
	return mp3_fp


@bot.event
async def event_ready():
	'Called once when the bot goes online.'
	print(f"{bot['nick']} is online!")
	ws = bot._ws  # this is only needed to send messages within event_ready
	await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
	'Runs every time a message is sent in chat.'
	# make sure the bot ignores itself and the streamer
	if ctx.author.name.lower() == bot['nick'].lower():
		return


@bot.command(name='doigt')
async def test(ctx):
	mixer.init()
	text=generate_random_quote()
	sound = speak(text)
	sound.seek(0)
	mixer.music.load(sound, "mp3")
	mixer.music.play()
	await ctx.send(text)

if __name__ == "__main__":
	bot.run()

