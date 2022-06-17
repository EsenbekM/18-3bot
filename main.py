from aiogram.utils import executor
from handlers import client, callback, extra, admin, fsm_anketa

from config import dp
import logging
from database.bot_db import sql_create


async def on_startup(_):
    sql_create()

client.register_handler_client(dp)
callback.register_handlers_callback(dp)
admin.register_handler_admin(dp)
fsm_anketa.register_handler_fsmanketa(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
