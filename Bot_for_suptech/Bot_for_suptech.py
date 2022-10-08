#код для телеграм бота, который бы дублировал любое сообщение, которое ему отправлено.
from aiogram import Bot, Dispatcher, executor, types

#bot init
bot = Bot(token="5502399074:AAFSgJVoaKHL6X_zUVWMdHQS--ILsgVS7Vo")
dp = Dispatcher(bot)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# run long-polling
if __name__== "__main__"