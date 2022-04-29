from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def handle_404(request, exception):
    """ Handle 404 erorrs and render 404 custom template """
    return render(request, '404.html')