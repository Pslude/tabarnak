from django.views.generic import TemplateView
from django_registration.views import RegistrationView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .forms import JoinForm


class JoinView(RegistrationView):
    template_name = 'authentication/join_form.html'
    form_class = JoinForm
    success_url = reverse_lazy('authentication:join_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create an Account')
        return context

    #def post(self, request, *args, **kwargs):
    #return super().post(self, request, *args, **kwargs)

    def register(self, form, **kwargs):
        #if 'referrer_id' in self.request.session:
        #  form.instance.referrer_id = self.request.session['referrer_id']

        form.save()

        # log the new user in
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], )
        if new_user is None:
            raise Exception('Error authenticating new user')

        login(self.request, new_user)


class JoinDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'authentication/join_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Account Created')
        return context


class LoggedOutView(TemplateView):
    template_name = 'authentication/logged_out.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Logged Out')
        return context

    def get(self, request, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('logout')
        return super().get(request, **kwargs)
