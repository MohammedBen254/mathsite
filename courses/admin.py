from django.contrib import admin
from .models import SchoolLevel, Course, Chapter, Exercise, Exam

admin.site.register(SchoolLevel)
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Exercise)
admin.site.register(Exam)