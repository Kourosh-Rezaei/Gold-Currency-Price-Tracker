import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("BOT_KEY")


def main():

    if not token:
        raise RuntimeError("[ERROR] The Telegram bot token is not defined!")
    



if __name__ == "__main__":
    main()
