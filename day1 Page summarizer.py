# imports

import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI


# Load enviroment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")


# check the key

if not api_key:
    print(
        "No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!"
    )
elif not api_key.startswith("sk-proj-"):
    print(
        "An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook"
    )
elif api_key.strip() != api_key:
    print(
        "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook"
    )
else:
    print("API key found and looks good so far!")


openai = OpenAI()

system_prompt = """
You are Professional and concise assistant that analyzes the content of a website and extract only the most important information, in a Bullet points format only.
"""

# Define our user prompt

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
"""


def message_for(website):
    return [
        {"role": "system", "content": system_prompt},{"role": "user", "content": user_prompt_prefix + website}
    ]


# And now: call the OpenAI API.

def summarize(url):
    website = fetch_website_contents(url)
    response = openai.chat.completions.create(
        model="gpt-4.1-mini", 
        messages=message_for(website)
    )

    return response.choices[0].message.content

def display_summary(url):
    summary = summarize(url)
    print(summary)

# display_summary("https://edwarddonner.com")
display_summary("https://dahabshiil.com")


# You can try it by runing: display_summary("website_url_here")
