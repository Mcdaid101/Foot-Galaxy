from django.shortcuts import render


def view_faqs(request):
    """ A view to return the FAQ's page """

    return render(request, 'info/faqs.html')