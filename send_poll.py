import asyncio
import os
from datetime import date, timedelta

from telegram import Bot

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])  # safer to keep chat ID out of code too


# Function to calculate the closest Saturday
def get_closest_saturday():
    today = date.today()
    days_until_saturday = (5 - today.weekday()) % 7  # Saturday is weekday 5
    return today + timedelta(days=days_until_saturday)

closest_saturday = get_closest_saturday()
poll_question = f"Кружок в субботу ({closest_saturday.isoformat()})"
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
