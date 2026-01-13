from django.test import TestCase, Client
from django.urls import reverse
from .models import ChatMessage
from unittest.mock import patch

class ChatbotTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_chatbot_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chatbot_home.html')

    @patch('geminichatbot.views.OpenAI')
    def test_chatbot_view_post(self, MockOpenAI):
        # Mock the OpenRouter API response
        mock_client = MockOpenAI.return_value
        mock_completion = mock_client.chat.completions.create.return_value
        mock_completion.choices = [type('obj', (object,), {'message': type('obj', (object,), {'content': 'I am a bot.'})})]
        
        response = self.client.post(self.url, {'message': 'Hello'})
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ChatMessage.objects.count(), 2) # User message + Bot message
        self.assertEqual(ChatMessage.objects.first().message, 'Hello')
        self.assertEqual(ChatMessage.objects.last().message, 'I am a bot.')
