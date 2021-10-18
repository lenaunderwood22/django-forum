from django.urls import path, include

from . import views

import main.views

main_urlpatterns = [
    # path('login/', main.views.LoginTemplateView.as_view(), name='login'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('logout/', views.logout, name='logout'),
    # path('reset_pwd_form/', views.resetPwdForm, name='reset_pwd_form'),
    # path('reset_pwd_done/', views.resetPwdDone, name='reset_pwd_done'),
    # path('reset_pwd_confirm/', views.resetPwdConfirm, name='reset_pwd_confirm'),
    # path('reset_pwd_complete/', views.resetPwdComplete, name='reset_pwd_complete'),

    # path('register/', main.views.RegisterTemplateView.as_view(), name='register'),
    # path('login/', main.views.LoginTemplateView.as_view(), name='login'),
    # path('register/', main.views.RegisterTemplateView.as_view(), name='register'),
    # path('profil/', main.views.ProfilTemplateView.as_view(), name='profil'),
    # path('reset_pwd_form/', main.views.ResetPwdFormTemplateView.as_view(), name='reset_pwd_form'),
    # path('reset_pwd_done/', main.views.ResetPwdDoneTemplateView.as_view(), name='reset_pwd_done'),
    # path('reset_pwd_confirm/', main.views.ResetPwdConfirmTemplateView.as_view(), name='reset_pwd_confirm'),
    # path('reset_pwd_complete/', main.views.ResetPwdCompleteTemplateView.as_view(), name='reset_pwd_complete'),
    # path('topics/', main.views.TopicListTemplateView.as_view(), name='topic_list'),
    # path('topics/topic_pk/', main.views.TopicDetailTemplateView.as_view(), name='topic_detail'),
    # path('topics/new/', main.views.TopicCreateTempalteView.as_view(), name='topic_create'),

    path('profile/edit', views.editProfile, name='edit_profile'),

    path('profile/view/<int:user_id>/', views.viewProfile, name='view_profile'),
    path('profile/view', views.getProfile, name='view_profile'),

    path('topics/', views.topicsList, name='topic_list'),
    path('topics/?filter=<str:filter>', views.topicsList, name='topic_list'),
    path('topics/?search_query=<str:search_query>', views.topicsList, name='topic_list'),
    path('topics/?sortby=<str:sortby>', views.topicsList, name='topic_list'),
    # path('topics/?filter=<str:filter>?sortby=<str:sortby>', views.topicsList, name='topic_list'),

    path('topics/new/', views.createTopic, name='topic_create'),

    path('topics/<slug:slug>/', views.replyTopic, name='topic_detail'),
    path('topics/<slug:slug>/?filter=<str:filter>', views.replyTopic, name='topic_detail'),
    path('topics/<slug:slug>/?search_query=<str:search_query>', views.replyTopic, name='topic_detail'),
    path('topics/<slug:slug>/?page=<int:page>#comment_<int:comment_id>', views.replyTopic, name='topic_detail'),
    path('topics/<slug:slug>/?filter=<str:filter>?page=<int:page>#comment_<int:comment_id>', views.replyTopic, name='topic_detail'),
    path('topics/<slug:slug>/?search_query=<str:search_query>?page=<int:page>#comment_<int:comment_id>', views.replyTopic, name='topic_detail'),
    path('react/', main.views.ReactTempalteView.as_view(), name='react'),
    path('', main.views.HomeTemplateView.as_view(), name='home'),
]

urlpatterns = [
    path('', main.views.HomeTemplateView.as_view(), name='home'),
    path('main/', include(main_urlpatterns)),
]