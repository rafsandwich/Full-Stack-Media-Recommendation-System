from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #(loginrequiredmixin) redirect new review attempts not logged in to login page
from django.contrib.auth.models import User
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

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews.html' #<model> name _ <viewtype>
    context_object_name = 'reviews'
    ordering = ['-date_posted'] #ordering newest anime reviews first
    paginate_by = 6

class UserReviewListView(ListView):
    model = Review
    template_name = 'user_reviews.html' 
    context_object_name = 'reviews'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #kwargs query paramaters, gets username from url
        return Review.objects.filter(author=user).order_by('-date_posted')

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['head', 'body']
    template_name = 'review_form.html'
    #success_url = home page eg if wanted redirect somewhere else

    def form_valid(self, form):
        form.instance.author = self.request.user #set author of instance to current logged in user
        return super().form_valid(form) #send author before validation of form

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['head', 'body']
    template_name = 'review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    #protect reviews from being updated by bad users
    def test_func(self):
        review = self.get_object() #get review trying to be updated
        #if logged in user is the same as author of review in question
        if self.request.user == review.author:
            return True
        else:
            return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url='/reviews'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        else:
            return False