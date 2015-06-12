from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Choiceship
from django.contrib.auth.models import User

class ChoiceshipInline(admin.TabularInline):
    model = Choice.members.through
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [ChoiceshipInline,]

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceshipInline,]
    exclude = ('members',)
    
admin.site.register(Choice, ChoiceAdmin)
#admin.site.register(User, UserAdmin)
    

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)