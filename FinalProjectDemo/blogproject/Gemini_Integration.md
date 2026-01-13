# Gemini Chatbot Integration Guide

This document details the steps performed to integrate the Gemini Chatbot into the `Blog-Project` using OpenRouter.

## 1. App Initialization
- Created a new Django app named `geminichatbot`.
  ```bash
  python manage.py startapp geminichatbot
  ```

## 2. Configuration
### `settings.py`
- Registered the new app in `INSTALLED_APPS`.
- Added the `OPENROUTER_API_KEY` setting.
  ```python
  INSTALLED_APPS = [
      # ...
      'geminichatbot',
  ]

  OPENROUTER_API_KEY = 'sk-or-v1-...' # Your OpenRouter API Key
  ```

## 3. Database Model
### `geminichatbot/models.py`
- Defined a `ChatMessage` model to store user and bot interactions.
  ```python
  class ChatMessage(models.Model):
      user = models.CharField(max_length=300)
      message = models.TextField()
      timestamp = models.DateTimeField(auto_now_add=True)
  ```

## 4. Backend Logic
### `geminichatbot/views.py`
- Implemented the `index` view to handle chat logic.
- Used the `openai` library to interact with the OpenRouter API (accessing Gemini models).

```python
from openai import OpenAI
from django.shortcuts import render
from django.conf import settings
from .models import ChatMessage

def index(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            # Save user message
            ChatMessage.objects.create(user='User', message=user_message)
            
            # Configure OpenRouter
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=settings.OPENROUTER_API_KEY,
            )
            
            try:
                # Get response from OpenRouter
                completion = client.chat.completions.create(
                    model="google/gemini-2.0-flash-exp:free", # Using free tier model as default
                    messages=[
                        {"role": "user", "content": user_message}
                    ]
                )
                bot_message = completion.choices[0].message.content
                
                # Save bot message
                ChatMessage.objects.create(user='Gemini', message=bot_message)
            except Exception as e:
                ChatMessage.objects.create(user='System', message=f"Error: {str(e)}")
                
    messages = ChatMessage.objects.all().order_by('timestamp')
    return render(request, 'chatbot_home.html', {'messages': messages})
```

## 5. URL Routing
### `geminichatbot/urls.py`
- Defined the URL pattern for the chatbot view.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### `blogproject/urls.py`
- Included the `geminichatbot` URLs in the main project configuration.
  ```python
  path('geminichatbot/', include('geminichatbot.urls')),
  ```

## 6. Frontend Interface
### `templates/chatbot_home.html`
- Created a template to display the chat history and a form for sending new messages.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gemini Chatbot</title>
</head>

<body>
    <h1>Gemini Chatbot</h1>

    <div id="chat-box">
        {% for message in messages %}
        <div class="message">
            <strong>{{ message.user }}:</strong> {{ message.message }}
            <small>{{ message.timestamp }}</small>
        </div>
        {% endfor %}
    </div>

    <form method="post">
        {% csrf_token %}
        <input type="text" name="message" placeholder="Type your message..." required>
        <button type="submit">Send</button>
    </form>
</body>

</html>
```

## 7. Dependencies
- Installed the `openai` library to communicate with OpenRouter.
  ```bash
  pip install openai
  ```

## 8. Database Setup
- Created and applied migrations to set up the database table for `ChatMessage`.
  ```bash
  python manage.py makemigrations geminichatbot
  python manage.py migrate
  ```

## 9. Verification
- Implemented automated tests in `geminichatbot/tests.py` to verify the view and API integration (using mocks).
- Verified functionality by running the server and interacting with the chatbot at `/geminichatbot/`.

## Usage
1. Ensure the virtual environment is activated.
2. Run the server: `python manage.py runserver`.
3. Navigate to `http://127.0.0.1:8000/geminichatbot/`.
