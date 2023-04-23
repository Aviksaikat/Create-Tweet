import toml
import tweepy
import argparse

# Load keys from keys.toml file
with open("keys.toml") as f:
	keys = toml.load(f)

# Access individual keys
api_key = keys["API_KEYS"]["api_key"]
api_key_secret = keys["API_KEYS"]["api_key_secret"]
access_token = keys["API_KEYS"]["access_token"]
access_token_secret = keys["API_KEYS"]["access_token_secret"]

def post_on_twitter(tweet, image):
	# Use the keys in your Tweepy code
	auth = tweepy.OAuthHandler(api_key, api_key_secret)
	auth.set_access_token(access_token, access_token_secret)

	# Create API object
	api = tweepy.API(auth, wait_on_rate_limit=True)

	# Upload image
	media = api.media_upload(image)

	# Create a tweet
	post_result = api.update_status(status=tweet, media_ids=[media.media_id])

	print("Tweet posted successfully.")

def main():
	# Create argument parser
	parser = argparse.ArgumentParser(description="Post a tweet on Twitter with content and image")
	parser.add_argument("-m", "--message", type=str, help="Tweet content")
	parser.add_argument("-i", "--image", type=str, help="Image path")

	# Parse command line arguments
	args = parser.parse_args()

	# Check if message and image arguments are provided
	if args.message and args.image:
		# Call the function to post on Twitter
		post_on_twitter(args.message, args.image)
	else:
		print("Please provide both tweet content and image path using -m and -i arguments respectively.")


if __name__ == "__main__":
	main()