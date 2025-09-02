from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Course, Chapter, Exam, SchoolLevel, Exercise
from django.template.loader import render_to_string
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- Your email credentials (better to use environment variables in production) ---
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER='mathricsnewway@gmail.com'
EMAIL_HOST_PASSWORD = 'suda uuva moup wabg' # <-- CHANGE to your email password or app password

RECIEPENT_EMAIL='mathricsnewway@gmail.com'

# --- (course_list, courses_by_level, and other views remain the same) ---

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def courses_by_level(request, level_id):
    level = get_object_or_404(SchoolLevel, pk=level_id)
    view_type = request.GET.get('view', 'courses')
    context = {
        'level': level,
        'view_type': view_type,
    }
    if view_type == 'exams':
        exams_with_solution = Exam.objects.filter(level=level, with_solution=True)
        exams_blank = Exam.objects.filter(level=level, with_solution=False)
        context['exams_with_solution'] = exams_with_solution
        context['exams_blank'] = exams_blank
    else:
        courses = Course.objects.filter(level=level)
        context['courses'] = courses
    return render(request, 'courses/level_detail.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    chapters = course.chapter_set.all()
    exercises = Exercise.objects.filter(chapter__course=course)
    context = {
        'course': course,
        'chapters': chapters,
        'exercises': exercises,
    }
    return render(request, 'courses/course_detail.html', context)

def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    return render(request, 'courses/chapter_detail.html', {'chapter': chapter})

def exercise_detail(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    return render(request, 'courses/exercise_detail.html', {'exercise': exercise})

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'courses/exam_list.html', {'exams': exams})

def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    return render(request, 'courses/exam_detail.html', {'exam': exam})

def contact(request):
    form = ContactForm()
    return render(request, 'courses/contact.html', {'form': form})

def send_email(name, sender_email, message_text):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Contact Form Submission from {name}"
        msg["From"] = EMAIL_HOST_USER
        msg["To"] = RECIEPENT_EMAIL

        # --- THIS IS THE KEY CHANGE ---
        # 1. Prepare the context for the template
        email_context = {
            'name': name,
            'email': sender_email,
            'message': message_text,
        }
        # 2. Render the HTML from your template file
        html_part = render_to_string('courses/contact_email.html', email_context)
        # -----------------------------
        
        msg.attach(MIMEText(html_part, "html"))

        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(EMAIL_HOST_USER, RECIEPENT_EMAIL, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error sending email:", e)

def send_contact_info(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_email(name, email, message)
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
            return render(request, 'courses/contact.html', {'form': form})
    else:
        return redirect('contact')