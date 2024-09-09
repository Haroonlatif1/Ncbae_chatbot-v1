
from .models import UserFeedback
import json
from django.http import JsonResponse
from django.conf import settings
from llamaapi import LlamaAPI
from django.shortcuts import render

# ... (rest of the code remains the same)
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MessageSerializer
from .models import UserFeedback
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MessageSerializer
from .models import UserFeedback

class CreateUserView(APIView):
    def get(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'})
        return Response({'error': 'Invalid data'}, status=400)

class GetUsersView(APIView):
    def get(self, request):
        users = UserFeedback.objects.all()
        serializer = MessageSerializer(users, many=True)
        return Response(serializer.data)

def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            user = UserFeedback.objects.get(pk=user_id)
            user.user_message = data.get('user_message', user.user_message)
            user.bot_response = data.get('bot_response', user.bot_response)
            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except UserFeedback.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'PUT request required'}, status=400)

def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = UserFeedback.objects.get(pk=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserFeedback.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'DELETE request required'}, status=400)

llama = LlamaAPI(settings.LLAMA_API_KEY)

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('prompt', '').strip().lower()

            # Check all hard-coded responses first
            response_text = handle_static_responses(prompt)
            if response_text:
                return JsonResponse({'response': response_text})

            # If no hard-coded response found, call LLaMA API
            try:
                llama_response = call_llama_llm(prompt)
                response_text = llama_response.get('choices', [{}])[0].get('message', {}).get('content', '') 
                if not response_text:
                    raise ValueError("Empty response from LLaMA API")
            except Exception as llama_error:
                print(f"LLaMA API error: {llama_error}")
                response_text = "Sorry, I couldn't find any information on that. "

            return JsonResponse({'response': response_text })

        except Exception as e:
            print(f"Error processing request: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'POST request required'}, status=400)

def call_llama_llm(prompt):
    api_request_json = {
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "stream": False,
    }

    response = llama.run(api_request_json)
    response_json = response.json()

    if response.status_code != 200:
        raise Exception(f"LLaMA API call failed with status code {response.status_code}")

    return response_json

def handle_static_responses(prompt):
    prompts = {
        "greetings": ["hi", "hello", "hey", "hello there", "hi there", "hey there", "hullo", "hullo there","hlo"],
        "salam":["AOA","Assalam o alikum","aoa","Aoa","salam"],
        "introductions": ["what's your name?", "who are you?", "what's your name again?", "what are you called?", "what's your moniker?"],
        "ncbae_info": ["what's ncbae?", "what is ncbae?", "what does ncbae stand for?", "what's ncbae all about?", "what's the purpose of ncbae?"],
        "timings": ["what's ncbae timings?", "Ncbae office timings","ncbae timings","whats ncbae timing","whats ncbae timings","whats ncbae timings?", "what are ncbae timings?", "what time does ncbae open?", "what time does ncbae close?", "what are ncbae's hours?"],
        "location": ["where is ncbae located?", "what's ncbae address?", "where can i find ncbae?", "what's the location of ncbae?"],
        "rank": ["what's ncbae rank?","what's rank of ncbae", "what's ncbae ranking?", "is ncbae a good university?", "how good is ncbae?", "what's ncbae's reputation?"],
        "health": ["how are you", "how r u", "how are u", "how's it going", "how's life", "how's everything", "how are you doing"],
        "thanks": ["thank you", "thanks", "appreciate it", "thanks a lot", "thanks so much"],
        "weather": ["what's the weather like?", "how's the weather?", "what's the weather?", "is it sunny?", "is it raining?"],
        "offeredcourses":["Which courses does ncbae offer","courses"],
        "courses":["Which courses does ncbae offer","courses"]
    }

    responses = {
        "greetings": "Hi there! How can I help you today?",
        "introductions": "I'm NCBAE chatbot!",
        "salam":"Walikum asalam",
        "ncbae_info": "NCBAE is a private institute which offers a variety of courses",
        "timings": "NCBAE timings are from 9am to 5pm",
        "location": "West canal Lahore near Muslim Town",
        "rank": "In top 300 universities of Pakistan",
        "health": "I'm just a chatbot, but I'm functioning as expected!",
        "thanks": "No problem dear!",
        "weather": "I can't check the weather right now, but it's usually nice somewhere.",
        "offeredcourses":"We offer many courses like ADP-CS, BS Accounting and finance ,BS management sciences, ADP-Finance and accounting and much more"
    }

    for category, prompts_list in prompts.items():
        if prompt.lower() in [p.lower() for p in prompts_list]:
            return responses[category]

    return ""
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')

            user = User.objects.create(username=username, email=email)
            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'POST request required'}, status=400)

def get_users(request):
    if request.method == 'GET':
        try:
            users = list(User.objects.values())  # Retrieve all users from database
            return JsonResponse(users, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'GET request required'}, status=400)