import pyrogram , pyromod

from pyromod import listen
from keep import alive
from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='plugins')
tok = '6299081551:AAGvumouIsJdFG3j7zLRLW6C4xSopzIkkFc' ## توكنك 
id = 1308075085 ## ايديك
db = dt("data.sqlite", 'fuck')
if not db.get("checker"):
  db.set('checker', None)
if not db.get("admin_list"):
  db.set('admin_list', [id])
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('sessions'):
  db.set('sessions', [])
if not db.get('force'):
  db.set('force', ['trprogram'])
x = Client(name='loclhosst', api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)
alive()
x.run()
