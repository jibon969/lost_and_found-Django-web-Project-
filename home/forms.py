from django import forms
from .models import Reward


class RewardModeLForm(forms.ModelForm):

    class Meta:
        model = Reward
        fields = [
            'text'
        ]