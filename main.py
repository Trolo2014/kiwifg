import discord
import os
from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Create an instance of the bot
intents = discord.Intents.default()
intents.members = True  # Enable the members intent to get access to member update events
client = discord.Client(intents=intents)

# Dictionary to store enforced nicknames
enforced_nicknames = {
    762409919210323978: "Kiwi (I'm Shawn's Biggest Fan)"
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_update(before, after):
    # Check if the member has an enforced nickname
    if before.id in enforced_nicknames:
        enforced_nickname = enforced_nicknames[before.id]

        # If the new nickname is different from the enforced one, revert it
        if after.nick != enforced_nickname:
            try:
                await after.edit(nick=enforced_nickname)
                print(f'Reverted {after.name}\'s nickname to {enforced_nickname}')
            except discord.Forbidden:
                print(f'Permission error: Unable to change nickname for {after.name}.')
            except discord.HTTPException as e:
                print(f'HTTP Exception: {e}')

@client.event
async def on_member_join(member):
    # If the user has an enforced nickname, set it when they join
    if member.id in enforced_nicknames:
        enforced_nickname = enforced_nicknames[member.id]
        try:
            await member.edit(nick=enforced_nickname)
            print(f'Set {member.name}\'s nickname to {enforced_nickname}')
        except discord.Forbidden:
            print(f'Permission error: Unable to change nickname for {member.name}.')
        except discord.HTTPException as e:
            print(f'HTTP Exception: {e}')

# Flask route to keep the bot alive
@app.route('/')
def home():
    return 'Bot is running!'

# Run the Flask server
def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Start the bot and Flask server
if __name__ == "__main__":
    import threading
    # Directly using the bot token (not recommended for production)
    token = 
    threading.Thread(target=run_flask).start()
    client.run(token)