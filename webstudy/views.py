from django.shortcuts import render

def index(request):
    """
    Renders the main index page.
    """
    context = {} # You can pass data to your template here
    return render(request, 'index.html', context)
