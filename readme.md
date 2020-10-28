<p align=center>

  <img height="128px" src="https://user-images.githubusercontent.com/45269106/97458816-5f71f200-193b-11eb-9014-b6f911c24d81.png"/>

  <br>
  <span>Sokobot is a Discord bot written with <a href="https://github.com/Rapptz/discord.py">discord.py</a> that lets you play <a href="https://en.wikipedia.org/wiki/Sokoban">Sokoban</a>, the classic box-pushing puzzle game.</span>
  <br>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
  <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/github/license/commander07/sokobot"></a>
  <a target="_blank" href="https://twitter.com/intent/tweet?text=Sokobot%20is%20a%20Discord%20bot%20written%20with%20discord.py%20that%20lets%20you%20play%20Sokoban,%20the%20classic%20box-pushing%20puzzle%20game.%20&url=https://github.com/Commander07/Sokobot&hashtags=discord" title="Share on Twitter"><img src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FCommander07%2FSokobot"></a>
  <a target="_blank" href="https://sokobot.cf"><img alt="Website" src="https://img.shields.io/website?down_color=red&down_message=DOWN&style=flate&up_color=green&up_message=UP&url=https%3A%2F%2Fsokobot.cf"></a>
  <a target="_blank"><img alt="Version" src="https://img.shields.io/badge/dynamic/json?color=green&label=version&prefix=v&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FCommander07%2FSokobot%2Fmain%2Fdata%2Fvalues.json"></a>
  <a target="_blank" href=""><img alt="Uptime" src="https://img.shields.io/uptimerobot/ratio/m786241270-00f6d056a098b2de3035d425"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contributing">Contributing</a>
</p>

## Installation

### Windows

```console
# clone the repo
$ git clone https://github.com/Commander07/sokobot.git

# change the working directory to sokobot
$ cd sokobot

# create and activate python environment
$ python3 -m venv bot-env
$ bot-env\Scripts\activate.bat

# install the requirements
$ python3 -m pip install -r requirements.txt
```

### Linux

```console
# clone the repo
$ git clone https://github.com/Commander07/sokobot.git

# change the working directory to sokobot
$ cd sokobot

# create and activate python environment
$ python3 -m venv bot-env
$ source bot-env/bin/activate

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

### Windows

```console
# create a .env file and add your bot token as the variable TOKEN
$ notepad .env

# start bot
$ python bot.py
```

### Linux

```console
# create a .env file and add your bot token as the variable TOKEN
$ nano .env

# start bot
$ python bot.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Feel free to create a fork and use the code.