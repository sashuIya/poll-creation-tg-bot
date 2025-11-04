import argparse
import asyncio
import os
from datetime import date, timedelta

from telegram import Bot

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = int(os.environ["CHAT_ID"])  # safer to keep chat ID out of code too


def get_closest_weekday(target_weekday):
    today = date.today()
    days_until = (target_weekday - today.weekday()) % 7
    return today + timedelta(days=days_until)


def get_poll_data(poll_type):
    if poll_type == "choose_day":
        closest_saturday = get_closest_weekday(5)  # 5=Sat
        closest_sunday = get_closest_weekday(6)  # 6=Sun
        poll_question = f"Выбираем день встречи"
        poll_options = [
            f"Суббота ({closest_saturday.isoformat()})",
            f"Воскресенье ({closest_sunday.isoformat()})",
            "Не приду",
        ]
    elif poll_type == "choose_time":
        poll_question = "Выбираем время встречи"
        poll_options = [
            "После 12pm",
            "После 1pm",
            "После 2pm",
            "После 3pm",
            "После 4pm",
            "После 5pm",
            "После 6pm",
            "После 7pm",
            "Не приду",
        ]
    else:
        raise ValueError("Unknown poll type. Use 'choose_day' or 'choose_time'.")
    return poll_question, poll_options


async def send_poll(poll_type):
    poll_question, poll_options = get_poll_data(poll_type)
    bot = Bot(token=BOT_TOKEN)
    await bot.send_poll(
        chat_id=CHAT_ID,
        question=poll_question,
        options=poll_options,
        is_anonymous=False,
        allows_multiple_answers=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send a Telegram poll for choosing day or choosing time."
    )
    parser.add_argument(
        "--poll",
        choices=["choose_day", "choose_time"],
        required=True,
        help="Which poll to send",
    )
    args = parser.parse_args()
    asyncio.run(send_poll(args.poll))
