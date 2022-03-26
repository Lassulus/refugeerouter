from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from refugeerouter.models import Group
from django.views.generic.edit import UpdateView
from refugeerouter.forms import UpdateGroupForm


# Create your views here.
def group(request):
    return render(request, 'group.html')


def add_group(request):
    return render(request, 'add_group.html')

class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = "group_update_view.html"
    form_class = UpdateGroupForm
