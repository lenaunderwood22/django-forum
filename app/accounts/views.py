from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages


from .forms import UserCreationForm


# from .forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    # success_url = reverse_lazy('login')
    success_url = reverse_lazy('topic_list')
    template_name = 'registration/signup.html'

    def get_success_url(self, user_id):
        return reverse_lazy('view_profile', args=(user_id,))

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        email = self.request.POST['email']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(email=email, password=password)
        login(self.request, user)
        messages.success(self.request, f"Success!  New account created: {email}", extra_tags="success_register")
        return HttpResponseRedirect(self.get_success_url(user.id))

def logout_redirect(request):
    messages.success(request, f"You are now logged out.", extra_tags='success_logout')
    return HttpResponseRedirect(reverse('login'))