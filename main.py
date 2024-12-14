from os import getenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
import requests

# Define states for the conversation
ASK_TICKER_INFO = 1
ASK_TICKER_ANALYTICS = 2

TOKEN = getenv('TELEGRAM_BOT_TOKEN')
INVEST_API_URL = getenv('INVEST_API_URL', 'http://192.168.0.72:49161')

# Command to start the ticker info process
async def get_ticker_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Please provide the ticker name for overview info:")
    return ASK_TICKER_INFO

# Handle the ticker name input and fetch info data
async def fetch_ticker_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ticker_name = update.message.text
    url = f"{INVEST_API_URL}/info/overview/{ticker_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        await update.message.reply_text(f"Overview Info:\n{data}")
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f"Failed to fetch ticker info: {e}")
    except ValueError:
        await update.message.reply_text("The server returned an invalid response.")
    return ConversationHandler.END

# Command to start the ticker analytics process
async def get_ticker_analytics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Please provide the ticker name for analytics:")
    return ASK_TICKER_ANALYTICS

# Handle the ticker name input and fetch analytics data
async def fetch_ticker_analytics(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    ticker_name = update.message.text
    url = f"{INVEST_API_URL}/info/analytics/{ticker_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        await update.message.reply_text(f"{data}")
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f"Failed to fetch ticker analytics: {e}")
    except ValueError:
        await update.message.reply_text("The server returned an invalid response.")
    return ConversationHandler.END

# Allow users to cancel the conversation
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END

def main():
    application = Application.builder().token(TOKEN).build()

    # Conversation handler for the /get_ticker_info command
    info_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("get_ticker_info", get_ticker_info)],
        states={
            ASK_TICKER_INFO: [MessageHandler(filters.TEXT & ~filters.COMMAND, fetch_ticker_info)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Conversation handler for the /get_ticker_analytics command
    analytics_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("get_ticker_analytics", get_ticker_analytics)],
        states={
            ASK_TICKER_ANALYTICS: [MessageHandler(filters.TEXT & ~filters.COMMAND, fetch_ticker_analytics)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Add both handlers to the application
    application.add_handler(info_conv_handler)
    application.add_handler(analytics_conv_handler)

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
