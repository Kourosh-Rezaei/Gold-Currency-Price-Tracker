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


SELECT_CATEGORY, SELECT_METAL, SELECT_CURRENCY, SELECT_UNIT = range(4)

CATEGORIES = {
    "precious metals": "precious",
    "precious": "precious",
    "industrial metals": "industrial",
    "industrial": "industrial",
}

PRECIOUS_METALS = {
    "gold": "gold",
    "silver": "silver",
    "platinum": "platinum",
    "palladium": "palladium",
}

INDUSTRIAL_METALS = {
    "copper": "copper",
    "aluminum": "aluminum",
    "aluminium": "aluminum",
    "nickel": "nickel",
    "lead": "lead",
    "zinc": "zinc",
}

CURRENCIES = {
    "usd": "USD",
    "eur": "EUR",
    "gbp": "GBP",
}

PRECIOUS_UNITS = {
    "toz": "toz",
    "g": "g",
    "gram": "g",
    "kg": "kg",
}

INDUSTRIAL_UNITS = {
    "mt": "mt",
    "metric ton": "mt",
    "ton": "mt",
    "kg": "kg",
    "g": "g",
    "gram": "g",
}


def normalize_input(text: str) -> str:
    """Normalize user input by removing extra spaces and converting it to lowercase."""
    return text.strip().lower()
    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the conversation and display the metal category keyboard."""

    context.user_data.clear()

    keyboard = [
        ["Precious Metals"],
        ["Industrial Metals"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await update.message.reply_text(
        "Welcome!\nSelect a metal category:",
        reply_markup=reply_markup,
    )

    return SELECT_CATEGORY



async def select_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Validate the selected category and display available metals."""

    category = normalize_input(update.message.text)

    if category not in CATEGORIES:
        await update.message.reply_text(
            "Invalid category❌ Please select a valid category."
        )
        return SELECT_CATEGORY

    selected_category = CATEGORIES[category]

    context.user_data["category"] = selected_category

    if selected_category == "precious":
        keyboard = [
            ["Gold", "Silver"],
            ["Platinum", "Palladium"],
        ]

    else:
        keyboard = [
            ["Copper", "Aluminum"],
            ["Nickel", "Lead"],
            ["Zinc"],
        ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )

    await update.message.reply_text(
        "Category selected successfully ✅\n\n"
        "Select a metal or type its name:",
        reply_markup=reply_markup,
    )

    return SELECT_METAL



async def select_metal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Validate the selected metal and ask the user to choose a currency."""

    metal = normalize_input(update.message.text)

    category = context.user_data["category"]

    if category == "precious":
        available_metals = PRECIOUS_METALS
    else:
        available_metals = INDUSTRIAL_METALS

    if metal not in available_metals:
        await update.message.reply_text(
            "Invalid metal❌ Please select or enter a valid metal name."
        )
        return SELECT_METAL

    context.user_data["metal"] = available_metals[metal]

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
    """Validate the selected currency and ask the user to choose a unit."""

    currency = normalize_input(update.message.text)

    if currency not in CURRENCIES:
        await update.message.reply_text(
            "Invalid currency❌ Please select or enter a valid currency."
        )
        return SELECT_CURRENCY

    context.user_data["currency"] = CURRENCIES[currency]

    if context.user_data["category"] == "precious":
        keyboard = [["toz", "g", "kg"]]
    else:
        keyboard = [["mt", "kg", "g"]]

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
    """Validate the selected unit and display the user's final selections."""

    unit = normalize_input(update.message.text)

    if context.user_data["category"] == "precious":
        available_units = PRECIOUS_UNITS
    else:
        available_units = INDUSTRIAL_UNITS

    if unit not in available_units:
        await update.message.reply_text(
            "Invalid unit❌ Please select or enter a valid unit."
        )
        return SELECT_UNIT

    context.user_data["unit"] = available_units[unit]

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
    """Cancel the conversation and clear the user's stored selections."""
    context.user_data.clear()

    await update.message.reply_text(
        "Operation cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END


def main():
    """Configure and run the Telegram bot application."""
    if not token:
        raise RuntimeError("[ERROR] The Telegram bot token is not defined!")

    application = (
    Application.builder()
    .token(token)
    .connect_timeout(30)
    .read_timeout(30)
    .write_timeout(30)
    .pool_timeout(30)
    .get_updates_connect_timeout(30)
    .get_updates_read_timeout(40)
    .get_updates_write_timeout(30)
    .get_updates_pool_timeout(30)
    .build()
    )
 
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECT_CATEGORY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    select_category,)
                    ],
            SELECT_METAL: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    select_metal,)
                    ],
            SELECT_CURRENCY: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    select_currency,)
                    ],
            SELECT_UNIT: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    select_unit,)
                    ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
        )

    application.add_handler(conversation_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
