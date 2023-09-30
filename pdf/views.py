from django.shortcuts import render
from .models import Profile
# Create your views here.

# def create_cv(request):
#     if request.method == "POST":
#         name = request.POST.get("name","")
#         email = request.POST.get("email","")
#         phone = request.POST.get("phone","")
#         summary = request.POST.get("summary","")
#         previous_work = request.POST.get("previous-work","")
#         degree = request.POST.get("degree","")
#         school = request.POST.get("school","")
#         university = request.POST.get("university","")
#         skills = request.POST.get("skills","")

#         user_profile = Profile.objects.create(
#             name=name, 
#             email=email, 
#             phone=phone,
#             summary=summary, 
#             previous_work=previous_work, 
#             degree=degree, 
#             university=university , 
#             skills=skills,
#             school=school
#             )
#     return render(request, "pdf/accept.html")


def generated_cv_view(request,id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, "pdf/resume.html",{ "user_profile":user_profile})
