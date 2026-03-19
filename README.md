![Discord Bot Banner](public/discord-bot-1240w.jpeg)

# Simple bot - Discord

A simple yet feature-rich Discord bot with utility commands. Perfect for learning Python backend development and Discord.py integration!

## Features

- **`/ping`** — Check if the bot is online and measure response latency
- **`/roll`** — Roll a dice with customizable sides (default: d6, or specify: `/roll 20` for d20)
- **`/flip`** — Flip a coin to get Heads or Tails
- **`/choose`** — Pick one random option from a list (example: `/choose pizza, tacos, sushi`)
- **`/poll`** — Create interactive polls with emoji reactions (example: `/poll "Favorite pizza?" pepperoni, margherita, hawaiian`)

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- A Discord bot token (obtain one by creating an application at the [Discord Developer Portal](https://discord.com/developers/applications))

### Installation Steps

**Step 1: Navigate to the project directory**
```bash
cd /path/to/dbot
```

**Step 2: Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 3: Install required dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Configure your bot token**

First, copy the example environment file:
```bash
cp .env.example .env
```

Then edit the `.env` file and replace the placeholder with your actual Discord bot token:
```
DISCORD_TOKEN=your_actual_token_here
```

**Step 5: Start the bot**
```bash
python3 bot.py
```

Upon successful startup, you should see confirmation messages:
```
Bot logged in as MainBot#XXXX
Synced X command(s)
```

## Inviting the Bot to Your Server

1. Open the [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your bot application from the list
3. Navigate to **OAuth2** and then **URL Generator**
4. Under Scopes, select: `bot`
5. Under Permissions, select:
   - `Send Messages`
   - `Use Slash Commands`
   - `Add Reactions`
6. Copy the generated URL from the bottom of the page
7. Paste the URL into your browser and authorize the bot on your desired server

## Command Usage Examples

Try the following commands in your Discord server to see the bot in action:

```
/ping
→ Response: Pong! (42ms)

/roll
→ Response: You rolled a **4** on a d6

/roll 20
→ Response: You rolled a **17** on a d20

/flip
→ Response: **Heads**!

/choose pizza, tacos, sushi
→ Response: I choose: **tacos**

/poll "Best color?" red, blue, green
→ Creates an interactive poll with numbered reactions
```

## Project Structure

```
dbot/
├── bot.py              # Main bot code
├── requirements.txt    # Python dependencies
├── .env                # Your bot token (keep secret!)
├── .env.example        # Example env file (safe to share)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Learning Points

This project teaches:
- **Discord.py basics** - Creating a bot and handling interactions
- **Python virtual environments** - Managing project dependencies
- **Environment variables** - Securely storing sensitive data
- **Async/await** - Working with asynchronous code
- **Discord slash commands** - Using app_commands decorator
- **Message reactions** - Adding emoji reactions to messages

## Troubleshooting

### `DISCORD_TOKEN not found`
- Make sure you created `.env` and added your token

### Commands don't show up
1. Stop the bot (`Ctrl+C`)
2. Restart it (`python3 bot.py`)
3. Wait for `✓ Synced X command(s)`
4. Refresh Discord (fully close and reopen)

### `Improper token has been passed`
- Your token is invalid or expired
- Go to Discord Developer Portal and regenerate the token
- Update `.env` with the new token

## Next Steps

Try adding:
- A welcome message when bot joins a server
- A user profile/stats command
- A fun fact or joke command
- Moderation commands (kick, ban, etc.)

## Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

---

**Made for learning Python backend development** 🐍
