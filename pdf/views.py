from django.shortcuts import render, redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader 
import io
from django.contrib import messages 

# Create your views here.

def create_cv(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        previous_work = request.POST.get("previous-work","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        skills = request.POST.get("skills","")

        user_profile = Profile.objects.create(
            name=name, 
            email=email, 
            phone=phone,
            summary=summary, 
            previous_work=previous_work, 
            degree=degree, 
            university=university , 
            skills=skills,
            school=school
            )
        messages.success(request, "Resume Created Successfully")
        return redirect ("profiles")
    else:
        messages.warning(request, "There was an error creating resume. Please try again")
        return render(request, "pdf/accept.html")


def generated_cv_view(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template("pdf/resume.html")
    html = template.render({ "user_profile":user_profile})
    options={
        "page-size":"Letter",
        "encoding" : "UTF-8"
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type="application/pdf")
    response["Content-Disposition"] = "attachment"
    filename = "resume.pdf"
    return response



def list_of_profiles(request):
    profiles = Profile.objects.all()
    return render(request, "pdf/list.html",{ "profiles":profiles })