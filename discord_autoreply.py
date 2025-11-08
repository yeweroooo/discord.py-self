#!/usr/bin/env python3
"""
Discord Auto-Reply Bot using Ditcord
Automatically replies to all DM channels once
Uses Android Mobile Stealth Mode
"""
import ditcord
import asyncio
import random
from pathlib import Path
from typing import Set

# ==================== CONFIGURATION ====================
TOKEN = "YOUR_DISCORD_TOKEN_HERE"
MESSAGE = "Hello! This is an automated reply. Thank you for your message!"
PRESENCE = "online"  # online, idle, dnd, invisible

# ==================== SETTINGS ====================
setmaxmessage = 0  # 0 = unlimited
set_afk = False

# ==================== FILE PATHS ====================
REPLIED_FILE = Path("replied.txt")
ERROR_FILE = Path("error.txt")

# ==================== GLOBAL VARIABLES ====================
replied_channels: Set[int] = set()
error_channels: Set[int] = set()


# ==================== HELPER FUNCTIONS ====================

def load_channel_ids(file_path: Path) -> Set[int]:
    """Load channel IDs from file"""
    if not file_path.exists():
        file_path.touch()
        return set()

    channel_ids = set()
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and line.isdigit():
                channel_ids.add(int(line))
    return channel_ids


def save_channel_id(file_path: Path, channel_id: int):
    """Save channel ID to file"""
    with open(file_path, 'a') as f:
        f.write(f"{channel_id}\n")


def is_bot_dm_channel(channel: ditcord.DMChannel, bot_user: ditcord.ClientUser) -> bool:
    """Check if DM channel is with a bot"""
    return channel.recipient and channel.recipient.bot


# ==================== DISCORD CLIENT ====================

class AutoReplyClient(ditcord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_replied = 0
        self.total_errors = 0
        self.total_skipped = 0

    async def on_ready(self):
        print("=" * 70)
        print("🤖 Discord Auto-Reply Bot Started")
        print("📱 Android Mobile Stealth Mode: Active")
        print("=" * 70)
        print(f"✅ Logged in as: {self.user.name}#{self.user.discriminator}")
        print(f"   ID: {self.user.id}")
        print(f"   Guilds: {len(self.guilds)}")
        print("=" * 70)

        # Load already processed channels
        global replied_channels, error_channels
        replied_channels = load_channel_ids(REPLIED_FILE)
        error_channels = load_channel_ids(ERROR_FILE)

        print(f"📄 Loaded {len(replied_channels)} replied channels")
        print(f"📄 Loaded {len(error_channels)} error channels")
        print("=" * 70)

        # Set presence
        await self.set_presence()

        # Start auto-reply process
        await self.auto_reply_all_dms()

    async def set_presence(self):
        """Set user presence/status"""
        status_map = {
            "online": ditcord.Status.online,
            "idle": ditcord.Status.idle,
            "dnd": ditcord.Status.dnd,
            "invisible": ditcord.Status.invisible
        }

        status = status_map.get(PRESENCE.lower(), ditcord.Status.online)

        try:
            await self.change_presence(
                status=status,
                afk=set_afk
            )
            print(f"✅ Presence set to: {PRESENCE} (AFK: {set_afk})")
        except Exception as e:
            print(f"⚠️ Failed to set presence: {e}")

    async def auto_reply_all_dms(self):
        """Main function to auto-reply to all DM channels"""
        print("\n" + "=" * 70)
        print("🔍 Fetching all DM channels...")
        print("=" * 70)

        try:
            # Fetch all private channels
            private_channels = self.private_channels

            dm_channels = [
                ch for ch in private_channels
                if isinstance(ch, ditcord.DMChannel)
            ]

            print(f"📬 Found {len(dm_channels)} DM channels")

            if not dm_channels:
                print("⚠️ No DM channels found")
                await self.close()
                return

            # Process each DM channel
            processed = 0
            for i, channel in enumerate(dm_channels, 1):
                # Check if max message limit reached
                if setmaxmessage > 0 and self.total_replied >= setmaxmessage:
                    print(f"\n⚠️ Max message limit ({setmaxmessage}) reached")
                    break

                await self.process_dm_channel(channel, i, len(dm_channels))
                processed += 1

            # Summary
            print("\n" + "=" * 70)
            print("📊 SUMMARY")
            print("=" * 70)
            print(f"✅ Successfully replied: {self.total_replied}")
            print(f"❌ Errors: {self.total_errors}")
            print(f"⏭️ Skipped (already processed): {self.total_skipped}")
            print(f"📝 Total processed: {processed}/{len(dm_channels)}")
            print("=" * 70)

        except Exception as e:
            print(f"❌ Error fetching DM channels: {e}")
            import traceback
            traceback.print_exc()

        finally:
            print("\n🔴 Closing bot...")
            await self.close()

    async def process_dm_channel(self, channel: ditcord.DMChannel, index: int, total: int):
        """Process a single DM channel"""
        channel_id = channel.id
        recipient = channel.recipient

        print(f"\n[{index}/{total}] Processing DM Channel: {channel_id}")

        if recipient:
            print(f"   👤 Recipient: {recipient.name}#{recipient.discriminator}")
            print(f"   🆔 ID: {recipient.id}")
            print(f"   🤖 Bot: {recipient.bot}")
        else:
            print(f"   ⚠️ No recipient info available")

        # Check if channel is with a bot
        if is_bot_dm_channel(channel, self.user):
            print(f"   ⏭️ Skipping: DM with bot")
            if channel_id not in error_channels:
                save_channel_id(ERROR_FILE, channel_id)
                error_channels.add(channel_id)
            self.total_skipped += 1
            return

        # Check if already replied
        if channel_id in replied_channels:
            print(f"   ⏭️ Skipping: Already replied")
            self.total_skipped += 1
            return

        # Check if in error list
        if channel_id in error_channels:
            print(f"   ⏭️ Skipping: In error list")
            self.total_skipped += 1
            return

        # Try to send reply
        try:
            print(f"   📤 Sending message...")
            message = await channel.send(MESSAGE)

            # Random delay 2-3 seconds
            delay = random.uniform(2.0, 3.0)
            await asyncio.sleep(delay)

            print(f"   ✅ Message sent successfully!")
            print(f"   📨 Message ID: {message.id}")
            print(f"   ⏱️ Delay: {delay:.2f}s")

            # Save to replied.txt
            save_channel_id(REPLIED_FILE, channel_id)
            replied_channels.add(channel_id)
            self.total_replied += 1

        except ditcord.Forbidden as e:
            print(f"   ❌ Forbidden: {e}")
            print(f"   💾 Saving to error.txt")
            save_channel_id(ERROR_FILE, channel_id)
            error_channels.add(channel_id)
            self.total_errors += 1

        except ditcord.HTTPException as e:
            print(f"   ❌ HTTP Error: {e}")
            print(f"   💾 Saving to error.txt")
            save_channel_id(ERROR_FILE, channel_id)
            error_channels.add(channel_id)
            self.total_errors += 1

        except Exception as e:
            print(f"   ❌ Unexpected Error: {e}")
            print(f"   💾 Saving to error.txt")
            save_channel_id(ERROR_FILE, channel_id)
            error_channels.add(channel_id)
            self.total_errors += 1
            import traceback
            traceback.print_exc()


# ==================== MAIN FUNCTION ====================

async def main():
    print("\n" + "=" * 70)
    print("🚀 Starting Discord Auto-Reply Bot")
    print("📱 Platform: Android Mobile (Stealth Mode)")
    print("=" * 70)

    # Validate configuration
    if TOKEN == "YOUR_DISCORD_TOKEN_HERE":
        print("❌ Error: Please set your Discord token in the TOKEN variable")
        return

    print(f"⚙️ Configuration:")
    print(f"   Message: {MESSAGE}")
    print(f"   Presence: {PRESENCE}")
    print(f"   Max Messages: {setmaxmessage if setmaxmessage > 0 else 'Unlimited'}")
    print(f"   AFK: {set_afk}")
    print("=" * 70)

    # Create and run client
    client = AutoReplyClient()

    try:
        await client.start(TOKEN)
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user (Ctrl+C)")
    except ditcord.LoginFailure:
        print("\n❌ Login failed: Invalid token")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
