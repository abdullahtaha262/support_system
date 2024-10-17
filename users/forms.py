from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile, Skill
from django.utils.translation import gettext_lazy as _

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'user_type', 'phone_number', 'skills']

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        skills = cleaned_data.get('skills')

        # Initial validation (not accessing many-to-many yet)
        if user_type == 'customer' and skills:
            raise ValidationError(_('Customers cannot have skills.'))
        if user_type == 'support' and not skills:
            raise ValidationError(_('Supports must have at least one skill.'))

        return cleaned_data