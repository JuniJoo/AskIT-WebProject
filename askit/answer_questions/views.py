import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Question, Answer, Tag, Module, Comment, Notification
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


def check_upvote_or_downvote_question(question, user):
    print(question.upvotes.filter(id=user.id))
    if question.upvotes.filter(id=user.id).exists():
        return "upvote"
    elif question.downvotes.filter(id=user.id).exists():
        return "downvote"
    else:
        return "none"


def check_upvote_or_downvote_answer(answer, user):
    if answer.upvotes.filter(id=user.id).exists():
        return "upvote"
    elif answer.downvotes.filter(id=user.id).exists():
        return "downvote"
    else:
        return "none"


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_question(request, question_id):
    context = {}
    try:
        question = Question.objects.get(id=question_id)
        question.views += 1
        question.save()
        context['question_id'] = question.id
        context['title'] = question.title
        context['author'] = getattr(question.author, 'username', 'Anonymous')
        context['module'] = question.module.title
        context['explanation'] = question.explanation
        context['tried_what'] = question.tried_what
        context['summary'] = question.summary
        context['pub_date'] = question.pub_date
        context['status'] = question.status
        context['tags'] = []
        for x in question.tags.all():
            context['tags'].append(str(x))
        context['score'] = question.score
        context['views'] = question.views
        context['upvote_or_downvote'] = check_upvote_or_downvote_question(question, request.user)

        Comment_query_result = Comment.objects.filter(question=question)
        context['comment_list'] = []
        for comment in Comment_query_result:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['author'] = getattr(comment.author, 'username', 'Anonymous')
            comment_dict['content'] = comment.content
            comment_dict['pub_date'] = comment.pub_date
            context['comment_list'].append(comment_dict)

        answer_query_result = Answer.objects.filter(question=question)
        context['answer_list'] = []
        for answer in answer_query_result:
            answer_dict = {}
            answer_dict['id'] = answer.id
            answer_dict['author'] = getattr(answer.author, 'username', 'Anonymous')
            answer_dict['content'] = answer.content
            answer_dict['pub_date'] = answer.pub_date
            answer_dict['score'] = answer.score
            answer_dict['is_solution'] = answer.is_solution
            answer_dict['upvote_or_downvote'] = check_upvote_or_downvote_answer(answer, request.user)
            context['answer_list'].append(answer_dict)
    except Question.DoesNotExist:
        context['question_id'] = context['title'] = context['author'] = context['module'] = context['explanation'] = \
            context['tried_what'] = context['summary'] = context['pub_date'] = context['status'] = context['score'] = \
            context['views'] = context['upvote_or_downvote'] = "Question does not exist"
    return JsonResponse(context)


def set_up_test_database(request):
    Module.objects.all().delete()
    Question.objects.all().delete()
    Tag.objects.all().delete()
    Answer.objects.all().delete()

    ossp = Module(id=1, title="OSSP",
                  description="An Operating System is the system software that manages computer hardware, hardware and software resources and provides common services for user programs. System programming is the type of programming necessary to produce software, such as operating systems, that deal with hardware, provide services to other software or manage performance constraints. This module teaches the technology of operating systems and introduces students to the challenges of systems-level programming .Also, this module gives practical insight into modern operating system topics. ")
    ossp.save()
    tp = Module(id=2, title="TP",
                description="This module teahes about team project, which is a capstone project for the students to apply the knowledge they have learned in the past 3 years. ")
    tp.save()
    sn = Module(id=3, title="SN",
                description="This moduel teaches about security and networking. It covers the basic concepts of computer security and networking. It also covers the design and implementation of secure systems and networks. ")
    sn.save()
    ossp_q1 = Question(module=ossp, title="Test file not working for part 1",
                       explanation="Hi, I have noticed that the test file doesn't work for part 1, it seems to want addnode to return the root of the tree, which is not what was done for assignment 1(if i remembering correctly) or what is given to us in the bst.c model answer for this assignment. should I assume that test_bst.c is incorrect and modify it to start the root before the 10k loop and run the loop without it overwriting the root variable or should I modify the model answer bst.c to return the root node and not the newly added node",
                       tried_what="I have tried to modify the test_bst.c file to start the root before the 10k loop and run the loop without it overwriting the root variable, but it still doesn't work. ",
                       summary="The test file doesn't work for part 1, it seems to want addnode to return the root of the tree, which is not what was done for assignment 1(if i remembering correctly) or what is given to us in the bst.c model answer for this assignment. ")
    ossp_q1.save()
    ossp_q1_a1 = Answer(question=ossp_q1,
                        content="I think the test file is correct, you should modify the model answer bst.c to return the root node and not the newly added node")
    ossp_q1_a1.save()
    ossp_q1_a2 = Answer(question=ossp_q1,
                        content="The code for the binary search tree actually needs to be slightly different for assignment 2 than the requirements for assignment 1. The difference is that addNode needs to return the root rather than the node which it adds. So whether you're using your own answer to assignment 1 or the model answer to assignment 1 as the code for the binary search tree in assignment 2, you need to change it so that addNode returns the root instead of the leaf. I'm sorry that this wasn't made clear. There will be a canvas announcement later today clarifying this and some other things.")
    ossp_q1_a2.save()
    ossp_q2 = Question(module=ossp, title="What is a process in an operating system?",
                       explanation="I am new to operating systems and system programming, and I keep hearing about processes. What exactly is a process in an operating system? How is it different from a program or a thread?",
                       tried_what="", summary="What is a process in an operating system?")
    ossp_q2.save()
    ossp_q2_a1 = Answer(question=ossp_q2,
                        content="A process is an instance of a program that is currently running on the operating system. It consists of the program code, data, and a set of resources that are allocated to it, such as memory, CPU time, and input/output devices. A process is different from a program in that a program is a static entity that resides on disk, while a process is a dynamic entity that is created by the operating system when a program is executed. A process can have one or more threads, which are independent paths of execution within the process.")
    ossp_q2_a1.save()
    ossp_q2_a2 = Answer(question=ossp_q2,
                        content="In operating systems, a process is an executing instance of a program. A process is comprised of an executable program, associated data, and system resources such as memory and CPU time. Processes are managed by the operating system's kernel, which is responsible for allocating resources to them, scheduling their execution, and providing interprocess communication mechanisms. A thread, on the other hand, is a lightweight process that shares the same resources as its parent process but executes independently.")
    ossp_q2_a2.save()
    tp_q1 = Question(id=1, module=tp, title="How to start the project?",
                     explanation="I am new to team project, and I don't know how to start the project. Can anyone give me some advice?",
                     tried_what="", summary="How to start the project?")
    tp_q1.save()
    tp_q1_a1 = Answer(question=tp_q1,
                      content="You can start by reading the project description carefully and understanding the requirements. Then you can start to think about how to implement the project. You can also discuss with your team members about the project.")
    tp_q1_a1.save()
    tp_q1 = Question(id=2, module=tp,
                     title="The marking criteria for the GDPR policy says we need to state where our servers are located - where are the University provided VPS's located?",
                     explanation="", tried_what="", summary="Where are the University provided VPS's located?")
    tp_q1.save()

    tp_q2 = Question(id=3, module=tp,
                     title="How can I access a postgres database during development? My axios requests on the frontend are returning empty and I think its because.",
                     explanation="", tried_what="", summary="Accessing a postgres database during development")
    tp_q2.save()

    tp_q2_a1 = Answer(question=tp_q2,
                      content="Can you instead use a terminal, connect to the VM (with ssh) and log to postgres on it? It might less easy to use than an intelliJ tool, but at least we can avoid restrictions")
    tp_q2_a1.save()

    tp_q3 = Question(id=4, module=tp,
                     title="I added some dependencies to the angular.json file but when I tried to push the changes",
                     explanation=", the pipeline failed at the package stage. How can I solve this issue?",
                     tried_what="", summary="Angular dependency issue")
    tp_q3.save()

    tp_q3_a1 = Answer(question=tp_q3, content="Which dependencies have you added?")
    tp_q3_a1.save()

    tp_q4 = Question(id=5, module=tp,
                     title="Hello, we are Team DAI 57 and are currently facing an issue with our git repository. ",
                     explanation="A commit was made that had some errors and when other team members clone the repository, we all get errors related to it, we have tried going back to a previous commit and pushing that to be the recent one and have attempted all possible options but it is not working for us. We have communicated this concern with both Professor Panos and Niloofer and we were recommended to ask if it’s possible we can have our repository reset please.",
                     tried_what="", summary="Git repository issue")
    tp_q4.save()

    tp_q4_a1 = Answer(question=tp_q4,
                      content="Normally this is an issue that can be fixed by reverting the commit. from what I can see the issue is a compilation error - if you can resolve that on your local development environment, then you should be able to get it working again. Also, please consider carefully if this is a good reason to move tech stack days before the MVP deadline. remember - don't commit broken code!")
    tp_q4_a1.save()
    t = Tag(tag_name="java")
    t.save()
    t2 = Tag(tag_name="python")
    t2.save()
    t3 = Tag(tag_name="c")
    t3.save()
    t4 = Tag(tag_name="c++")
    t4.save()
    t5 = Tag(tag_name="javascript")
    t5.save()
    ossp_q1.tags.add(t)
    ossp_q1.tags.add(t2)
    ossp_q2.tags.add(t)
    ossp_q2.tags.add(t2)
    tp_q1.tags.add(t3)
    tp_q1.tags.add(t4)
    tp_q2.tags.add(t3)
    tp_q2.tags.add(t4)
    tp_q3.tags.add(t5)
    tp_q4.tags.add(t5)
    ossp_q1.save()
    ossp_q2.save()
    tp_q1.save()
    tp_q2.save()
    tp_q3.save()
    tp_q4.save()
    return HttpResponse("The database has been reset, visit https://teamai55-22.bham.team to go back to the home page")


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def submit_answer(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        post_data = json.loads(request.body)
        content = post_data['content']
        author = request.user
        answer = Answer(question=question, content=content, author=author)
        answer.save()
        notification = Notification(receiver=question.author,
                                    detail=f"{author.username} has answered your question {question.title}"[:500],
                                    link="/question/" + str(question.id))
        notification.save()
        answer_dict = {'id': answer.id,
                       'author': getattr(answer.author, 'username', 'Anonymous'),
                       'content': answer.content,
                       'pub_date': answer.pub_date,
                       'score': answer.score,
                       'is_solution': answer.is_solution}
        return JsonResponse(answer_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def submit_comment(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        post_data = json.loads(request.body)
        content = post_data['content']
        author = request.user
        comment = Comment(question=question, content=content, author=author)
        comment.save()
        comment_dict = {'id': comment.id,
                        'author': getattr(comment.author, 'username', 'Anonymous'),
                        'content': comment.content,
                        'pub_date': comment.pub_date}
        return JsonResponse(comment_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def upvote_question(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        # check if user has already upvoted or downvoted
        if question.upvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": question.score, "error": "You have already upvoted this question"})
        if question.downvotes.filter(id=request.user.id).exists():
            # remove from downvotes and increase score
            question.downvotes.remove(request.user)
            question.score += 1
        # add to upvotes and increase score
        question.upvotes.add(request.user)
        question.score += 1
        question.save()
        return JsonResponse({"success": True, "score": question.score})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def downvote_question(request, question_id):
    if request.method == 'POST':
        question = Question.objects.get(id=question_id)
        # check if user has already upvoted or downvoted
        if question.downvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": question.score, "error": "You have already downvoted this question"})
        if question.upvotes.filter(id=request.user.id).exists():
            # remove from upvotes and decrease score
            question.upvotes.remove(request.user)
            question.score -= 1
        # add to downvotes and decrease score
        question.downvotes.add(request.user)
        question.score -= 1
        question.save()
        return JsonResponse({"success": True, "score": question.score})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def upvote_answer(request, question_id, answer_id):
    if request.method == 'POST':
        answer = Answer.objects.get(id=answer_id)
        # check if user has already upvoted or downvoted
        if answer.upvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": answer.score, "error": "You have already upvoted this answer"})
        if answer.downvotes.filter(id=request.user.id).exists():
            # remove from downvotes and increase score
            answer.downvotes.remove(request.user)
            answer.score += 1
        # add to upvotes and increase score
        answer.upvotes.add(request.user)
        answer.score += 1
        answer.save()
        return JsonResponse({"success": True, "score": answer.score})


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def downvote_answer(request, question_id, answer_id):
    if request.method == 'POST':
        answer = Answer.objects.get(id=answer_id)
        # check if user has already upvoted or downvoted
        if answer.downvotes.filter(id=request.user.id).exists():
            return JsonResponse(
                {"success": False, "score": answer.score, "error": "You have already downvoted this answer"})
        if answer.upvotes.filter(id=request.user.id).exists():
            # remove from upvotes and decrease score
            answer.upvotes.remove(request.user)
            answer.score -= 1
        # add to downvotes and decrease score
        answer.downvotes.add(request.user)
        answer.score -= 1
        answer.save()
        return JsonResponse({"success": True, "score": answer.score})
