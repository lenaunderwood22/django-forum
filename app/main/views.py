from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Count
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.paginator import Paginator, Page

from .models import Topic, Comment

from user.models import User, UserManager

# Create your views here.
def topicsList(request, filter="all"):
    latest_posts = Topic.objects.order_by('-pub_date')
    if filter == "solved":
        latest_posts = Topic.objects.filter(solved=True).order_by('-pub_date')
    if filter == "unsolved":
        latest_posts = Topic.objects.filter(solved=False).order_by('-pub_date')
    if filter == "no_replies":
        latest_posts = Topic.objects.annotate(comment_count=Count('comment')).filter(comment_count=0)
    
    if request.method == 'GET':
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
            latest_posts = Topic.objects.filter(title__contains=search_query)
        # if request.GET.get('page'):
        paginator = Paginator(latest_posts, 4)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        latest_posts = paginator.page(page_number)
    
    context = {
        'latest_posts': latest_posts,
        'page_obj': page_obj,
    }

    return render(request, 'main/topic_list.html', context)

def createTopic(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            topic_content = request.POST['description']
            topic_title = request.POST['title']
            if Topic.objects.filter(title=topic_title, content=topic_content).count() == 0:
                Topic.objects.create(title=topic_title, content=topic_content, author=request.user)
            return HttpResponseRedirect(reverse('topic_list'))
    return render(request, 'main/topic_create.html') #, context)
# return HttpResponse("Create a new topic here.")

def replyTopic(request, topic_id):
    this_topic = Topic.objects.get(pk=topic_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('reply'):
                comment_content = request.POST['reply']
                comment_author = request.user
                Comment.objects.create(content=comment_content, author=comment_author, topic=this_topic)
            else:
                this_topic.solved = True
                this_topic.save()
    return render(request, 'main/topic_detail.html', {'topic': this_topic})
    # return HttpResponse("Reply to topic %s here." % topic_id)

def login(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        user_pwd = request.POST['password']
        user = authenticate(request, email=user_email, password=user_pwd)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('profile'))
    return render(request, 'main/login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'main/logout.html')

def register(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_pwd = request.POST.get('password')
        user = User.objects.create_user(user_email, password=user_pwd)
        if request.POST.get('first_name'):
            user.first_name = request.POST.get('first_name')
        if request.POST.get('last_name'):
            user.last_name = request.POST.get('last_name')
        if request.POST.get('username'):
            user.username = request.POST.get('username')
        user.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'main/register.html')

def profile(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user = User.objects.get(email=user_email)
        user.email = user_email
        if request.POST.get('first_name'):
            user.first_name = request.POST.get('first_name')
        if request.POST.get('last_name'):
            user.last_name = request.POST.get('last_name')
        if request.POST.get('username'):
            user.username = request.POST.get('username')
        if request.POST.get('status'):
            user.status = request.POST.get('status')
        if request.FILES.get('profile_photo'):
            user.avatar = request.FILES['profile_photo']
        user.save()
    return render(request, 'main/profil.html')

def resetPwdForm(request):
    return render(request, 'main/reset_pwd_form.html')

def resetPwdDone(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
    return render(request, 'main/reset_pwd_done.html')

def resetPwdConfirm(request):
    return render(request, 'main/reset_pwd_confirm.html')

def resetPwdComplete(request):
    return render(request, 'main/reset_pwd_complete.html')

class HomeTemplateView(TemplateView):
    template_name = 'main/home.html'

class LoginTemplateView(TemplateView):
    template_name = 'main/login.html'

class RegisterTemplateView(TemplateView):
    template_name = 'main/register.html'

class ResetPwdFormTemplateView(TemplateView):
    template_name = 'main/reset_pwd_form.html'

class ResetPwdDoneTemplateView(TemplateView):
    template_name = 'main/reset_pwd_done.html'

class ResetPwdConfirmTemplateView(TemplateView):
    template_name = 'main/reset_pwd_confirm.html'

class ResetPwdCompleteTemplateView(TemplateView):
    template_name = 'main/reset_pwd_complete.html'

class ProfilTemplateView(TemplateView):
    template_name = 'main/profil.html'

class TopicListTemplateView(TemplateView):
    template_name = 'main/topic_list.html'

class TopicDetailTemplateView(TemplateView):
    template_name = 'main/topic_detail.html'

class TopicCreateTempalteView(TemplateView):
    template_name = 'main/topic_create.html'

class ReactTempalteView(TemplateView):
    template_name = 'main/react.html'