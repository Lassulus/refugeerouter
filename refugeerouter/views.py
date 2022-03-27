import json

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from refugeerouter.api import RefugeeSerializer, GroupSerializer
from refugeerouter.models import Group, Refugee
from django.views.generic.edit import UpdateView
from refugeerouter.forms import UpdateGroupForm


# Create your views here.
def group(request):
    return render(request, 'group.html')


def add_group(request):
    return render(request, 'add_group.html')


def edit_group(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        serialized_group = GroupSerializer(group).data
        return render(request, 'add_group.html',
                      {'group': json.dumps(serialized_group),
                       'editing': True
                       })
    else:
        data = json.loads(request.body)
        group.name = data['name']
        group.wish_city = data.get('wish_city', None)
        group.notes = data.get('notes', None)
        for ref in data['refugees']:
            if ref['id']:
                refugee = Refugee.objects.get(pk=ref['id'])
                for key, value in ref.items():
                    setattr(refugee, key, value)
                refugee.save()
            else:
                Refugee.objects.create(group=group, **ref)
        group.save()
        return JsonResponse({'ok': 'ok'})

# class GroupUpdateView(LoginRequiredMixin, UpdateView):
#     model = Group
#     template_name = "add_group.html"
#     form_class = UpdateGroupForm
