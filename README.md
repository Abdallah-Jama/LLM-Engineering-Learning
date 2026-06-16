# LLM Engineering — Day 1: Web Page Summarizer

My daily practice following **Edward Donner's LLM Engineering course**.
Day 1 builds a command-line tool that scrapes a website and produces a concise,
bullet-point summary using the OpenAI API.

## What it does

1. Scrapes a web page (title + visible text, truncated to 2,000 characters).
2. Sends the content to an OpenAI chat model with a system prompt that asks for
   a short, professional, bullet-point summary.
3. Prints the summary to the terminal — including any news or announcements.

## Project structure

| File | Purpose |
| --- | --- |
| `day1_page_summarizer.py` | Main script — loads the API key, builds the prompt, calls OpenAI, prints the summary. |
| `scraper.py` | Helper that fetches and cleans web page content with `requests` + BeautifulSoup. |
| `requirements.txt` | Python dependencies. |
| `.env` | Holds your `OPENAI_API_KEY` (not committed — git-ignored). |

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your OpenAI API key** — create a `.env` file in the project root:

   ```
   OPENAI_API_KEY=sk-proj-your-key-here
   ```

   The script validates that the key exists, starts with `sk-proj-`, and has no
   stray whitespace.

## Usage

```bash
# Summarize any website
python day1_page_summarizer.py https://example.com

# Run with no argument to use the default URL
python day1_page_summarizer.py
```

## How it works

- `scraper.fetch_website_contents(url)` downloads the page, strips out
  `script`, `style`, `img`, and `input` tags, and returns the title plus the
  cleaned text.
- `summarize(url)` wraps that content in a system + user prompt and calls
  `gpt-4.1-mini` via the OpenAI Chat Completions API.
- `display_summary(url)` prints the result.

## Running in Jupyter Notebook or Google Colab

This script is written for the command line and prints plain text. If you'd
rather run it in a **Jupyter Notebook** or **Google Colab**, you can render the
summary as nicely formatted Markdown instead. Install IPython and add these
imports:

```bash
pip install ipython
```

```python
from IPython.display import Markdown, display
```

Then display the summary as Markdown instead of printing it:

```python
def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))
```

These imports are **only** needed in a notebook environment — the standard
command-line script does not require them.

## Notes

- Page content is capped at 2,000 characters to keep requests small and cheap.
- The model is set to `gpt-4.1-mini`; change it in `summarize()` if you want a
  different model.
