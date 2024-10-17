from django.contrib import admin
from .models import UserProfile, Skill
from .forms import UserProfileForm

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    list_display = ('user', 'user_type', 'phone_number', 'get_skills')
    search_fields = ('user__username', 'phone_number', 'user_type')
    list_filter = ('user_type',)
    list_per_page = 20

    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])
    get_skills.short_description = 'Skills'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 20
    
    

