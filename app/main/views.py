from django.http.request import HttpRequest
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Count
from django.urls import reverse
from django.contrib.auth import authenticate, get_user
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.paginator import Paginator
from django.contrib import messages
from slugify import slugify


from .models import Topic, Comment

# from user.models import User, UserManager

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def topicsList(request, filter="all", search_query=None): # sortby='pub_date'
    # if sortby=='pub_date': second_sortby='comment_count'
    # latest_posts = Topic.objects.annotate(comment_count=Count('comment')).order_by('-'+sortby)
    latest_posts = Topic.objects.order_by('-pub_date')
    if filter == "solved":
        latest_posts = Topic.objects.filter(solved=True).order_by('-pub_date')
    if filter == "unsolved":
        latest_posts = Topic.objects.filter(solved=False).order_by('-pub_date')
    if filter == "no_replies":
        latest_posts = Topic.objects.annotate(comment_count=Count('comment')).filter(comment_count=0).order_by('-pub_date')
    
    if request.method == 'GET' or search_query != None:
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
            latest_posts = Topic.objects.filter(title__contains=search_query).order_by('-pub_date')
        if search_query != None:
            latest_posts = Topic.objects.filter(title__contains=search_query).order_by('-pub_date')
        paginator = Paginator(latest_posts, 4)
        page_number = request.GET.get('page', 1)
        latest_posts = paginator.page(page_number)
        
    context = {
        'latest_posts': latest_posts,
        'search_query': search_query,
        'filter': filter,
        # 'sortby': sortby,
    }
    return render(request, 'main/topic_list.html', context)

def createTopic(request):
    form_errors={}
    if request.method == 'POST':
        if request.user.is_authenticated:
            topic_content = request.POST['description']
            topic_title = request.POST['title']
            if topic_content=="" or topic_title=="":
                if topic_content=="":
                    form_errors['content'] = "This is a required field."
                if topic_title=="":
                    form_errors['title'] = "This is a required field."
            else:
                topic_slug = slugify(topic_title)+'-'+str(Topic.objects.last().id+1)
                topic = Topic.objects.create(title=topic_title, content=topic_content, author=request.user, slug=topic_slug)
                messages.success(request, f"Success!  Your topic has been posted.", extra_tags='success_topic_create')
                return HttpResponseRedirect(reverse('topic_detail', args=(topic.slug,)))
    return render(request, 'main/topic_create.html', {'form_errors': form_errors})
# return HttpResponse("Create a new topic here.")

def replyTopic(request, slug, filter='all', search_query=None):
    form_errors={}
    this_topic = Topic.objects.get(slug=slug)
    latest_comments = this_topic.comment_set.order_by('pub_date')
    paginator = Paginator(latest_comments, 4)
    page_number = request.GET.get('page', 1)
    latest_comments = paginator.page(page_number)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if "close_topic_btn" in request.POST:
                this_topic.solved = True
                this_topic.save()
                messages.success(request, f"Success!  You marked this topic as solved.", extra_tags='success_topic_close')
            elif "reply_signed_in" in request.POST or request.POST['reply_signed_in']=="":
                comment_content = request.POST['reply_signed_in']
                comment_author = request.user
                if comment_content=="":
                    form_errors['content'] = "This is a required field."
                else:
                    comment = Comment.objects.create(content=comment_content, author=comment_author, topic=this_topic)
                    latest_comments = this_topic.comment_set.order_by('pub_date')
                    paginator = Paginator(latest_comments, 4)
                    page_number = request.GET.get('page', 1)
                    latest_comments = paginator.page(page_number)
                    return HttpResponseRedirect('?page=%s#comment_%s' % (paginator.num_pages, comment.id))
    return render(request, 'main/topic_detail.html', {'topic': this_topic, 'filter': filter, 'search_query': search_query, 'latest_comments': latest_comments, 'form_errors': form_errors})
    # return HttpResponse("Reply to topic %s here." % topic_id)

# def login(request):
#     if request.method == 'POST':
#         user_email = request.POST['username']
#         user_pwd = request.POST['password']
#         user = authenticate(request, email=user_email, password=user_pwd)
#         if user is not None:
#             auth_login(request, user)
#             return HttpResponseRedirect(reverse('home'))
#     return render(request, 'main/login.html')

# def logout(request):
#     auth_logout(request)
#     return render(request, 'main/logout.html')

# def register(request):
#     if request.method == 'POST':
#         user_email = request.POST.get('username')
#         user_pwd = request.POST.get('password')
#         # user = User.objects.create_user(user_email, password=user_pwd)
#         user = get_user_model().objects.create_user(user_email, password=user_pwd)
#         if request.POST.get('first_name'):
#             user.first_name = request.POST.get('first_name')
#         if request.POST.get('last_name'):
#             user.last_name = request.POST.get('last_name')
#         # if request.POST.get('username'):
#         #     user.username = request.POST.get('user_username')
#         user.save()
#         messages.success(request, f"New account created: {username}")

#         return HttpResponseRedirect(reverse('login'))
#     return render(request, 'main/register.html')

def editProfile(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        # user = User.objects.get(email=user_email)
        user = get_user_model().objects.get(email=user_email)
        user.email = user_email
        if request.FILES.get('profile_photo'):
            user.avatar = request.FILES['profile_photo']
            user.save()
        else:
            if request.POST.get('first_name'):
                user.first_name = request.POST.get('first_name')
            if request.POST.get('last_name'):
                user.last_name = request.POST.get('last_name')
            if request.POST.get('username'):
                user.user_username = request.POST.get('username')
            user.save()
            messages.success(request, f"Success!  Your profile has been updated.", extra_tags='success_profile_update')
            return HttpResponseRedirect(reverse('view_profile', args=(user.id,)))
    return render(request, 'main/profile_edit.html')

def viewProfile(request, user_id):
    this_user = get_user_model().objects.get(pk=user_id)
    latest_posts = Topic.objects.filter(author=this_user).order_by('-pub_date')
    paginator = Paginator(latest_posts, 4)
    page_number = request.GET.get('page', 1)
    latest_posts = paginator.page(page_number)
    context = {
        'user': this_user,
        'latest_posts': latest_posts,
    }
    return render(request, 'main/profile_view.html', context)

def getProfile(request):
    user = request.user
    return HttpResponseRedirect(reverse('view_profile', args=(user.id,)))

# def resetPwdForm(request):
#     return render(request, 'main/reset_pwd_form.html')

# def resetPwdDone(request):
#     if request.method == 'POST':
#         user_email = request.POST.get('email')
#     return render(request, 'main/reset_pwd_done.html')

# def resetPwdConfirm(request):
#     return render(request, 'main/reset_pwd_confirm.html')

# def resetPwdComplete(request):
#     return render(request, 'main/reset_pwd_complete.html')

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