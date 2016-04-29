# Preparing your Environment

**install python 3.4 from source**
```
wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tgz
tar xvf Python-3.4.2.tgz
cd Python-3.4.2
./configure
sudo apt-get install build-essential
make
make test
sudo make install
```
**update libraries**
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential python-dev python-setuptools python3-pip
sudo apt-get install build-essential libncursesw5-dev libgdm-dev libc6-dev
sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install libssl-dev openssl
```
**git clone the repository**

*make sure to cd to a new directory first(`cd /home/<user>/hangoutsbot`)

if directory does not exist:
```
cd /home/<user>
sudo mkdir hangoutsbot
cd hangoutsbot
```
```
git clone https://github.com/anshulkch/hangoutsbot
```

**install a virtual environment**
```
pip3 install virtualenv
sudo apt-get install virtualenv
virtualenv venv -p python3
```
**install dependencies**
```
pip3 install -r requirements.txt
```

# First-Run

You need to **run the bot for the first time**. You will need at least
  two gmail accounts: one is your actual account, the other will be your
  bot account.

The basic syntax for running the bot (assuming you are in the root
  of the cloned repository (``/home/<user>/hangoutsbot``) is:
```
source venv/bin/activate
cd hangupsbot
python3 hangupsbot/hangupsbot.py
```

If you are having problems starting the bot, appending a `-d` at the
  end will dump more details into the bot logs e.g.
  `python3 hangupsbot.py -d` - more configuration
  directives can be found at the end of the README file.

You will be prompted by a link to a website, which is the portal for connecting the bot to your account. Once you are logged in to your bot account in the browser of your choice, paste the link. You will be prompted to continue setting up your "Android TV". Copy the code received, and paste it into the terminal to store it in the bot's memory files.

If the login is sucessful, you will see
  additional logs about plugins being loaded. The credentials will be
  saved so that running the bot again will not prompt you for username
  and password again.

To quit the bot from the console, press CTRL-C

# Initial Configuration

DO NOT EDIT the `config.json` supplied with the bot. It is the
  reference file used to generate the actual config file, which
  is located elsewhere. Please see the next section on
  **Additional Configuration** to get the location of the
  actual configuration file if you need to edit it manually.

You will need to add your actual Hangouts user as a bot administrator.

This will be accomplished using the supplied **starter** plugin with
  the default supplied configuration.

1. Using a hangouts client and your actual gmail account, open a
   hangout with the bot account.
2. Send any message to the bot.
3. On a browser, login into the bot's gmail account and ensure chat
   is activated. Accept the invite from your actual account.
4. Back on your hangouts client, send the following message:
   `/bot iamspartacus`
5. The bot should reply with "configuring first admin" or a similar
   message.

# Additional Configuration

After the first successful run of the bot, it should generate a
  `config.json` somewhere in your user directory.

You should be able to find it in:
  `/<user>/.local/share/hangupsbot/`, where <user> is your
  operating system username.

You can edit this file and restart the bot to load any new configs.

For further information, please see the README file and wiki.

# Troubleshooting

* For console output when the bot is starting, errors messages always
  start in ALLCAPS e.g. "EXCEPTION in ..."
* Additional logs can be found in:
  `/<user>/.local/share/hangupsbot/hangupsbot.log` -
  note: this file is more useful for developers and may be quite verbose
* You can verify the location of your active `config.json` by sending
  the following command to the bot via hangouts: `/bot files` (with
  the **starter** plugin active)
