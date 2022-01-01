from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import new_user

# Create your views here.

def index(request):
    return HttpResponse('<em>Hello World!</em>')

def help(request):
    my_dic = {'new_content': 'Help form Django'}
    return render(request, 'AppTwo/help.html.', context=my_dic)

def upload_records(request):
    info_list = User.objects.order_by('First_name')
    inf_dict = {'user_data': info_list}
    return render(request, 'AppTwo/recpage.html', context=inf_dict)

def n_user(request):
    form = new_user()

    if request.method == 'POST':
        form = new_user(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error form invalid")

    return render(request, 'AppTwo/user.html', {'form': form})