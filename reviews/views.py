from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm(request.POST)
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })

# def review(request):
#   if request.method == 'POST':
#     form = ReviewForm(request.POST)
#     #to update data
#     # existing_data = Review.objects.get(pk=1)
#     # form = ReviewForm(request.POST, instance=existing_data)

#     if form.is_valid():
#       # review = Review(
#       #   user_name=form.cleaned_data['user_name'],
#       #   review_text=form.cleaned_data['review_text'],
#       #   rating=form.cleaned_data['rating'])
#       form.save()
#       print(form.cleaned_data)
#       return HttpResponseRedirect("/thank-you")

#   else:
#     form = ReviewForm()

#   return render(request, "reviews/review.html", {
#     "form": form
#   })


# class ThankYouReview(View):

#     def get(self, request):
#         return render(request, 'reviews/thank_you.html')


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Hii" 
        return context
    

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] =  reviews
#         return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html" 
    model = Review 
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=1)
        return data
    

    

class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"] # same as wriiten in path in urls.py
        selected_review = Review.objects.get(pk=review_id)
        context["review"] = selected_review
        return context
    


