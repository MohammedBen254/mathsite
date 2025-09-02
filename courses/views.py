from django.shortcuts import render, get_object_or_404
# from .models import Course, Chapter, Exam
from django.shortcuts import redirect # Import redirect to handle post-submission redirects
from django.contrib import messages # Import the messages framework
from .forms import ContactForm # Import your new form
from .models import Course, Chapter, Exam, SchoolLevel

# This view shows ALL courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# --- Add this new view function ---
def courses_by_level(request, level_id):
    # Get the specific school level the user clicked on
    level = get_object_or_404(SchoolLevel, pk=level_id)
    # Get all courses that belong to that level
    courses = Course.objects.filter(level=level)
    # Reuse the same template, but pass the specific level and filtered courses
    context = {
        'level': level,
        'courses': courses
    }
    return render(request, 'courses/course_list.html', context)

# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    chapters_found = course.chapter_set.all()
    print(f"DEBUG: Course is '{course.title}'. Chapters found: {chapters_found[0].pdf_file}")

    return render(request, 'courses/course_detail.html', {'course': course})

def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    
    return render(request, 'courses/chapter_detail.html', {'chapter': chapter})

def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'courses/exam_list.html', {'exams': exams})

def contact(request):
    form = ContactForm()
    return render(request, 'courses/contact.html', {'form': form})

# View to process the form data
def send_contact_info(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # The data is valid, you can now access it
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message']

            # THIS IS THE FIX:
            # Instead of message(...), use print() to see it in the terminal
            print(f"Contact form submitted by: {name} ({email})")
            print(f"Message: {message_text}")

            # Optional: Show a success message to the user on the page
            messages.success(request, 'Your message has been sent successfully!')

            # Redirect back to the contact page after successful submission
            return redirect('contact')
    else:
        # If not a POST request, just redirect to the contact page
        return redirect('contact')