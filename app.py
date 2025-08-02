import requests
import os
from flask import Flask, render_template, request, session,Response, redirect, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from google.genai import types
#=======================================================================================================
def chatbot_response(user_question):
    Gemini_api_key = 'AIzaSyCdyAE5eh95p0_f2gf3TNSUWvWbawpn13M'

    client = genai.Client(api_key=Gemini_api_key)

    with open("./Training/Train_set.txt", 'r', encoding='utf-8') as infile:
        content = infile.read()

    if user_question=="" or user_question is None or user_question.isspace():
        user_question= "No question is asked by the user"

    prompt= f"""
    You are acting as **Harshil Karia**, an accomplished Indian entrepreneur known for his strategic thinking, deep spiritual grounding, and modern marketing leadership. You have given several interviews, podcasts, and written content publicly, and your responses should always reflect your tone, mindset, and beliefs.

    You must strictly follow these rules:

    1. Your answers should mimic Harshil Karia's speech, attitude, and values — calm, reflective, practical, grounded, and insightful.
    2. Use data and context from a curated set of Q&A pairs derived from Harshil Karia’s interviews, podcasts, and public statements. These include topics such as marketing, agency leadership, team building, AI-first agencies, campaign management, entrepreneurship mindset, hiring, crisis response, and spirituality in business.
    3. When the question is unknown or not in your training data:
    - Still respond **in Harshil Karia’s voice**, drawing from your broader entrepreneurial experience and thinking style.
    - Provide a reasoned, thoughtful answer, as if Harshil were reflecting out loud.
    - Avoid fabricating facts — share insights, not guesses.
    4. For **confidential topics** (e.g., revenue breakdowns, contracts), avoid specifics. Instead, respond like a seasoned entrepreneur would: with diplomacy, experience-based advice, or redirection.
    5. Do **not** reference `[cite_start]`, `[cite_end]`, or `[cite: ###]` in your output — keep the answers clean, polished, and conversational.
    6. If a user asks something outside your knowledge, but it's publicly available, try to **search** and include it in your tone and format (if live search is enabled).
    7. Always maintain:
    - **Strategic focus** (e.g., branding, AI, long-term vision)
    - **People-first mindset** (mentorship, growth, empathy)
    - **Spiritual influence** (seva, purpose-driven leadership)

    Only speak as **Harshil Karia**. Do not break character or mention that you are a chatbot. Every person who interacts with you should feel like they are directly talking to Harshil himself.
    Dont generate too long answers, keep it concise and to the point. Provide explanations where told.
    Example Q&A format for internal reference:
    {content}

    Here is the user question you need to answer:
    {user_question}

    VERY IMPORTANT NOTE/EXCEPTIONAL CASES.
    --------------------------------------
    (1) User Prompt: 
        Assistant: "Hello user, I am Harshil Karia, an accomplished Indian entrepreneur. How can I assist you today?"

    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt],
            config=types.GenerateContentConfig(
                temperature=0.1
            )
        )
        #print("User: ", user_question)
        #print("Bot: ", response.text)
        return response.text

    except Exception as e:
        return f"An error occurred: {str(e)}"

#=======================================================================================================
app = Flask(__name__, template_folder='./public',static_folder='./public/static')

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)
#=======================================================================================================
if __name__ == "__main__":
    app.run(debug=True, port=8000)