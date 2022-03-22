from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo


# 用户登录表单
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# 用户注册表单
# 如果表单中的数据写入数据库表或者修改某些记录的值，就要让表单继承ModelForm类， 如果提交表单之后，不会对数据库进行修改，则继承Form类
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError("passwords do not match.")
            return cd['password2']


# 用户属性表单
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme")

    class UserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ("email",)
