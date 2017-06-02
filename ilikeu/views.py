from django.http import HttpResponseRedirect, Http404
from django.utils.datetime_safe import datetime

from .forms import LoginForm, SaveForm
from .models import Human
from .models import MateDates
from django.shortcuts import render
import time

# Create your views here.


def home(request):
    return render(request, 'blog/login.html', {})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data.get('gender')
            mate_date = form.cleaned_data.get('mate_date')
            convert_date = datetime.date(mate_date).strftime("%Y-%m-%d")
            phone_number = form.cleaned_data.get('phoneNumber')
            password = form.cleaned_data.get('password')
            mate_seq = form.cleaned_data.get('mate_seq')

            if gender is 'M':
                gender = 'W'
            else:
                gender = 'M'

            # if gender is 'M' than return Woman else return Man
            try:
                login_user = Human.objects.filter(
                    phoneNumber=phone_number, mate_date=convert_date,
                    password=password, mate_seq=mate_seq)
                login_user = Human.objects.get(pk=login_user[0].pk)
                mates = Human.objects.filter(mate_date=convert_date, gender=gender, mate_seq=login_user.mate_seq,)
                mate_dates = MateDates.objects.get(mate_date=convert_date, mate_seq=login_user.mate_seq, )
            except:
                if not login_user or not mates == 0:
                    return render(request, 'blog/login.html', {'alert': True})
                raise Http404('아이디 비번을 다시 입력해주세')

            if login_user.gender == mates[0].gender:
                return render(request, 'blog/login.html', {'alert': True})

            is_match = False
            choice_you = []
            choice_1 = 0
            choice_2 = 0

            for mate in mates:
                if login_user.choice1 == mate.number and \
                        (login_user.number == mate.choice1 or login_user.number == mate.choice2):
                    choice_1 = mate
                    is_match = True

                if login_user.choice2 == mate.number and \
                        (login_user.number == mate.choice1 or login_user.number == mate.choice2):
                    choice_2 = mate
                    is_match = True

                if login_user.number == mate.choice1 or \
                        login_user.number == mate.choice2:
                    choice_you.append(str(mate.number))

            context = {
                'login_user': login_user,
                'mates': mates,
                'mate_dates': mate_dates,
                'is_match': is_match,
                'choice_one': choice_1,
                'choice_two': choice_2,
                'choice_you': choice_you,
            }

            if login_user:
                return render(request, 'blog/profile-page.html', context)
        else:
            return render(request, 'blog/login.html', {'alert': True})
    else:
        return HttpResponseRedirect('blog/login.html', {'alert': True})
        # return render(request, 'blog/profile-page.html', {})


def save_choice(request):
    if request.method == 'POST':
        form = SaveForm(request.POST)
        if form.is_valid():
            # choice1 = form.cleaned_data.get('choice1')
            # choice2 = form.cleaned_data.get('choice2')
            choice_list = request.POST.getlist('choice')
            date = request.POST.get('mate_date');
            # May 6, 2017
            # convert_date = datetime.date(date).strftime("%Y-%m-%d")
            convert_date = time.strptime(date, "%Y-%m-%d")

            if len(choice_list) == 2:
                choice1 = choice_list[0]
                choice2 = choice_list[1]
            else:
                choice1 = choice_list[0]
                choice2 = 0

            phone_number = form.cleaned_data.get('phoneNumber')
            login_user = Human.objects.filter(phoneNumber=phone_number).update(choice1=choice1, choice2=choice2)
            context = {'login_user': login_user,}
            return render(request, 'blog/login.html', context)

    return render(request, 'blog/profile-page.html', {})
