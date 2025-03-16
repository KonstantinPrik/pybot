import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.methods import DeleteWebhook
from aiogram.types import Message
import requests


TOKEN = '7519820801:AAHaECACfXLq6fkhGh-vaCUjIBxQy_ALJKs' # ⁡⁢⁡⁢⁣⁣ПОМЕНЯЙТЕ ТОКЕН НА ВАШ⁡


logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher()


# ⁡⁢⁣⁣КОМАНДА СТАРТ⁡
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я бот с подключенной нейросетью, отправь свой запрос', parse_mode = 'HTML')


# ⁡⁢⁣⁣ОБРАБОТЧИК ЛЮБОГО СООБЩЕНИЯ⁡
@dp.message()
async def filter_messages(message: Message):
    url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6ImFmYWZlNzQ0LWIxNDgtNDQ5Ni05M2YzLWMxNWIxNmVjZDUzNCIsImV4cCI6NDg5NTc0NzQ4NX0.PtqrmuMMaOK4apG3LtbPee0h9-6YBbZ2G-OZxTtDmTK1vnYQfaTAw9UsVr9anWQimhZ99MHCmAWiWM7p56ZUsw",
    }

    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": message.text
            }
        ],
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    # pprint(data) 

    text = data['choices'][0]['message']['content']
    bot_text = text.split('</think>\n\n')[1]

    await message.answer(bot_text, parse_mode = "Markdown")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
