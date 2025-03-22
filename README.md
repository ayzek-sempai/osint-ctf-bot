# OSINT CTF Telegram Bot

## Overview
This is a Telegram bot designed for CTF (Capture The Flag) challenges related to OSINT (Open-Source Intelligence). It allows users to submit specific queries and receive predefined responses, such as flags, based on their inputs.

## Features
- **Automated CTF Challenges**: Responds to specific OSINT-related queries with CTF flags.
- **Custom Response Mapping**: Define specific responses for given inputs.
- **User-Friendly Commands**: Simple and structured commands for ease of use.
- **Security Measures**: Implements rate-limiting and command restrictions.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/ayzek-sempai/osint-ctf-bot.git
   cd osint-ctf-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   ```sh
   TELEGRAM_BOT_TOKEN=your_bot_token
   ```
4. Run the bot:
   ```sh
   python bot.py
   ```

## Usage
- Start the bot by sending `/start`.
- Use `/help` to see available commands.
- Send predefined queries to receive CTF flags.
- Example:
  - User: `What is the target's name?`
  - Bot: `Flag{target_name_found}`

## Example Specific Responses
The bot is configured to return specific responses based on input patterns. Example:

```python
RESPONSES = {
    "comany name": "Flag{company_name_discovered}",
    "IP address": "Flag{ip_address_traced}"
}
```

## License
This project is licensed under the MIT License.
