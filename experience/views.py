from django.shortcuts import render, redirect
from django.contrib import messages
from apiclient.discovery import build
from .models import Experience, Organizer


api_key = "AIzaSyDJeSsqZU2ANJcMq1rACgfMqy86iXEgHW8"
resource = build("customsearch", 'v1', developerKey=api_key).cse()

def home(request):
    context = {
        'check': 'hey',
    }
    print(context)
    return render(request, 'experience/home.html', context)

def newExperiencePost(request):
    if request.method == 'POST':
        form = request.POST.dict()
        organizer_logo = 'logo '+form.get("organization_name")
        result = resource.list(q=organizer_logo, cx='009788653011454125862:nwy48iuc4ai', searchType='image').execute()
        obj, created = Organizer.objects.get_or_create(
            organization_name = form.get("organization_name"),
            organizer_logo_link = result['items'][0]['link'],
        )
        if created:
            obj.save()
        p = Experience(
                author_name=form.get("author_name"),
                author_email = form.get("author_email"),
                author_about = form.get("author_about"),
                result_field = form.get("result_field"),
                experience_result_more = form.get("experience_result_more"),
                experience_type_field = form.get("experience_type_field"),
                organization = obj,
                experience_title = form.get("experience_title"),
                experience_desc = form.get("experience_desc"),
                experience_recommendation = form.get("experience_recommendation"),
                experience_start_date = form.get("experience_start_date"),
                experience_end_date = form.get("experience_end_date"),
                website = form.get("website"),
                status = 2
            )
        p.save()
        context = {
        'check':'hey',
        }
        messages.add_message(request, messages.SUCCESS,"You experience post has been sent for review!")
        return redirect('experience-home')
    else:
        return render(request, 'experience/experience_post_form.html')
