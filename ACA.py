import logging
import os
import datetime
import random

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Logging levels
logging.basicConfig(level=logging.INFO)

load_dotenv()

# read the environment variables
SLACK_BOT_TOKEN = os.environ["ACA_Project_Bot_User_OAuth_Token"]
SLACK_APP_TOKEN = os.environ["ACA_Project_Socket_Mode_Token"]

app = App(token=SLACK_BOT_TOKEN)



@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event, logger):
    request = payload['blocks'][0]['elements'][0]['elements'][1]['text']
    # logger.info(request)
    res = request.lstrip().split(' ', 1)
    logger.info(res)
    com = res[0].strip().lower()
    if len(res) > 1:
        params = res[1].lstrip()
    else:
        params = ""
    logger.info(com)
    logger.info('------')

    if com == "hi":
        hi_command(request, com, params, say, logger)
    elif com == "happy":
        I_am_happy_command(request, com, params, say, logger)
    elif com == "sad":
        I_am_sad_command(request, com, params, say, logger)
    elif com == "tired":
        I_am_tired_command(request, com, params, say, logger)
    elif com == "mad":
        I_am_mad_command(request, com, params, say, logger)
    elif com == "lost":
        I_am_lost_command(request, com, params, say, logger)
    else:
        say("(❀╹◡╹) It's okay if you don't want to talk about it! I'll always be here")


# Hi command
def hi_command(request, com, params, say, logger):
    say(
        '''
        How was your day? ᕕ( ᐛ )ᕗ
        
        @I am
            1) happy
            2) sad
            3) tired
            4) mad
            5) lost
            

        '''
    )

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

# Happy command
def I_am_happy_command(request, com, params, say, logger):
    say(" Tell me more! What happened °˖✧◝(⁰▿⁰)◜✧˖°  ")
  
# Sad command
def I_am_sad_command(request, com, params, say, logger):
    cheer_up_playlist = [
        "https://www.youtube.com/watch?v=pPH2zrX4-iQ",
        "https://www.youtube.com/watch?v=APFMvzH1WEE",
        "https://www.youtube.com/watch?v=cKMR913sanw",
        "https://www.youtube.com/watch?v=UuzrLAjtoEc",
        "https://www.youtube.com/watch?v=zwo5EFCFcxA"
    ]
    say("What happened(ง •̀_•́)ง  Maybe a good song might cheer you up ")
    say( "ᖰ(·•︠ ˍ•︡ )ᖳ   " + random.choice(cheer_up_playlist))
    

# Tired command
def I_am_tired_command(request, com, params, say, logger):
    # get current time
    current_time = datetime.datetime.now()

    say("໒( ̿ ᴥ ̿ )७ It's " + str(current_time.hour) + ":" + str(current_time.minute))

    if current_time.hour < 19 and current_time.hour > 10:
        say("You should take a quick nap")

    elif current_time.hour < 10 and current_time.hour > 6:
        say("Did you sleep enough? What about drinking coffee ⅽ[ː̠̈ː̠̈ː̠̈] ͌")

    else:
        say("( ꒪⌓꒪) What about going to bed?")

# Mad command
def I_am_mad_command(request, com, params, say, logger):
    say(" ٩(๑•̀o•́๑)و WHAT HAPPENED TELL ME  ")

# Lost command
def I_am_lost_command(request, com, params, say, logger):
    lost_quotes = [
        "“All our dreams can come true, if we have the courage to pursue them.“ —Walt Disney",
        "“The secret of getting ahead is getting started.“ — Mark Twain",
        "“I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life, and that is why I succeed.” —Michael Jordan",
        "“Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve.” —Mary Kay Ash",
        "“The best time to plant a tree was 20 years ago. The second best time is now.” ―Chinese Proverb",
        "“Only the paranoid survive.” —Andy Grove",
        "“It’s hard to beat a person who never gives up.” —Babe Ruth",
        "“I wake up every morning and think to myself, ‘How far can I push this company in the next 24 hours.’” —Leah Busque",
        "“If people are doubting how far you can go, go so far that you can’t hear them anymore.” —Michele Ruiz",
        "“We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes―understanding that failure is not the opposite of success, it’s part of success.” ―Arianna Huffington",
        "“Write it. Shoot it. Publish it. Crochet it. Sauté it. Whatever. MAKE.” —Joss Whedon",

    ]
    say(random.choice(lost_quotes))



if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
