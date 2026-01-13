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
