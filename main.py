import requests
from aiogram import Bot
from time import sleep

import asyncio


API_TOKEN = ''
bot = Bot(token=API_TOKEN)

def status_parser(url:str):
    curr_id = None
    print("Начало")
    manga_name = url.split("/")[-1] if url.split("/")[-1] != "" else url.split("/")[-2] 
    while True:
        print("Сайт будет проверяться каждый час!")

        r = requests.get(f"https://api.remanga.org/api/titles/{manga_name}/")
        if r.status_code == 200:
            r =r.json()

        name = r["content"]["status"]["name"]
        id = r["content"]["status"]["id"]
        if not curr_id:
            curr_id = id
        elif curr_id != id:
            c = asyncio.get_event_loop()
            b = c.create_task(main(name,url))
            c.run_until_complete(b)
        sleep(60*60)


async def main(name,url):
    text = f'{url} перешел в {name}'
    await bot.send_message(chat_id="",text=text)


if __name__ == "__main__":
    url = input("Введи URL: ")
    status_parser(url)