# Simple Discord Ping Bot

A minimal Discord bot that responds to `/ping` with a pong message and latency.

## Quick Setup

### 1. Create your bot on Discord Developer Portal
- Go to https://discord.com/developers/applications
- Click "New Application"
- Go to "Bot" → "Add Bot"
- Under TOKEN, click "Copy" (this is your bot token)

### 2. Set up the environment
```bash
cd dbot
cp .env.example .env
```

### 3. Add your token to .env
Edit `.env` and replace `your_bot_token_here` with your actual bot token:
```
DISCORD_TOKEN=
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the bot
```bash
python bot.py
```

You should see:
```
✓ Bot logged in as YourBotName#0000
✓ Syncing commands...
✓ Synced 1 command(s)
```

### 6. Invite the bot to your server
- In Developer Portal, go to OAuth2 → URL Generator
- Select scopes: `bot`
- Select permissions: `Send Messages`, `Use Slash Commands`
- Copy the generated URL and open it in your browser

### 7. Test it
In your Discord server, type `/ping` and the bot will respond with "Pong! 🏓 (Xms)"

## Commands

- `/ping` - Check if the bot is online (responds with latency)
