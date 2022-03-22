from django.shortcuts import render

# 导入HttpResponse
from django.http import HttpResponse

# django 认证模块导入
from django.contrib.auth import authenticate, login

# LoginForm, RegistrationForm 表单导入
from .forms import LoginForm, RegistrationForm, UserProfileForm

from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User



# Create your views here.
# 创建登录视图函数，视图函数必须使用request作为第一个参数
# 当用户通过URL向服务器发送请求时，Django会创建一个HttpRequest对象，request是HttpRequest的替代。


def user_login(request):
    if request.method == "POST":
        # 建一个绑定实例
        login_form = LoginForm(request.POST)
        # 判断数据是否合法
        if login_form.is_valid():
            # 引用字典类型数据
            cd = login_form.cleaned_data
            # 验证密码是否正确
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                # 引入login()函数，使用User实例对象作为参数，实现用户登录。用户登录之后，Django会自动调用默认的session应用，将用户ID保存在session中，完成用户登录操作。
                login(request, user)
                return HttpResponse("Welcome You. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


# 注册函数
def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, you can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})


# 用户信息
@login_required(login_url='/account/login')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, "account/myself.html", {"user": user, "userinfo": userinfo, "userprofile": userprofile})
