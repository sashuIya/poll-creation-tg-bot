import asyncio
import os
from datetime import date

from telegram import Bot

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])  # safer to keep chat ID out of code too


poll_question = f"Кружок в субботу ({date.today().isoformat()})"
poll_options = [
    "Приду онлайн",
    "Приду онлайн или оффлайн",
    "Приду оффлайн",
    "Не приду",
]

async def send_poll():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_poll(
        chat_id=CHAT_ID,
        question=poll_question,
        options=poll_options,
        is_anonymous=False  # Optional, keep responses public
    )


if __name__ == "__main__":
    asyncio.run(send_poll())
