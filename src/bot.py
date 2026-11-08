import os

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

load_dotenv()

token = os.getenv("BOT_KEY")


SELECT_METAL, SELECT_CURRENCY, SELECT_UNIT = range(3)


METALS = {
    "gold": "gold",
    "silver": "silver",
    "platinum": "platinum",
    "palladium": "palladium",
}

CURRENCIES = {
    "usd": "USD",
    "eur": "EUR",
    "gbp": "GBP",
}

UNITS = {
    "toz": "toz",
    "g": "g",
    "gram": "g",
    "kg": "kg",
}


def normalize_input(text: str) -> str:
    return text.strip().lower()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.clear()

    keyboard = [
        ["Gold", "Silver"],
        ["Platinum", "Palladium"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await update.message.reply_text(
        "Welcome!\nSelect a metal or type its name :",
        reply_markup=reply_markup,
    )

    return SELECT_METAL


async def select_metal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    metal = normalize_input(update.message.text)

    if metal not in METALS:
        await update.message.reply_text(
            "Invalid metal❌ Please select or enter a valid metal name."
        )
        return SELECT_METAL

    context.user_data["metal"] = METALS[metal]

    keyboard = [
        ["USD", "EUR", "GBP"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await update.message.reply_text(
        "Metal selected successfully ✅\n\n"
        "Select a currency or type its code:",
        reply_markup=reply_markup,
    )

    return SELECT_CURRENCY


async def select_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):

    currency = normalize_input(update.message.text)

    if currency not in CURRENCIES:
        await update.message.reply_text(
            "Invalid currency❌ Please select or enter a valid currency."
        )
        return SELECT_CURRENCY

    context.user_data["currency"] = CURRENCIES[currency]

    keyboard = [
        ["toz", "g", "kg"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await update.message.reply_text(
        "Currency selected successfully ✅\n\n"
        "Select a unit or type its name:",
        reply_markup=reply_markup,
    )

    return SELECT_UNIT


async def select_unit(update: Update, context: ContextTypes.DEFAULT_TYPE):

    unit = normalize_input(update.message.text)

    if unit not in UNITS:
        await update.message.reply_text(
            "Invalid unit❌ Please select or enter a valid unit."
        )
        return SELECT_UNIT

    context.user_data["unit"] = UNITS[unit]

    metal = context.user_data["metal"]
    currency = context.user_data["currency"]
    unit = context.user_data["unit"]

    await update.message.reply_text(
    f"📋 Your selections:\n"
    f"🔩 Metal: {metal}\n"
    f"💱 Currency: {currency}\n"
    f"📏 Unit: {unit}\n\n"
    "All selections completed! ✅",
    reply_markup=ReplyKeyboardRemove(),
)
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.clear()

    await update.message.reply_text(
        "Operation cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END


def main():

    if not token:
        raise RuntimeError("[ERROR] The Telegram bot token is not defined!")

    application = (
        Application.builder()
        .token(token)
        .build()
    )

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT_METAL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, select_metal)
            ],
            SELECT_CURRENCY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, select_currency)
            ],
            SELECT_UNIT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, select_unit)
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
    )

    application.add_handler(conversation_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
