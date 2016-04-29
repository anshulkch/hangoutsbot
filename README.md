# Introduction

Hangupsbot is a chat bot designed for working with Google Hangouts.

Please see:
* [Instructions for installing](https://github.com/hangoutsbot/hangoutsbot/blob/master/INSTALL.md)
* [Issue tracker](https://github.com/hangoutsbot/hangoutsbot/issues) for bugs, issues and feature requests
* [Wiki](https://github.com/hangoutsbot/hangoutsbot/wiki) for everything else


## Repository Links
* [GitHub Organisation](https://github.com/hangoutsbot)
* [anshulkch'sfork](https://github.com/hangoutsbot)
* [Translation Project](https://github.com/hangoutsbot/hangoutsbot-locales)
* [Reference Hangups Library](https://github.com/hangoutsbot/hangups)


## Features
* **Mentions** :
  If somebody mentions you in a room, receive a private hangout from the bot with details on the mention,
  including context, room and person who mentioned you.
* **Syncouts** :
  This allows syncing of group chats that want to chat with more than 150 people at once. This way EVERY SINGLE PERSON in the ENTIRE school can see your cat videos. perfect.
* **Cross-chat Syncouts** :
  Half of your nonexistent friends are on Slack? No problem! You can connect them into the same room to communicate. Jkjkjk but seriously. You can do that.
* **Plugins and sinks** :
  The bot has [instructions for developing your own plugins and sinks](https://github.com/hangoutsbot/hangoutsbot/wiki/Authoring-Bot-Extensions), allowing the bot to interact
  with external services such as your company website, Google scripts and much more. That's right. Even the Urban Dictionary. Don't get any dirty thoughts though, somebody might have to yank your head out of the gutter.
* **Insult command** :
Got a friend you hate? Use the /bot insult command on them to get em back, but don't abuse it. That's kinda cyber-bullying... not cool.
* **Plugins** :
 tons of great plugins already preloaded, including the API if you want to develop some yourself: [Plugin-List](https://github.com/hangoutsbot/hangoutsbot/wiki/Plugin-List)

# Running The Bot

Note: **First run?** See the [installation instructions](https://github.com/hangoutsbot/hangoutsbot/blob/master/INSTALL.md)

To execute:

`source venv/bin/activate`  
`python3 hangupsbot.py`

```
usage: hangupsbot [-h] [-d] [--log LOG] [--cookies COOKIES] [--memory MEMORY] [--config CONFIG] [--version]

optional arguments:
-h, --help         show this help message and exit
-d, --debug        log detailed debugging messages (default: False)
--log LOG          log file path (default:
                   ~/.local/share/hangupsbot/hangupsbot.log)
--cookies COOKIES  cookie storage path (default:
                   ~/.local/share/hangupsbot/cookies.json)
--memory MEMORY    memory storage path (default:
                   ~/.local/share/hangupsbot/memory.json)
--config CONFIG    config storage path (default:
                   ~/.local/share/hangupsbot/config.json)
--version          show program's version number and exit
```

# Bot Configuration for Administrators

Configuration directives can be specified in `config.json`.

Please note that the `config.json` file supplied with the repository is not
  supposed to be edited/changed. It is the reference file used by the bot to
  create the actual configuration file located elsewhere in the system. To find out
  where the actual file is, please see the [**Additional Configuration** section](https://github.com/hangoutsbot/hangoutsbot/blob/master/INSTALL.md#additional-configuration)
  in the [installation](https://github.com/hangoutsbot/hangoutsbot/blob/master/INSTALL.md)
  instructions.

  You can also use the `/bot help` command to locate the files.

Most configuration directives are specified **globally**
* Global directives are always specified in the "root" of `config.json`.
* To specify a per-conversation directive, the same configuration option should
  be defined as `config.conversations[<conversation-id>].<configuration option>`.
* Per-conversation directives override global settings, if both are set.
* Manually-configured per-conversation directives are DEPRECATED.

## Plugins

The `plugins` key in `config.json` allows you to optionally specify a list of plugins
  that will be loaded by the bot on startup. If this option is left as `null`, then
  all available plugins will be loaded.

To specify the plugins to be loaded, first ensure that the correct `.py` files are
  inside your `hangupsbot/plugin/` directory, then modify the `plugins` key in
  `config.json` to reflect which plugins/files you want to load e.g.
    `plugins: ["mentions", "default", "chance", "syncrooms"]`

Some plugins may require extra configuration.
  `config.json` is the the configuration provider for the bot and its plugins.

The wiki has a more comprehensive **[list of plugins](https://github.com/hangoutsbot/hangoutsbot/wiki/Plugin-List)**...

# Interacting with the Bot

There are two general types of interactions with the bot:
* **`/bot` commands** begin with `/bot` e.g. `/bot dosomething`
  * some bot commands are admin-only
* custom interactions (usage and accessibility varies by plugin)

The base bot supports some basic command even without any plugins loaded.
  Here is a partial list:

`/bot help`
* Bot lists all supported commands in a private message with the user

`/bot ping`
* Bot replies with a `pong`.

`/bot version`
* Bot replies with the version number of the framework

A full list of commands supported by the base framework is available at the
  [**Core Commands**](https://github.com/hangoutsbot/hangoutsbot/wiki/Core-Commands)
  wiki page.

The wiki also has a
  [**list of plugins**](https://github.com/hangoutsbot/hangoutsbot/wiki/Plugin-List)
  detailing available plugins with commands lists and usage.

# Updating

* Navigate to the bot directory (eg. `cd ~/hangupsbot`)
* Change to the latest stable branch using `git checkout master`
* `git pull` to pull the latest version of hangupsbot
* `pip3 install -r requirements.txt --upgrade`
* Restart the bot

# Debugging

* Run the bot with the `-d` parameter e.g. `python3 hangupsbot.py -d` - this
  lowers the log level to `INFO` for a more verbose and informative log file.
* `tail` the log file, which is probably located at
  `/<user>/.local/share/hangupsbot/hangupsbot.log` - the location varies by
  distro!
* Console output (STDOUT) is fairly limited whatever the log level, so rely
  on the output of the log file instead.

## Tips for troubleshooting
**Program isn't running:**
* Update `hangupsbot` and `hangups`
* Run `hangups` to check if the original hangups library is working
  * If there are errors, delete the cookie at ``~/.local/share/hangupsbot/cookies.json` and try again
  * Log into your Google Account from the server's address.

**Bot isn't responding to messages:**
* Check that the chats are not going into the 'Invites' section of Hangouts.

# Credits / History

Hangoutsbot is derived from the [mogunsamang](https://gitlab.sabah.io/eol/mogunsamang) bot,
  which itself is a fork of xmikos's [hangupsbot](https://github.com/xmikos/hangupsbot)

On 2015-06-20, this fork was detached and made standalone on GitHub

On 2015-07-03, the fork was made into a Github Organisation

This bot has been modified to suit [anshukch's](https://github.com/anshulkch) needs
