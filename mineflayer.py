from javascript import require, once, console

mf = require('mineflayer')

BOT_USERNAME = f'HubTVMC'
bot = mf.createBot({ 'host': '127.0.0.1', 'port': 25565, 'username': BOT_USERNAME, 'hideErrors': False })

def respawn(*args, **kwargs):
    bot.respawn()

once(bot, 'login')
bot.chat('Hello World')
bot.on('kicked', console.log)
bot.on('error', console.log)
bot.on('death', respawn)

def handle_key(event):
    pass

## TODO - CHAT INSTRUCTIONS

bot.dig()
bot.stopDigging()
bot.openContainer()

headpos = mf.Vec3(0, 60, 0)
block = bot.lookAt(headpos)

