from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from google import genai

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
# from openai import OpenAI
# client = OpenAI(api_key=settings.OPENAI_API_KEY)

# def ask_openai(message):
#     response  =client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "user", "content": message}
#         ]
#     )
#     answer=response.choices[0].message.content.strip()
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


def chatbot(request):
    if request.method =='POST':
        message=request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message':message, 'response':response})
    return render(request,'chatbot.html',)





