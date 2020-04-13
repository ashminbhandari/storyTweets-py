# storyTweets-py

Automatically share your Twitter tweets to Instagram stories

## Installation

Create a new [Twitter developers](https://developer.twitter.com/en) project to gather keys/token information

Download and install [ChromeDriver](https://chromedriver.chromium.org/). 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the script requirements

```bash
pip install -r requirements.txt
```

Make sure that you have a config file [config.py] setup with the parameters as shown below

```python
config = {'screen_name': '', #Twitter screenname to register updates for
          'consumer_key': '', #Gather from Twitter Developers project
          'consumer_secret': '', 
          'access_token_key': '', 
          'access_token_secret': '', 
          'path_to_driver': '', #Path to ChromeDriver
          'save_path': '', #Path to save your screenshot to
          'listening_freq': 10} #Listening frequency 

```

## Usage
```bash
python3 listener.py
```
Log in to the [Instagram](http://www.instagram.com) window that pops up and save your user information/pass through other prompts.

Let the script listen for tweets in your terminal.

Start Tweeting. 🥴

✅ Tested on Mac OS.

Linux/Windows may require some tweaking.

## Contributing
Feel free to push the knowledge forward my friend.

## License
[MIT](https://choosealicense.com/licenses/mit/)
