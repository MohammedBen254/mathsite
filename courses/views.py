from django.shortcuts import render, get_object_or_404
from .models import Course, Chapter, Exam

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    return render(request, 'courses/chapter_detail.html', {'chapter': chapter})

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'courses/exam_list.html', {'exams': exams})