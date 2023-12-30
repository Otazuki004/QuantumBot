import asyncio
from root import bot
from root import prefix
from root.database.coins import add_coins_to_db, get_coins_from_users
from root.database.main import get_users_list
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from root.plugins.main import ask_to_dm_first


dice_users = []
@bot.on_message(filters.command("dice", prefix))
async def dice(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id in (await get_users_list()):
         return await ask_to_dm_first(message=message)
    if user_id in dice_users:
        return await message.reply_text("Try Later You Already Played! Next One Would Be Takes 10Minutes")
    dice_users.append(user_id)    
    xx = await bot.send_dice(chat_id=chat_id)
    value = int(xx.dice.value)
    if value == 1:
         coins = 10000
    else:
         await asyncio.sleep(4)
         await message.reply_text(f"🥸 [Better Luck Next Time.]({xx.link})", quote=True)
         await asyncio.sleep(10*60)
         dice_users.remove(user_id)
         return 
    await add_coins_to_db(
        user_id=user_id,
        coins=coins)
    kk = await get_coins_from_users(
            user_id=user_id)
    await asyncio.sleep(4)
    await message.reply_text(
        f"You won: **{coins}**\nTotal coins: **{kk}**")
    await asyncio.sleep(10*60)
    dice_users.remove(user_id)
    return 


dart_users = []
@bot.on_message(filters.command("dart", prefix))
async def dart(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id in (await get_users_list()):
         return await ask_to_dm_first(message=message)
    if user_id in dart_users:
        return await message.reply_text("Try Later You Already Played! Next One Would Be Takes 10Minutes")
    dart_users.append(user_id)    
    xx = await bot.send_dice(chat_id=chat_id, emoji="🎯")
    value = int(xx.dice.value)
    if value == 6:
         coins = 10000
    else:
         await asyncio.sleep(4)
         await message.reply_text(f"🥸 [Better Luck Next Time.]({xx.link})", quote=True)
         await asyncio.sleep(10*60)
         dart_users.remove(user_id)
         return 
    await add_coins_to_db(
        user_id=user_id,
        coins=coins)
    kk = await get_coins_from_users(
            user_id=user_id)
    await asyncio.sleep(4)
    await message.reply_text(
        f"You won ✅: **{coins}**\nTotal coins 💰: **{kk}**")
    await asyncio.sleep(10*60)
    dart_users.remove(user_id)
    return 


football_users = []
@bot.on_message(filters.command("football", prefix))
async def football(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id in (await get_users_list()):
         return await ask_to_dm_first(message=message)
    if user_id in football_users:
        return await message.reply_text("Try Later You Already Played! Next One Would Be Takes 10Minutes")
    football_users.append(user_id)    
    xx = await bot.send_dice(chat_id=chat_id, emoji="⚽")
    value = int(xx.dice.value)
    if value != 1 and value != 2:
         coins = 10000
    else:
         await asyncio.sleep(4)
         await message.reply_text(f"🥸 [Better Luck Next Time.]({xx.link})", quote=True)
         await asyncio.sleep(10*60)
         football_users.remove(user_id)
         return 
    await add_coins_to_db(
        user_id=user_id,
        coins=coins)
    kk = await get_coins_from_users(
            user_id=user_id)
    await asyncio.sleep(4)
    await message.reply_text(
        f"You won ✅: **{coins}**\nTotal coins 💰: **{kk}**")
    await asyncio.sleep(10*60)
    football_users.remove(user_id)
    return 

basketball_users = []
@bot.on_message(filters.command("basketball", prefix))
async def basketball(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id in (await get_users_list()):
         return await ask_to_dm_first(message=message)
    if user_id in basketball_users:
        return await message.reply_text("Try Later You Already Played! Next One Would Be Takes 10Minutes")
    basketball_users.append(user_id)    
    xx = await bot.send_dice(chat_id=chat_id, emoji="🏀")
    value = int(xx.dice.value)
    if value not in [1,2,3]:
         coins = 10000
    else:
         await asyncio.sleep(4)
         await message.reply_text(f"🥸 [Better Luck Next Time.]({xx.link})", quote=True)
         await asyncio.sleep(10*60)
         basketball_users.remove(user_id)
         return 
    await add_coins_to_db(
        user_id=user_id,
        coins=coins)
    kk = await get_coins_from_users(
            user_id=user_id)
    await asyncio.sleep(4)
    await message.reply_text(
        f"You won ✅: **{coins}**\nTotal coins 💰: **{kk}**")
    await asyncio.sleep(10*60)
    basketball_users.remove(user_id)
    return 


bowling_users = []
@bot.on_message(filters.command("bowl", prefix))
async def bowling(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id in (await get_users_list()):
         return await ask_to_dm_first(message=message)
    if user_id in bowling_users:
        return await message.reply_text("Try Later You Already Played! Next One Would Be Takes 10Minutes")
    bowling_users.append(user_id)    
    xx = await bot.send_dice(chat_id=chat_id, emoji="🎳")
    value = int(xx.dice.value)
    if value == 6:
         coins = 10000
    else:
         await asyncio.sleep(4)
         await message.reply_text(f"🥸 [Better Luck Next Time.]({xx.link})", quote=True)
         await asyncio.sleep(10*60)
         bowling_users.remove(user_id)
         return 
    await add_coins_to_db(
        user_id=user_id,
        coins=coins)
    kk = await get_coins_from_users(
            user_id=user_id)
    await asyncio.sleep(4)
    await message.reply_text(
        f"You won ✅: **{coins}**\nTotal coins 💰: **{kk}**")
    await asyncio.sleep(10*60)
    bowling_users.remove(user_id)
    return 
