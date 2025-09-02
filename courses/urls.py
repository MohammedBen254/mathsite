# courses/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    # --- Add this new line for filtering by level ---
    path('level/<int:level_id>/', views.courses_by_level, name='courses_by_level'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('chapter/<int:pk>/', views.chapter_detail, name='chapter_detail'),
    path('exams/', views.exam_list, name='exam_list'),
    path('contact/', views.contact, name='contact'),  # New contact page URL
    path('send_contact_info/', views.send_contact_info, name='send_contact_info'),  # New URL for handling form submission
]