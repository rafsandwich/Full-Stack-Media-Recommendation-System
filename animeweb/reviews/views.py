from django.shortcuts import render
from django.http import HttpResponse
from recommend.models import Review

#legacy dummy data
testreviews = [
    {
        'author':'sachi95',
        'title':'SAO sucks!',
        'content':'they killed me off smh',
        'date_posted': '1 January 2022',
    },
    {
        'author':'raf',
        'title':'second review',
        'content':'grrr gosh diddly darn it you kno',
        'date_posted': '4 January 2022',
    },
]

# Create your views here.
def reviewsMain(request):
    context={
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews.html', context)
