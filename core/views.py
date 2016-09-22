# coding=utf-8
from django.shortcuts import render
from django.views.generic import CreateView, FormView


# Create your views here.


def logout():
    pass

# TODO 如何结合rest api??


class NextUrlMixin(object):
    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET.get('next')

        return super(NextUrlMixin, self).get_success_url()


class LoginView(NextUrlMixin, FormView):
    pass


class AccountRegistrationView(CreateView):
    pass
