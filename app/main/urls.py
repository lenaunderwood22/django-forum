from django.urls import path, include

from . import views

import main.views

main_urlpatterns = [
    # path('login/', main.views.LoginTemplateView.as_view(), name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:user_username>', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    # path('register/', main.views.RegisterTemplateView.as_view(), name='register'),
    # path('login/', main.views.LoginTemplateView.as_view(), name='login'),
    # path('register/', main.views.RegisterTemplateView.as_view(), name='register'),
    # path('profil/', main.views.ProfilTemplateView.as_view(), name='profil'),
    path('reset_pwd_form/', views.resetPwdForm, name='reset_pwd_form'),
    path('reset_pwd_done/', views.resetPwdDone, name='reset_pwd_done'),
    path('reset_pwd_confirm/', views.resetPwdConfirm, name='reset_pwd_confirm'),
    path('reset_pwd_complete/', views.resetPwdComplete, name='reset_pwd_complete'),
    # path('reset_pwd_form/', main.views.ResetPwdFormTemplateView.as_view(), name='reset_pwd_form'),
    # path('reset_pwd_done/', main.views.ResetPwdDoneTemplateView.as_view(), name='reset_pwd_done'),
    # path('reset_pwd_confirm/', main.views.ResetPwdConfirmTemplateView.as_view(), name='reset_pwd_confirm'),
    # path('reset_pwd_complete/', main.views.ResetPwdCompleteTemplateView.as_view(), name='reset_pwd_complete'),
    path('topics/', views.topicsList, name='topic_list'),
    path('topics/?filter=<str:filter>', views.topicsList, name='topic_list'),
    path('topics/new/', views.createTopic, name='topic_create'),
    path('topics/<int:topic_id>/', views.replyTopic, name='topic_detail'),
    # path('topics/', main.views.TopicListTemplateView.as_view(), name='topic_list'),
    # path('topics/topic_pk/', main.views.TopicDetailTemplateView.as_view(), name='topic_detail'),
    # path('topics/new/', main.views.TopicCreateTempalteView.as_view(), name='topic_create'),
    path('react/', main.views.ReactTempalteView.as_view(), name='react'),
    path('', main.views.HomeTemplateView.as_view(), name='home')
]

urlpatterns = [
    path('', main.views.HomeTemplateView.as_view(), name='home'),
    path('main/', include(main_urlpatterns)),
]