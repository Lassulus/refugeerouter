from django import forms
from refugeerouter.models import Group


class UpdateGroupForm(forms.ModelForm):
    signature = forms.CharField(required=False, widget=forms.TextInput(attrs={"readonly": "readonly"}))

    class Meta:
        model = Group
        fields = [
            "name",
            "wish_city"
        ]
