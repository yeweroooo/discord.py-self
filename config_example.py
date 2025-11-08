# Discord Auto-Reply Bot Configuration Example
# Copy this file to config.py and fill in your details

# ==================== REQUIRED CONFIGURATION ====================

# Your Discord Token
# Get this from: https://discord.com/developers/applications
# Or from browser console (NOT RECOMMENDED for security)
TOKEN = "YOUR_DISCORD_TOKEN_HERE"

# Message to send to all DM channels
MESSAGE = "Hello! This is an automated reply. Thank you for your message!"

# Your presence status
# Options: "online", "idle", "dnd", "invisible"
PRESENCE = "online"

# ==================== OPTIONAL SETTINGS ====================

# Maximum messages to send (0 = unlimited)
# Useful for testing or limiting the scope
setmaxmessage = 0

# AFK mode (True = away from keyboard, False = active)
set_afk = False

# ==================== EXAMPLES ====================

# Example 1: Basic auto-reply
"""
TOKEN = "YOUR_DISCORD_TOKEN_HERE"
MESSAGE = "Thanks for your message! I'll get back to you soon."
PRESENCE = "online"
setmaxmessage = 0
set_afk = False
"""

# Example 2: Limited replies (for testing)
"""
TOKEN = "YOUR_DISCORD_TOKEN_HERE"
MESSAGE = "Auto-reply test message"
PRESENCE = "idle"
setmaxmessage = 5  # Only reply to first 5 DMs
set_afk = False
"""

# Example 3: Stealth mode
"""
TOKEN = "YOUR_DISCORD_TOKEN_HERE"
MESSAGE = "Hi! Currently unavailable."
PRESENCE = "invisible"  # Hide your status
setmaxmessage = 0
set_afk = True
"""

# Example 4: Marketing/Business
"""
TOKEN = "YOUR_TOKEN"
MESSAGE = '''Terima kasih telah menghubungi kami!

Tim customer service kami akan segera merespons pesan Anda dalam waktu 1x24 jam.

Untuk informasi lebih lanjut, kunjungi website kami di www.example.com

Salam,
Tim Support'''
PRESENCE = "online"
setmaxmessage = 0
set_afk = False
"""

# Example 5: Personal auto-responder
"""
TOKEN = "YOUR_TOKEN"
MESSAGE = '''Hey! 👋

Saya sedang sibuk saat ini dan mungkin tidak bisa langsung membalas.
Akan saya respon secepat mungkin ya!

Thanks for understanding!'''
PRESENCE = "idle"
setmaxmessage = 0
set_afk = True
"""
