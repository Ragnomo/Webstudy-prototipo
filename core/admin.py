from django.contrib import admin
from .models import Course, Module, Lesson, Exercise, QuizQuestion, UserProgress

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Exercise)
admin.site.register(QuizQuestion)
admin.site.register(UserProgress)
