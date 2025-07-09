from django.shortcuts import render

# Create your views here.
def index(request):
    """
        Render the index page.
    """
    # Here you can add any context data you want to pass to the template
    context = {}
    return render(request, 'index.html', context)