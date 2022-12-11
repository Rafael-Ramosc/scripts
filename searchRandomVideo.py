from googleapiclient.discovery import build

# Set the API key
api_key = "AIzaSyAnKrehn6flBqaCfOTFpu6gu40mBsKJ7F8"

# Build the YouTube API service
service = build("youtube", "v3", developerKey=api_key)

# Search for videos
results = service.search().list(
  part="id,snippet",
  type="video",
  q="",
  maxResults=10).execute()

# Print the results
for result in results["items"]:
  print(result["snippet"]["title"])

  import random

# Choose a random video from the results
random_video = random.choice(results["items"])

# Print the video title
print(random_video["snippet"]["title"])

# Open the video in the default web browser
import webbrowser
webbrowser.open(f"https://www.youtube.com/watch?v={random_video['id']['videoId']}")