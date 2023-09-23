from django.contrib import auth
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.view import TitleMixin

from .forms import RegistrashionUser, UserLoginForm, UserProfileforms
from .models import Customuser, EmailVerification


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('/')

    else:
        form = UserLoginForm
    context = {'form': UserLoginForm()}
    context['title'] = 'Store - Авторизация'
    return render(request, 'users/login.html', context)


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = Customuser
    form_class = RegistrashionUser
    template_name = 'users/regisrtashion.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегестрированы'

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserProfileView(UpdateView):
    model = Customuser
    form_class = UserProfileforms
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))


def logout(request):
    auth.logout(request)
    return redirect('/')


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html/'
    title = 'Успешно подтверждено'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = Customuser.objects.get(email=kwargs['email'])
        email_verificathions = EmailVerification.objects.filter(user=user, code=code)
        if email_verificathions.exists() and not email_verificathions.first().is_expired():
            user.is_verified = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
