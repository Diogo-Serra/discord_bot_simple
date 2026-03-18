# MainBot 🤖

A simple Discord bot with fun utility commands. Great for learning Python backend development!

## Features

- **`/ping`** - Check if the bot is online (responds with latency)
- **`/roll`** - Roll a dice (default: d6, or specify: `/roll 20` for d20)
- **`/flip`** - Flip a coin (Heads or Tails)
- **`/choose`** - Pick one random option (example: `/choose pizza, tacos, sushi`)
- **`/poll`** - Create a poll with emoji reactions (example: `/poll "Favorite pizza?" pepperoni, margherita, hawaiian`)

## Quick Setup

### Prerequisites
- Python 3.8+
- Discord bot token (create at [Discord Developer Portal](https://discord.com/developers/applications))

### 1. Clone/Navigate to project
```bash
cd /path/to/dbot
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your bot token
Copy the example and add your token:
```bash
cp .env.example .env
```

Edit `.env` and replace the placeholder with your Discord bot token:
```
DISCORD_TOKEN=your_actual_token_here
```

### 5. Run the bot
```bash
python3 bot.py
```

You should see:
```
✓ Bot logged in as MainBot#XXXX
✓ Synced X command(s)
```

## Inviting the Bot to Your Server

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your bot application
3. Go to **OAuth2** → **URL Generator**
4. Select scopes: `bot`
5. Select permissions: `Send Messages`, `Use Slash Commands`, `Add Reactions`
6. Copy the generated URL and open it in your browser
7. Select your server and authorize

## Usage Examples

In your Discord server:

```
/ping
→ Pong! 🏓 (42ms)

/roll
→ 🎲 You rolled a **4** on a d6

/roll 20
→ 🎲 You rolled a **17** on a d20

/flip
→ 🪙 **Heads**!

/choose pizza, tacos, sushi
→ 🎯 I choose: **tacos**

/poll "Best color?" red, blue, green
→ Creates a poll with emoji reactions (1️⃣, 2️⃣, 3️⃣)
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
