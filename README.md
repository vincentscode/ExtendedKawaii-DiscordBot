# ExtendedKawaii-DiscordBot
A drop in replacement for the popular KawaiiBot<br>
[Invite](https://discordapp.com/oauth2/authorize?client_id=665549589394227220&response_type=code&scope=bot)

# Self hosting
Add a `config.py` file in this format:
```python
# config
prefix = '+'
admin_ids = [] # discord user ids => admins (can allow custom commands)

# discord api
token = '<your_discord_token>'

# gif apis
tenor_key = '<your_tenor_api_key>'
giphy_key = '<your_giphy_api_key>'

# reddit
reddit_headers = {
	# request headers for reddit (required for +reddit)
	# can be acquired using by copying a curl to reddit and pasting it into https://curl.trillworks.com/
}

# developer settings
test_mode = False
dev_mode = False
```
