# InvestBot

**InvestBot** is a Telegram bot that provides public information about S&P 500 companies.  
It uses [investApp](https://github.com/Germael/investApp) as its backend to retrieve key financial data and present it in a user-friendly format directly via Telegram.

## Features

- 🔍 Search for S&P 500 companies by name or ticker
- 📊 Get key financial metrics and market data
- 💬 Fast and interactive Telegram interface

## Requirements

- Python 3.8+
- [Poetry](https://python-poetry.org/docs/#installation)
- Telegram bot token (create one via [BotFather](https://t.me/BotFather))

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/Germael/invest_bot.git
   cd invest_bot

2. **Install dependencies using Poetry**

   ```bash
   poetry install

3. **Set up environment variables**

   Create a .env file in the root directory and add your Telegram bot token:
   ```bash
   TELEGRAM_API_TOKEN=your-telegram-bot-token

4. **Run the bot**
   
   ```bash
   poetry run python main.py

## Usage

Once running, open Telegram, find your bot, and send a company name or ticker symbol (e.g., `AAPL` or `Apple`). The bot will respond with public data sourced from the S&P 500.

## Related Project

- [investApp](https://github.com/Germael/investApp) — Backend service used by the bot

## License

This project is licensed under the [MIT License](LICENSE).
