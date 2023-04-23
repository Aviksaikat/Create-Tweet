# My Simple Twitter Bot 🚀

A Python script that posts tweets on Twitter with content and image using Tweepy API. 🐦📸

![](media/banner.jpg)

## 📋 Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- Tweepy library installed (pip install tweepy)
- Twitter API keys and access tokens (refer to Twitter Developer documentation: https://developer.twitter.com/en/docs/getting-started/getting-access-to-the-twitter-api)

## 💻 Usage

1. Clone the repository:
```sh
git clone https://github.com/Aviksaikat/Create-Tweet
```

2. Navigate to the project directory:
```sh
cd Create-Tweet
```

3. Install the dependecies
```sh
pip install -r requirements.txt
```
 
3. Create a keys.toml file in the project directory with your Twitter API keys and access tokens:
```toml
[API_KEYS]
api_key = "your_api_key"
api_key_secret = "your_api_key_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
```

4. Run the script with tweet content and image path:
```sh
python3 tweet.py -m "Hello world! #TwitterBot" -i "images/my_image.png"
```

5. Sit back and enjoy your bot posting tweets with content and image on Twitter! 🎉🚀

# Example


https://user-images.githubusercontent.com/31238298/233862652-11bcb9f6-a800-4a67-997f-9caf828fa732.mp4



# 🤝 Contributing 
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality of this awesome Twitter bot. 💪


# License
This project is licensed under the MIT License.
