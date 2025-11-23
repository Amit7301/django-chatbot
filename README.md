# 💬 Django Gemini Chatbot

A full-stack, secure web application built with Django that provides an interactive chat interface powered by the Google Gemini API. This project demonstrates user authentication (Registration, Login, Logout) and persistent storage of conversation history.

## ✨ Features

* **Authentication:** Complete user management using Django's built-in `auth` system (Register, Login, Logout).
* **Secure Views:** Uses the `@login_required` decorator to protect the chat interface and ensure data privacy.
* **AI Integration:** Utilizes the **Google Gemini API** (`gemini-2.5-flash` by default) for fast, high-quality conversational responses.
* **Persistent Chat History:** Stores all user messages and AI responses in a database (`Chat` model).
* **Asynchronous Communication:** Uses JavaScript/AJAX to send messages and receive responses without a full page reload.

## 🚀 Getting Started

Follow these steps to get your project running locally.

### Prerequisites

* Python 3.10+
* A **Gemini API Key** (obtainable from Google AI Studio).

### 1. Setup Environment

Clone the repository and install the required Python packages:

```bash
# 1. Clone your repository (if starting new, otherwise skip)
# git clone <your-repo-url>
# cd django-chatbot

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/macOS
.\venv\Scripts\activate    # On Windows

# 3. Install dependencies
pip install django google-genai python-dotenv