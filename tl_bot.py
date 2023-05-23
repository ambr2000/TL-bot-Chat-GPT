import aiogram
from aiogram import Bot, Dispatcher, types
import openai

openai.api_key = 'open ai код'
bot_token = 'код бота'
bot_display_name = 'Иван Нифонтов'
bot = Bot(token=bot_token)
dispatcher = Dispatcher(bot)

@dispatcher.message_handler()
async def handle_message(message: types.Message):
    prompt = message.text
    response = chat_with_gpt(prompt)
    await message.answer(response)

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    aiogram.executor.start_polling(dispatcher)
