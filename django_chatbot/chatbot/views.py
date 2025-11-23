from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib import auth
from google import genai
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone

from django.contrib.auth.decorators import login_required
# Gemini
client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_openai(message):
    
    model_name = 'gemini-2.5-flash' 
    
    response = client.models.generate_content(
        model=model_name,
        contents=message, 
    )
    answer = response.text
    return answer


# open ai api configuration 
# from openai import OpenAI # type: ignore
# client = OpenAI(api_key=settings.OPENAI_API_KEY)

# def ask_openai(message):
#     response = client.chat.completions.create(
#         model = "gpt-4.1",
#         messages=[
#             {"role": "system", "content": "You are an helpful assistant."},
#             {"role": "user", "content": message},
#         ]
#     )
    
#     answer = response.choices[0].message.content.strip()
#     return answer

# azure openai api configuration
# from openai import AzureOpenAI # type: ignore
# client = AzureOpenAI(
#         api_key=settings.AZURE_OPENAI_API_KEY,
#         azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
#         api_version=settings.AZURE_OPENAI_API_VERSION,
#     )
# def ask_openai(message):
    
#     response = client.chat.completions.create(
#         model=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
#         messages=[
#             {"role": "user", "content": message}
#         ]
#     )
#     answer = response.choices[0].message.content.strip()
#     return answer

@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')