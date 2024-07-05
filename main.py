# Don't Remove Credit Tg - @Irrlrrr
# Subscribe Telegram Channel For Amazing Bot https://t.me/routineweek
# Ask Doubt on telegram @Innlnnn


from pyrogram import Client
from pyromod import listen
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            "Leader login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Leader"),
            workers=50,
            sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        print('Bot Started Powered By @Irrlrrr')

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

# Don't Remove Credit Tg - @Irrlrrr
# Subscribe Telegram Channel For Amazing Bot https://t.me/routineweek
# Ask Doubt on telegram @Innlnnn
