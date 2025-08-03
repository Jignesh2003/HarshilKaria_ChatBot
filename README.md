# 🧠 Harshil Karia AI ChatBot

A personalized AI chatbot that simulates the communication style, personality, and decision-making patterns of **Harshil Karia** — Founder of Schbang and a visionary in digital branding.

Built using **Flask for backend** and **HTML/CSS/JavaScript for frontend**, this chatbot mimics Harshil’s tone and knowledge based on real-world data scraped from public platforms like YouTube and Instagram.

---

## 🎯 Project Goal

> Create a functional AI chatbot that authentically replicates Harshil Karia's thought patterns and communication style, capable of providing brand advice, startup insights, and motivational content in his voice.

---

## 🧰 Tech Stack

| Layer         | Tools Used                          |
|-------------- |-------------------------------------|
| Backend       | Flask (Python)                      |
| Frontend      | HTML, CSS, JavaScript               |
| AI Model      | Gemini API (prompt-based behavior)  |
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
