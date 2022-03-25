from django import forms
from refugeerouter.models import Group


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            "name",
            "wish_city"
        ]
