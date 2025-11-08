# Discord Auto-Reply Bot

Script otomatis untuk membalas semua DM channel di Discord menggunakan module Ditcord dengan Android Mobile Stealth Mode.

## 🌟 Features

- ✅ **Auto-reply to all DM channels** (sekali per channel)
- ✅ **Android Mobile Stealth Mode** (TLS fingerprinting)
- ✅ **Smart tracking** (replied.txt dan error.txt)
- ✅ **Skip bot DMs** automatically
- ✅ **Customizable presence** (online, idle, dnd, invisible)
- ✅ **Random delay** (2-3s) untuk terlihat natural
- ✅ **Max message limit** (optional)
- ✅ **Detailed logging** dengan emoji indicators
- ✅ **Error handling** yang robust

## 📋 Requirements

```bash
# Install ditcord
pip install git+https://github.com/yeweroooo/discord.py-self@adit/ditcord

# Or if already cloned
pip install .
```

## ⚙️ Configuration

Edit file `discord_autoreply.py` bagian configuration:

```python
# ==================== CONFIGURATION ====================
TOKEN = "YOUR_DISCORD_TOKEN_HERE"  # Discord token Anda
MESSAGE = "Hello! This is an automated reply. Thank you for your message!"  # Pesan yang akan dikirim
PRESENCE = "online"  # online, idle, dnd, invisible

# ==================== SETTINGS ====================
setmaxmessage = 0  # 0 = unlimited, >0 = limit jumlah pesan
set_afk = False    # True = AFK mode, False = active
```

### Contoh Konfigurasi

**Basic:**
```python
TOKEN = "YOUR_DISCORD_TOKEN_HERE"
MESSAGE = "Terima kasih atas pesannya! 👋"
PRESENCE = "online"
```

**Limited (10 messages max):**
```python
TOKEN = "YOUR_DISCORD_TOKEN_HERE"
MESSAGE = "Auto-reply: Saya akan segera membalas pesan Anda."
PRESENCE = "idle"
setmaxmessage = 10
```

**Stealth Mode:**
```python
TOKEN = "YOUR_DISCORD_TOKEN_HERE"
MESSAGE = "Hi! I'll get back to you soon."
PRESENCE = "invisible"
set_afk = True
```

## 🚀 Usage

### Step 1: Configure

Edit `discord_autoreply.py` dan isi `TOKEN` dan `MESSAGE`.

### Step 2: Run

```bash
python discord_autoreply.py
```

### Step 3: Monitor

Script akan menampilkan progress real-time:

```
======================================================================
🚀 Starting Discord Auto-Reply Bot
📱 Platform: Android Mobile (Stealth Mode)
======================================================================
⚙️ Configuration:
   Message: Hello! This is an automated reply.
   Presence: online
   Max Messages: Unlimited
   AFK: False
======================================================================

======================================================================
🤖 Discord Auto-Reply Bot Started
📱 Android Mobile Stealth Mode: Active
======================================================================
✅ Logged in as: cihuytest#0
   ID: 1423073323654320168
   Guilds: 5
======================================================================
📄 Loaded 10 replied channels
📄 Loaded 2 error channels
======================================================================
✅ Presence set to: online (AFK: False)

======================================================================
🔍 Fetching all DM channels...
======================================================================
📬 Found 25 DM channels

[1/25] Processing DM Channel: 1234567890123456789
   👤 Recipient: John#1234
   🆔 ID: 9876543210987654321
   🤖 Bot: False
   📤 Sending message...
   ✅ Message sent successfully!
   📨 Message ID: 1111111111111111111
   ⏱️ Delay: 2.45s

[2/25] Processing DM Channel: 9999999999999999999
   👤 Recipient: BotUser#0000
   🆔 ID: 8888888888888888888
   🤖 Bot: True
   ⏭️ Skipping: DM with bot

...

======================================================================
📊 SUMMARY
======================================================================
✅ Successfully replied: 18
❌ Errors: 2
⏭️ Skipped (already processed): 5
📝 Total processed: 25/25
======================================================================
```

## 📁 Output Files

Script akan membuat 2 file otomatis:

### `replied.txt`
Berisi ID channel yang berhasil di-reply:
```
1234567890123456789
9876543210987654321
1111111111111111111
```

### `error.txt`
Berisi ID channel yang error atau skip (bot DMs):
```
9999999999999999999
8888888888888888888
```

## 🔄 Workflow

```
┌─────────────────┐
│   Bot Start     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Load Files     │◄── replied.txt
│                 │◄── error.txt
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Set Presence   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Fetch Private   │
│   Channels      │
└────────┬────────┘
         │
         ▼
    ┌────────┐
    │ For    │
    │ Each   │
    │ DM     │
    └───┬────┘
        │
        ▼
    ┌──────────────┐      Yes    ┌─────────────┐
    │ Is Bot DM?   │─────────────►│ Save to     │
    └───┬──────────┘              │ error.txt   │
        │ No                      └─────────────┘
        ▼
    ┌──────────────┐      Yes    ┌─────────────┐
    │ Already      │─────────────►│ Skip        │
    │ Replied?     │              └─────────────┘
    └───┬──────────┘
        │ No
        ▼
    ┌──────────────┐      Yes    ┌─────────────┐
    │ In Error     │─────────────►│ Skip        │
    │ List?        │              └─────────────┘
    └───┬──────────┘
        │ No
        ▼
    ┌──────────────┐
    │ Send Reply   │
    └───┬──────────┘
        │
        ├─Success─►┌─────────────┐
        │          │ Save to     │
        │          │ replied.txt │
        │          └─────────────┘
        │
        └─Error───►┌─────────────┐
                   │ Save to     │
                   │ error.txt   │
                   └─────────────┘
```

## 🎯 Features Detail

### 1. Smart Skip Logic

- ✅ Skip bot DMs (automatically saved to error.txt)
- ✅ Skip already replied channels (dari replied.txt)
- ✅ Skip error channels (dari error.txt)
- ✅ 1 DM = 1 Reply only

### 2. Error Handling

Script menangani berbagai error:
- `Forbidden`: User block/privacy settings
- `HTTPException`: API errors
- `Unknown errors`: Network issues, etc.

Semua error disimpan ke `error.txt`.

### 3. Natural Behavior

- Random delay 2-3 detik antar pesan
- Customizable presence
- AFK mode support
- Max message limit untuk testing

### 4. Android Mobile Stealth

Semua fitur stealth aktif:
- User-Agent: Android Mobile
- TLS Fingerprint: chrome131_android
- Platform: Android
- Super Properties: Android properties

## 📊 Use Cases

### Testing Mode
```python
setmaxmessage = 5  # Test dengan 5 pesan dulu
```

### Full Auto-Reply
```python
setmaxmessage = 0  # Reply ke semua DM
```

### Stealth Operation
```python
PRESENCE = "invisible"
set_afk = True
```

### Custom Message Per Use Case
```python
# Marketing
MESSAGE = "Terima kasih telah menghubungi kami! Tim kami akan segera merespons."

# Personal
MESSAGE = "Hai! Terima kasih pesannya, akan saya balas secepatnya 👋"

# Auto-responder
MESSAGE = "Saya sedang tidak available saat ini. Pesan Anda akan dibalas dalam 24 jam."
```

## ⚠️ Important Notes

1. **Rate Limits**: Discord memiliki rate limit. Script sudah include random delay.
2. **Token Security**: Jangan share token Anda!
3. **ToS Warning**: Auto-messaging melanggar Discord ToS. Use at your own risk.
4. **Testing**: Test dulu dengan `setmaxmessage = 1` atau `5`.

## 🐛 Troubleshooting

### "No DM channels found"
- Account baru atau belum pernah DM siapa-siapa
- Cek dengan Discord app apakah ada DMs

### "Login failed: Invalid token"
- Token salah atau expired
- Generate token baru

### "Forbidden errors"
- User sudah block Anda
- Privacy settings user
- Normal behavior, saved to error.txt

### Bot berhenti tiba-tiba
- Network issue
- Rate limited
- Restart script

## 📝 Tips

1. **Backup files**: Backup `replied.txt` dan `error.txt` sebelum run ulang
2. **Test first**: Gunakan `setmaxmessage = 1` untuk testing
3. **Custom message**: Sesuaikan `MESSAGE` dengan kebutuhan
4. **Monitor logs**: Perhatikan output untuk tracking progress
5. **Rate limit**: Jangan spam, biarkan delay natural bekerja

## 🔒 Security

- Token disimpan di script (jangan commit ke git!)
- Gunakan `.gitignore` untuk file config
- Jangan share `replied.txt` atau `error.txt` (contain channel IDs)

## 📞 Support

Untuk issues atau questions:
- GitHub: https://github.com/yeweroooo/discord.py-self
- Branch: adit/ditcord

## ✅ Checklist Before Running

- [ ] Installed ditcord package
- [ ] Set `TOKEN` in script
- [ ] Set `MESSAGE` in script
- [ ] Choose `PRESENCE` setting
- [ ] Set `setmaxmessage` (0 for unlimited)
- [ ] Set `set_afk` (True/False)
- [ ] Ready to run!

```bash
python discord_autoreply.py
```

Good luck! 🚀
