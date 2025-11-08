# Ditcord.py-self Usage Examples

## Installation

```bash
# Install from GitHub
pip install git+https://github.com/yeweroooo/discord.py-self@adit/ditcord

# Or clone and install locally
git clone https://github.com/yeweroooo/discord.py-self
cd discord.py-self
git checkout adit/ditcord
pip install .
```

## Example 1: Send Message to DM Channel

```python
import asyncio
import ditcord

class MyClient(ditcord.Client):
    async def on_ready(self):
        print(f'✅ Logged in as {self.user}')
        print(f'📱 Android Mobile Stealth Mode: Active')

        # Send message to DM channel
        channel_id = 1423206192339095572
        channel = await self.fetch_channel(channel_id)

        # Send the message
        message = await channel.send('adit ganteng')
        print(f'✅ Message sent: {message.content}')

        # Close after sending
        await self.close()

# Run the client
token = "YOUR_TOKEN_HERE"
client = MyClient()
asyncio.run(client.start(token))
```

## Example 2: Interactive Bot

```python
import ditcord

class MyBot(ditcord.Client):
    async def on_ready(self):
        print(f'✅ {self.user} is online!')
        print(f'📱 Android Mobile Stealth Mode')

    async def on_message(self, message):
        # Ignore own messages
        if message.author == self.user:
            return

        # Respond to commands
        if message.content == '!ping':
            await message.channel.send('🏓 Pong!')

        elif message.content == '!info':
            await message.channel.send(
                f'Running Ditcord v{ditcord.__version__}\n'
                f'Platform: Android Mobile (Stealth)'
            )

token = "YOUR_TOKEN_HERE"
client = MyBot()
client.run(token)
```

## Example 3: Send Message with Embed

```python
import ditcord

async def send_embed_message():
    token = "YOUR_TOKEN_HERE"
    channel_id = 1423206192339095572

    client = ditcord.Client()
    await client.start(token)

    # Wait for ready
    await client.wait_until_ready()

    # Get channel
    channel = await client.fetch_channel(channel_id)

    # Create embed
    embed = ditcord.Embed(
        title="Test Embed",
        description="adit ganteng",
        color=0x00ff00
    )
    embed.add_field(name="Platform", value="Android Mobile")
    embed.add_field(name="Stealth", value="Active")

    # Send embed
    await channel.send(embed=embed)
    print('✅ Embed sent!')

    await client.close()

import asyncio
asyncio.run(send_embed_message())
```

## Example 4: Commands Extension

```python
from ditcord.ext import commands

bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is ready!')
    print(f'📱 Android Mobile Stealth')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)

@bot.command()
async def dm(ctx, channel_id: int, *, message):
    """Send message to specific DM channel"""
    channel = await bot.fetch_channel(channel_id)
    await channel.send(message)
    await ctx.send(f'✅ Message sent to channel {channel_id}')

token = "YOUR_TOKEN_HERE"
bot.run(token)
```

## Example 5: Quick Message Sender

```python
import ditcord
import asyncio

async def quick_send(token: str, channel_id: int, message: str):
    """Quick function to send a message"""
    client = ditcord.Client()

    @client.event
    async def on_ready():
        print(f'✅ Connected as {client.user}')
        channel = await client.fetch_channel(channel_id)
        await channel.send(message)
        print(f'✅ Sent: {message}')
        await client.close()

    await client.start(token)

# Usage
token = "YOUR_DISCORD_TOKEN_HERE"
channel_id = 1423206192339095572
message = "adit ganteng"

asyncio.run(quick_send(token, channel_id, message))
```

## Example 6: Error Handling

```python
import ditcord

class SafeClient(ditcord.Client):
    async def on_ready(self):
        print(f'✅ Ready: {self.user}')

        channel_id = 1423206192339095572

        try:
            # Fetch channel
            channel = await self.fetch_channel(channel_id)

            # Send message
            msg = await channel.send('adit ganteng')
            print(f'✅ Message sent: {msg.id}')

        except ditcord.Forbidden:
            print('❌ No permission to send message')
        except ditcord.NotFound:
            print('❌ Channel not found')
        except ditcord.HTTPException as e:
            print(f'❌ HTTP error: {e}')
        except Exception as e:
            print(f'❌ Error: {e}')
        finally:
            await self.close()

token = "YOUR_TOKEN_HERE"
client = SafeClient()
client.run(token)
```

## Android Mobile Stealth Features

All examples above automatically use:
- ✅ Android mobile user-agent
- ✅ Android platform properties
- ✅ Mobile client hints
- ✅ Android TLS fingerprinting (if supported)
- ✅ Low memory usage
- ✅ Optimized for stealth

## Your Token

```python
token = "YOUR_DISCORD_TOKEN_HERE"
```

**Account Info:**
- Username: cihuytest#0
- Email: cihuy1577@gmail.com
- ID: 1423073323654320168

## Notes

1. **Stealth Mode**: All connections use Android mobile fingerprint automatically
2. **Self-bot**: Use `self_bot=True` when using commands extension
3. **Rate Limits**: Library handles Discord rate limits automatically
4. **Memory**: Optimized for low RAM usage with gc.collect()
5. **Compatibility**: Works with Python 3.10+

## Running in Production

```python
import ditcord
import logging

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

class ProductionClient(ditcord.Client):
    async def on_ready(self):
        print(f'✅ Production bot ready: {self.user}')
        print(f'📱 Stealth: Active')
        print(f'🔒 Guilds: {len(self.guilds)}')

    async def on_error(self, event, *args, **kwargs):
        import traceback
        print(f'❌ Error in {event}')
        traceback.print_exc()

token = "YOUR_TOKEN_HERE"
client = ProductionClient()
client.run(token)
```

## Support

For issues or questions:
- GitHub: https://github.com/yeweroooo/discord.py-self
- Branch: adit/ditcord
