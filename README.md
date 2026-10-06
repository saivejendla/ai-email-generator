# ✦ AI Email Generator

AI Email Studio is a Generative AI application that helps users create and improve professional emails using Google Gemini.

The application supports two main workflows:

- **Generate Email** — Create a new email from purpose, recipient, context, tone, length, and key points.
- **Rewrite Email** — Improve an existing email by making it more professional, friendly, formal, concise, clear, or grammatically correct.

The application is built with Python, Streamlit, and the Google Gemini API.

## 🚀 Live Demo

Try the deployed application here:

**[Open AI Email Generator](https://ai-email-generator-xjsyhcgo7gz3kvaaxrzrby.streamlit.app/
)**

---

## Features

### ✦ Generate Email

Generate personalized emails based on:

- Email purpose
- Recipient
- Context
- Key points
- Tone
- Desired length

Supported use cases include:

- Job applications
- Follow-up emails
- Thank-you emails
- Meeting requests
- Leave requests
- Client communication
- Networking emails
- Custom email purposes

### ✎ Rewrite Email

Paste an existing email and improve it using options such as:

- Make it Professional
- Make it Friendly
- Make it Formal
- Make it More Polite
- Make it Confident
- Shorten it
- Improve Clarity
- Fix Grammar

The rewrite workflow preserves the original meaning and instructs the AI not to invent new facts.

### Additional Features

- Structured prompt engineering
- Editable AI-generated drafts
- Copy-friendly email output
- User-friendly API error handling
- Gemini quota and service-unavailable handling
- Modern two-column Streamlit interface
- Secure API key management using environment variables

---

## Application Architecture

```text
                     AI Email Studio
                            │
               ┌────────────┴────────────┐
               │                         │
        Generate Email             Rewrite Email
               │                         │
       prompt_builder.py          rewrite_prompt.py
               │                         │
               └────────────┬────────────┘
                            │
                    email_generator.py
                            │
                      Google Gemini
                            │
                       AI Draft
                            │
                      Edit / Copy
```

---

## Project Structure

```text
ai-email-generator/
│
├── src/
│   ├── __init__.py
│   ├── email_generator.py
│   ├── prompt_builder.py
│   └── rewrite_prompt.py
│
├── tests/
│   ├── __init__.py
│   ├── test_prompt_builder.py
│   ├── test_email_generator.py
│   └── test_rewrite_prompt.py
│
├── .env.example
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

---

## Tech Stack

- **Python** — Core application logic
- **Streamlit** — Interactive web interface
- **Google Gemini** — Generative AI email creation and rewriting
- **google-genai** — Gemini Python SDK
- **python-dotenv** — Local environment variable management

---

## How It Works

### Generate Email

```text
User Input
    ↓
Prompt Builder
    ↓
Structured Prompt
    ↓
Gemini API
    ↓
Generated Email
    ↓
Editable AI Draft
```

### Rewrite Email

```text
Existing Email
    ↓
Rewrite Style
    ↓
Rewrite Prompt Builder
    ↓
Gemini API
    ↓
Improved Email
    ↓
Editable AI Draft
```

---

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd ai-email-generator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_actual_api_key
```

Do not commit the `.env` file to GitHub.

### 6. Run the application

```bash
python -m streamlit run app.py
```

---

## Environment Variables

The project uses:

```text
GEMINI_API_KEY
```

An example configuration is available in `.env.example`.

---

## Error Handling

The application handles common external API failures and displays user-friendly messages for situations such as:

- Gemini temporarily unavailable
- High API demand
- API quota or rate-limit errors
- Missing or invalid API configuration

This prevents raw API errors from being exposed directly in the user interface.

---

## Testing

The project includes tests for:

- Prompt construction
- Gemini email generation
- Rewrite prompt construction

Example:

```bash
python -m tests.test_prompt_builder
python -m tests.test_rewrite_prompt
```

The Gemini integration test requires a valid API key and available API quota.

---

## Security

API credentials are never hardcoded into the source code.

The following files/directories are excluded from Git:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## Future Improvements

Potential future enhancements include:

- Multiple LLM providers
- Email history
- Additional rewrite styles
- Email templates
- Direct email-provider integrations
- Advanced personalization

---

## Author

Built as part of an AI Engineering portfolio project focused on Generative AI application development.