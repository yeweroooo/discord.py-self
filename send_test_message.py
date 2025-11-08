#!/usr/bin/env python3
"""
Simple script to send a test message to a DM channel
Run this on your computer with: python send_test_message.py
"""
import ditcord
import asyncio

async def main():
    # Your configuration
    TOKEN = "YOUR_DISCORD_TOKEN_HERE"
    CHANNEL_ID = 1423206192339095572
    MESSAGE = "adit ganteng"

    print("=" * 60)
    print("🚀 Ditcord Message Sender")
    print("📱 Android Mobile Stealth Mode")
    print("=" * 60)

    # Create client
    client = ditcord.Client()

    @client.event
    async def on_ready():
        print(f'\n✅ Successfully connected!')
        print(f'   User: {client.user.name}#{client.user.discriminator}')
        print(f'   ID: {client.user.id}')
        print(f'   📱 Platform: Android Mobile (Stealth)')
        print(f'   🔒 Guilds: {len(client.guilds)}')
        print('-' * 60)

        try:
            # Fetch channel
            print(f'\n🔍 Fetching channel {CHANNEL_ID}...')
            channel = await client.fetch_channel(CHANNEL_ID)
            print(f'✅ Channel found: {channel}')

            # Send message
            print(f'\n📤 Sending message: "{MESSAGE}"')
            msg = await channel.send(MESSAGE)

            print(f'\n✅ Message sent successfully!')
            print(f'   Message ID: {msg.id}')
            print(f'   Content: {msg.content}')
            print(f'   Timestamp: {msg.created_at}')
            print(f'   Jump URL: {msg.jump_url}')

        except ditcord.Forbidden as e:
            print(f'\n❌ Permission Error: {e}')
            print('   You do not have permission to send messages in this channel')

        except ditcord.NotFound as e:
            print(f'\n❌ Not Found: {e}')
            print(f'   Channel {CHANNEL_ID} does not exist or is not accessible')

        except ditcord.HTTPException as e:
            print(f'\n❌ Discord API Error: {e}')

        except Exception as e:
            print(f'\n❌ Unexpected Error: {e}')
            import traceback
            traceback.print_exc()

        finally:
            print('\n' + '=' * 60)
            print('🔴 Closing connection...')
            print('=' * 60)
            await client.close()

    # Start the client
    try:
        await client.start(TOKEN)
    except KeyboardInterrupt:
        print('\n⚠️ Interrupted by user (Ctrl+C)')
    except Exception as e:
        print(f'\n❌ Connection failed: {e}')
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # Run the async main function
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\n👋 Goodbye!')
