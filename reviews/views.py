from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib import messages
from .models import Review


def reviews(request):
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been posted')
            return redirect(reverse('reviews'))
        else:
            form = ReviewForm()

    form = ReviewForm()
    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'reviews/reviews.html', context)
