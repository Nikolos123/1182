from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from baskets.models import Basket
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])

    subject = f'Для активации учетной записи {user.username} пройдите по ссылке'

    messages = f'Для подтверждения учетной записи {user.username} пройдите по ссылке: \n{settings.DOMAIN_NAME}' \
               f'{verify_link}'

    return send_mail(subject, messages, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    user = User.objects.get(email=email)
    if user and user.activation_key == activation_key and not user.is_activation_key_expires():
        user.is_active = True
        user.activation_key_create = None
        user.activation_key = ''
        user.save()
        auth.login(request, user)
        # return render(request, 'users/verification.html')
    return render(request, 'users/verification.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form
    }

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        # total_quantity = 0
        # total_sum = 0
        baskets = Basket.objects.filter(user=request.user)
        # if baskets:
        #     for basket in baskets:
        #         total_quantity += basket.quantity
        #         total_sum += basket.sum()
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'GeekShop - Профиле',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
        # 'total_quantity': sum(basket.quantity for basket in baskets),
        # 'total_sum': sum(basket.sum() for basket in baskets),
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
