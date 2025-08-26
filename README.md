# 🧠 Harshil Karia AI ChatBot (Stateless chatbot)

A personalized AI chatbot that simulates the communication style, personality, and decision-making patterns of **Harshil Karia** — Founder of Schbang and a visionary in digital branding.

Built using **Flask for backend** and **HTML/CSS/JavaScript for frontend**, this chatbot mimics Harshil’s tone and knowledge based on real-world data scraped from public platforms like YouTube and Instagram.

NOTE: It is a stateless chatbot meaning it doesn't maintain the previous chat history i.e. no memory is of previous chat is stored. It only give response to the present input irrespective of maintaining the previous chats context.

build for learning purpose.
---

## 🎯 Project Goal

> Create a functional AI chatbot that authentically replicates Harshil Karia's thought patterns and communication style, capable of providing brand advice, startup insights, and motivational content in his voice.

---

## 🧰 Tech Stack

| Layer         | Tools Used                          |
|-------------- |-------------------------------------|
| Backend       | Flask (Python)                      |
| Frontend      | HTML, CSS, JavaScript               |
| API Used      | Gemini API, Youtube API             |
| Data Storage  | Cleaned JSON file (used in prompt)  |
| Hosting       | PythonAnyWhere, Github Pages        |

---
## 🧩 File Structure
<pre lang="markdown"> 
HarshilKaria_ChatBot/
├──app.py # flask app
├──ExtractingData.py # Extracting data from youtube and instagram profile of Harshil Karia for model training
├──Training/ # Folder containing clean txt file which contains json data
|  ├──Train_set.txt
├──Transcripts/ # Folder containng all the raw transcripts of Harshil Karia's podcast extracted from Youtube 
|  ├──3fs-d-LseLk_transcript.txt
|  ├──503C9CJVHSA_transcript.txt
|  ├──HF-jYlncpvg_transcript.txt
|  ├──i1BEE9VBVw0_transcript.txt
|  ├──lYTi3FGxDXk_transcript.txt
|  ├──NWhm98HuXRg_transcript.txt
|  ├──ugfwW7hqkH0_transcript.txt
|  ├──wGTc8E6gnno_transcript.txt
|  ├──yZtLEFlh758_transcript.txt
├──Captions/ # All the ras caption extracted from Harshil Karia's Instagram profile 
|  ├──caption.txt
├──public/ # contains html files 
|  ├──static/ # contains all the js & css files
|  |  ├──css/
|  |  | ├──style.css
|  |  ├──js/
|  |  |  ├──script.js
|  |  ├──index.html
├── requirements.txt # Python dependencies
└── README.md # Project documentation
</pre>
---
## 📚 How It Works

### 1. **Data Collection**
- **YouTube**: Extracted transcripts from top 10 interviews/podcasts
- **Instagram**: Scraped captions from 30 recent public posts

### 2. **Data Preprocessing**
- Cleaned and structured all raw text into a JSON format.
- Labeled examples to reflect topics, tone, and themes typical of Harshil’s content.

### 3. **Chatbot Behavior**
- Used **Gemini API** for real-time response generation.
- Model used in LLM is **gemini-2.5-flash**
- Included the JSON knowledge file as context in the prompt to instruct Gemini to:
  > "Act as Harshil Karia. Use the data below to respond authentically in his voice."

### 4. **Frontend UI**
- A simple web-based chat interface with:
  - Input box
  - Dynamic response window
  - Clean styling using basic CSS

---

## 💻 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Jignesh2003/HarshilKaria_ChatBot.git
cd HarshilKaria_ChatBot
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. Add your Gemini API key in app.py
```bash
GEMINI_API_KEY=your_api_key_here
```

## 4. Run the project
```bash
python app.py
```

## 5. Open the frontend
```bash
Visit: http://localhost:8000 in your browser.
```

## ✅ Features 
- Responds like Harshil Karia
- Handles brand strategy & startup-related prompts
- Conversational, empathetic, and actionable style
- Pulls context from cleaned real-life data
- Fast, responsive, and easy to use

## Results
<img width="1914" height="915" alt="image" src="https://github.com/user-attachments/assets/7870971b-189b-4bb7-bf07-4f4d5f3c15d7" />

# If you want to extract transcripts from youtube than refer below steps (ExtractingData.py)
## YouTube Transcript Summarizer Using Gemini API

This project allows you to scrape the top 10 YouTube videos related to a specific keyword (e.g., "Harshil Karia"), extract their transcripts, and summarize the transcripts using **Google Gemini API**. The summarized text is then stored in a separate folder for further use.

---

## 🛠️ Features

- Scrapes the top 10 YouTube videos based on a search keyword.
- Extracts video transcripts using the **YouTube Transcript API**.
- Summarizes the transcript using **Gemini API**.
- Saves the summarized content into a new folder.
---

## 🔧 Tech Stack

- **Python** (for scripting)
- **YouTube Transcript API** (for fetching video transcripts)
- **Google Gemini API** (for text summarization)
- **requests** (for making API requests)
---

## 🧰 Prerequisites

- Python 3.x
- YouTube Data API v3 key (`YOUTUBE_API_KEY`)
- Gemini API key (`Gemini_api_key`)

1. Install required libraries:
    ```bash
    pip install youtube-transcript-api
    ```
2. Replace the `YOUTUBE_API_KEY` and `Gemini_api_key` with your own API keys in the script.
---

## 📝 Script Overview

### 1. **Fetching Top YouTube Videos**
The script fetches the top 10 YouTube videos related to a search keyword (`Harshil Karia`) using the **YouTube Data API v3**. 

```python
def get_YT_videos(noOfVideos, SearchKeyword, YT_API_KEY):
```
This function returns a list of video IDs that are used in the subsequent transcript fetching step.

### 2. **Generating Transcripts**
The generate_transcripts function uses the YouTube Transcript API to extract the transcripts for the fetched video IDs and saves them as .txt files in the Transcripts folder.
```python
def generate_transcripts(video_ids):
```
### 3. **Summarizing Transcripts Using Gemini API**
The GenerateYtSummary function takes the transcript text and passes it to the Gemini API to generate a summary. The summarization is done within 250 words.
```python
def GenerateYtSummary(content):
```
---
## 🏃 How to Run

1. Set up your API keys:
  - Get a YouTube Data API key from the [Google Developers Console](https://console.cloud.google.com/apis/library?inv=1&invt=Ab4eaQ&project=playingsongsbasedonemotion).
  - Get a Gemini API key from the [Gemini AiStudio](https://aistudio.google.com/app/apikey).
2. Run the script:
```bash
python ExtractingData.py
```
This will:
  -Fetch top 10 videos related to "Harshil Karia".
  -Extract the transcripts.
  -Summarize the transcripts using Gemini API.
  -Save the summarized content in the Summaries folder.
