ditcord.py-self
================

.. image:: https://img.shields.io/endpoint?color=neon&url=https%3A%2F%2Ftg.sumanjay.workers.dev%2Fdpy_self
   :target: https://t.me/dpy_self
   :alt: Telegram chat
.. image:: https://img.shields.io/pypi/v/ditcord.py-self.svg
   :target: https://pypi.python.org/pypi/ditcord.py-self
   :alt: PyPI version info
.. image:: https://img.shields.io/pypi/pyversions/ditcord.py.svg
   :target: https://pypi.python.org/pypi/ditcord.py-self
   :alt: PyPI supported Python versions
.. image:: https://img.shields.io/pypi/dm/ditcord.py-self.svg
   :target: https://pypi.python.org/pypi/ditcord.py-self
   :alt: PyPI downloads per month

A modern, easy-to-use, feature-rich, and async-ready API wrapper for Discord's user API written in Python.

**Ditcord is a stealth fork with Android mobile TLS fingerprinting (JA3/JA3S spoofing) for maximum detection avoidance.**

| **Note:**
| Automating user accounts is against the Discord ToS. This library is a proof of concept and I cannot recommend using it. Do so at your own risk.
|

| **Credits:**
- `Rapptz <https://github.com/Rapptz>`_ for the original library this fork is based on. Without it, the project would not exist.
- `arandomnewaccount <https://www.reddit.com/user/obviouslymymain123/>`_ for help when the project was first started.

Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- Optimised in both speed and memory (low RAM usage).
- Mostly compatible with the upstream ``discord.py``.
- Prevents user account automation detection.
- **Android mobile TLS fingerprinting with JA3/JA3S spoofing via curl-cffi.**
- **Maximum stealth mode with mobile device emulation.**
- Implements vast amounts of the user account-specific API. For a non-exhaustive list:

  * Sessions
  * Read states
  * Connections
  * Relationships
  * Experiments
  * Protobuf user settings
  * Application/team management
  * Store/SKUs/entitlements
  * Billing (e.g. subscriptions, payments, boosts, promotions, etc.)
  * Interactions (slash commands, buttons, etc.)

Installing
----------

**Python 3.10 or higher is required** (recommended: Python 3.12+ for best performance).

To install the library without full voice support, you can just run the following command:

.. note::

    A `Virtual Environment <https://docs.python.org/3/library/venv.html>`__ is recommended to install
    the library, especially on Linux where the system Python is externally managed and restricts which
    packages you can install on it.


.. code:: sh

    # Linux/macOS
    python3 -m pip install -U ditcord.py-self

    # Windows
    py -3 -m pip install -U ditcord.py-self

Otherwise to get voice support you should run the following command:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "ditcord.py-self[voice]"

    # Windows
    py -3 -m pip install -U ditcord.py-self[voice]


To install the development version, do the following:

.. code:: sh

    $ git clone https://github.com/yeweroooo/discord.py-self
    $ cd discord.py-self
    $ python3 -m pip install -U .[voice]


Optional Packages
~~~~~~~~~~~~~~~~~~

* `PyNaCl <https://pypi.org/project/PyNaCl/>`__ (for voice support)

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``dnf``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.6-dev`` for Python 3.6)

Using with Upstream
~~~~~~~~~~~~~~~~~~~~

**Ditcord is designed to replace discord.py entirely.** It uses the ``ditcord`` package name to avoid conflicts with the upstream ``discord.py`` library. This allows you to use both libraries side-by-side if needed.

Simply use ``import ditcord`` instead of ``import discord`` in your code.

Quick Example
--------------

.. code:: py

    import ditcord

    class MyClient(ditcord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # only respond to ourselves
            if message.author != self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    client = MyClient()
    client.run('token')

Bot Example
~~~~~~~~~~~~~

.. code:: py

    import ditcord
    from ditcord.ext import commands

    bot = commands.Bot(command_prefix='>', self_bot=True)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

You can find more examples in the examples directory.

Links
------

- `Documentation <https://discordpy-self.readthedocs.io/en/latest/index.html>`_
- `Project updates <https://t.me/dpy_self>`_
- `Discussion & support <https://t.me/dpy_self_discussions>`_
