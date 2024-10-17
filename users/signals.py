from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import UserProfile

# @receiver(post_save, sender=UserProfile)
# def validate_user_profile(sender, instance, **kwargs):
#     if instance.user_type == 'customer' and instance.skills.exists():
#         raise ValidationError(_('Customers cannot have skills.'))
#     if instance.user_type == 'support' and not instance.skills.exists():
#         raise ValidationError(_('Supports must have skills.'))
