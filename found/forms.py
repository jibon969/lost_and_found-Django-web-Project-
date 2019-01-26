
from django import forms
from person.models import Person
from item.models import Item


class FoundPersonModelForm(forms.ModelForm):
    """
    This model form work for user create a post for person attribute
    """
    class Meta:
        model = Person

        fields = [
            'status',
            'person',
            'name',
            'father_name',
            'mother_name',
            'gender',
            'age',
            'body_color',
            'height',
            'image',
            'location',
            'phone_number',
            'identification_mark',
            'secret_information'

        ]


class FoundItemModelForm(forms.ModelForm):
    """
    This model work user can create this post this attribute of item create form
    """
    class Meta:
        model = Item
        fields = [
            'status',
            'name',
            'phone_number',
            'category',
            'location',
            'image',
            'identification_mark',
            'secret_information',
        ]