import requests
import os
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from google.genai import types

YOUTUBE_API_KEY= '<your-api-key>'
Gemini_api_key = '<your-api-key>'

#=======================================================================================================

#Fetching top 10 videos of the searched person from YouTube
def get_YT_videos(noOfVideos, SearchKeyword, YT_API_KEY):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
                'key' : YT_API_KEY,
                'q' : SearchKeyword,
                'part' : 'snippet',
                'maxResults' : noOfVideos,
                'type' : 'video'
            }

    r = requests.get(search_url, params=search_params)
    if r.status_code == 200:
        search_results = r.json()['items']
        #print(search_results)
        video_ids = []
        for result in search_results:
            video_ids.append(result['id']['videoId'])
        print(video_ids)
        return video_ids
    else:
        print("Error fetching video IDs")
        return []
#=======================================================================================================

#Generating Transcript based on video IDS
def generate_transcripts(video_ids):
    ytt_api = YouTubeTranscriptApi()

    for video_id in video_ids:
        try:
            fetched_transcript = ytt_api.fetch(video_id)
            # Storing the transcript in a text file
            with open(f"{video_id}_transcript.txt", "w", encoding="utf-8") as file:
                for entry in fetched_transcript:
                    file.write(f"{entry.text} ")
        except Exception as e:
            print(f"Error fetching transcript for video ID {video_id}: {e}")
            continue
#=======================================================================================================

# Sumarizing the transcript using Gemini API
def GenerateYtSummary(content):
    client = genai.Client(api_key=Gemini_api_key)
    prompt= f""" You are Youtube video summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points within 250 words. The transcript text will be appended here: 
    {content}
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt],
            config=types.GenerateContentConfig(
                temperature=0.1
            )
        )
        return response.text 

    except Exception as e:
        print(f"API error: {e}")
        return None

#=======================================================================================================

#=======================================================================================================
# Main function to execute the script
def main():
    noOfVideos=10
    SearchKeyword = "Harshil Karia"
    video_ids = get_YT_videos(noOfVideos, SearchKeyword, YOUTUBE_API_KEY)
    if video_ids:
        generate_transcripts(video_ids) #Generating transcripts for the fetched video IDs

        

        input_folder = "./Transcripts" #Folder containing the original transcripts
        output_folder = "./Summaries" #Folder to save the summarized transcripts
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(input_folder):
            if filename.endswith(".txt"):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)

                with open(input_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    processed_content = GenerateYtSummary(content)

                with open(output_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(processed_content)
        print("✅ All .txt files processed and saved.")
    else:
        print("No video IDs found to generate transcripts.")

