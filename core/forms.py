# coding=utf-8


# 是否可以只覆盖class meta？？
from django.contrib.auth.forms import UserCreationForm
from core.models import User, UserInfo


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'nickname')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        # TODO commit情况下 user的pk是否已经存在？
        # TODO user新建后，userinfo表 也顺带新建
        if commit:
            user.save()
            user_info = UserInfo.objects.create(user=user)
            user_info.save()
        return user

