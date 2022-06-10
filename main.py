from aiogram.utils import executor
from handlers import client, callback, extra, admin

from config import dp
import logging

client.register_handler_client(dp)
callback.register_handlers_callback(dp)
admin.register_handler_admin(dp)

extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
