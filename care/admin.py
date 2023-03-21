from django.contrib import admin
from .models import Answer, Category,  Question
# Register your models here.
@admin.register(Category)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
class AnswerInlineModel(admin.ModelAdmin):
    model = Answer
    fields=[
        'answer_text',
        'is_right'
    ] 

    @admin.register(Question)

    class QuestionAdmin(admin.ModelAdmin):
        fields=[
            'title',
            'quiz',
        ]  
        list_display =[
            'title',
            'quiz',
            'date_updated'
        ]
   
    @admin.register(Answer)

    class AnswerAdmin(admin.ModelAdmin):
        
        list_display =[
            'answer_text',
            'is_right',
            'question'
        ]
    