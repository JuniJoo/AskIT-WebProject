from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Question, Module, Answer, UserProfile
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_question_list(request, mod):
    module = Module.objects.get(title=mod)
    questions = Question.objects.filter(module=module)
    question_array = []
    for question in questions:
        context = {'id': question.id,
                   'title': question.title,
                   'author': getattr(question.author, 'username', None),
                   'pub_date': question.pub_date,
                   'tags': []
                   }
        for tag_name in question.tags.all():
            context['tags'].append(str(tag_name))
        context['score'] = question.score
        context['views'] = question.views
        context['num_answers'] = Answer.objects.filter(question=question).count()
        question_array.append(context)

    return JsonResponse(question_array, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_popular_questions(request, mod, days):
    module = Module.objects.get(title=mod)
    questions = Question.objects.filter(module=module)
    question_array = []
    for index ,question in enumerate(questions):
        context = {'id': question.id,
                   'title': question.title,
                   'author': getattr(question.author, 'username', None),
                   'pub_date': question.pub_date,
                   'tags': []
                   }
        for tag_name in question.tags.all():
            context['tags'].append(str(tag_name))
        context['score'] = question.score
        context['views'] = question.views
        context['num_answers'] = Answer.objects.filter(question=question).count()
        question_array.append(context)
        if(index == 3):
            break

    return JsonResponse(question_array, safe=False)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_module_list(request):
    modules = Module.objects.all()
    module_array = []
    for module in modules:
        context = {'id': module.id,
                   'title': module.title,
                   'description': module.description,
                   }
        module_array.append(context)

    return JsonResponse(module_array, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def is_admin(request,mod):
    the_module = Module.objects.get(title=mod)
    if request.user in the_module.admins.all(): 
        return JsonResponse({'admin': True } )
    else:
        return JsonResponse({'admin': False } )
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_users(request,mod):
    users = User.objects.all()
    the_module = Module.objects.get(title=mod)
    user_array = []
    for user in users:
        print(user)
        userProfile = UserProfile.objects.get(user = user)
        admin = user in the_module.admins.all()
        member = user in the_module.members.all() 
        data = {'email': user.username,
                'first_name': userProfile.first_name,
                'last_name': userProfile.last_name,
                'admin': admin,
                'member': member,
        }
        user_array.append(data)
    return JsonResponse(user_array, safe=False)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def update_roles(request, mod):
    if request.method == 'POST':
        print(request.body)
        post_data_array = json.loads(request.body)
        for post_data in post_data_array:
            username = post_data['email']
            member = post_data['member']
            admin = post_data['admin']
            module = Module.objects.get(title=mod)
            user = User.objects.get(username = username)
            if member:
                module.members.add(user)
            else:
                module.members.remove(user)
            if admin:
                module.admins.add(user)
            else:
                module.admins.remove(user)
        module.save()
        return JsonResponse({"success": True})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def update_members(request, mod):
    success = 0
    fail = 0
    if request.method == 'POST':
        print(request.body)
        post_data_array = json.loads(request.body)
        module = Module.objects.get(title=mod)
        for post_data in post_data_array:
            try:
                user = User.objects.get(username = post_data)
                module.members.add(user) 
                success += 1
            except:
                print('no user')
                fail += 1
        module.save()
        return JsonResponse({"success": success,"fail":fail})
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def remove_members(request, mod):
    success = 0
    fail = 0
    if request.method == 'POST':
        print(request.body)
        post_data_array = json.loads(request.body)
        module = Module.objects.get(title=mod)
        for post_data in post_data_array:
            try:
                user = User.objects.get(username = post_data)
                module.members.remove(user) 
                success += 1
            except:
                print('no user')
                fail += 1
        module.save()
        return JsonResponse({"success": success,"fail":fail})
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def update_admins(request, mod):
    success = 0
    fail = 0
    if request.method == 'POST':
        print(request.body)
        post_data_array = json.loads(request.body)
        module = Module.objects.get(title=mod)
        for post_data in post_data_array:
            try:
                user = User.objects.get(username = post_data)
                module.admins.add(user) 
                success += 1
            except:
                print('no user')
                fail += 1
        module.save()
        return JsonResponse({"success": success,"fail":fail})
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def remove_admins(request, mod):
    success = 0
    fail = 0
    if request.method == 'POST':
        print(request.body)
        post_data_array = json.loads(request.body)
        module = Module.objects.get(title=mod)
        for post_data in post_data_array:
            try:
                user = User.objects.get(username = post_data)
                module.admins.remove(user) 
                success += 1
            except:
                print('no user')
                fail += 1
        module.save()
        return JsonResponse({"success": success,"fail":fail})