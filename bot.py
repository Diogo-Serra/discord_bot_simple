import discord
from discord import app_commands
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f"✓ Bot logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✓ Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"✗ Failed to sync: {e}")


@bot.tree.command(name="ping", description="Check if bot is online")
async def ping(interaction: discord.Interaction):
    """Responds with Pong! and the bot's latency"""
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(
        f"Ok! ({latency}ms)"
    )


@bot.tree.command(name="roll",
                  description="Roll a dice (default: d6)")
@app_commands.describe(sides="Number of sides (default 6)")
async def roll(interaction: discord.Interaction, sides: int = 6):
    """Rolls a dice with specified sides"""
    if sides < 1:
        await interaction.response.send_message(
            "❌ Dice sides must be 1 or higher!"
        )
        return
    result = random.randint(1, sides)
    await interaction.response.send_message(
        f"🎲 You rolled a **{result}** on a d{sides}"
    )


@bot.tree.command(name="flip", description="Flip a coin")
async def flip(interaction: discord.Interaction):
    """Flips a coin"""
    result = random.choice(["Heads", "Tails"])
    await interaction.response.send_message(f"🪙 **{result}**!")


@bot.tree.command(name="choose",
                  description="Pick one from multiple options")
@app_commands.describe(options="Comma-separated options to choose from")
async def choose(interaction: discord.Interaction, options: str):
    """Randomly picks one option from the list"""
    option_list = [opt.strip() for opt in options.split(",")]
    if len(option_list) < 2:
        msg = "❌ Provide 2+ options! Example: `pizza, tacos, sushi`"
        await interaction.response.send_message(msg)
        return
    choice = random.choice(option_list)
    await interaction.response.send_message(f"🎯 I choose: **{choice}**")


@bot.tree.command(name="poll", description="Create a poll with reactions")
@app_commands.describe(
    question="The poll question",
    options="Options separated by commas (e.g., yes, no, maybe)"
)
async def poll(interaction: discord.Interaction, question: str, options: str):
    """Creates a poll with reaction-based voting"""
    option_list = [opt.strip() for opt in options.split(",")]
    if len(option_list) < 2:
        await interaction.response.send_message(
            "❌ Provide 2+ options! Example: `yes, no, maybe`"
        )
        return
    if len(option_list) > 10:
        await interaction.response.send_message(
            "❌ Maximum 10 options allowed."
        )
        return

    # Number emojis for reactions
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣",
              "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    # Build poll message
    poll_text = f"📊 **{question}**\n\n"
    for i, option in enumerate(option_list):
        poll_text += f"{emojis[i]} {option}\n"

    # Send message and add reactions
    await interaction.response.defer()
    msg = await interaction.followup.send(poll_text)

    # Add reactions to message
    for i in range(len(option_list)):
        await msg.add_reaction(emojis[i])

# Run the bot
if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("✗ Error: DISCORD_TOKEN not found in .env file")
        exit(1)
    bot.run(token)
