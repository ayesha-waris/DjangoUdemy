import profile
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView

from profiles.forms import ProfileForm
from profiles.models import UserProfile

# Create your views here.

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html",{
#             "form" : form
#         })

#     def post(self, request):
        
#         submitted_form = ProfileForm(request.POST, request.FILES)


#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             # store_file(request.FILES["user_image"])
#             print(request.FILES["user_image"])
#             return HttpResponseRedirect("/profiles")
       
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })
