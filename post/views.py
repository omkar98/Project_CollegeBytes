from django.shortcuts import render, redirect
from post.importData import posts
from .models import Employment, User, Hackathon, OtherPost
from django.views.generic import ListView, DetailView
from django.contrib import messages
from apiclient.discovery import build

api_key = "AIzaSyDJeSsqZU2ANJcMq1rACgfMqy86iXEgHW8"
resource = build("customsearch", 'v1', developerKey=api_key).cse()

def home(request):
    superusers = User.objects.filter(is_superuser=True).all()
    print(superusers[0])
    context = {
        'job_posts':Employment.objects.filter(post_type=1).order_by('-id'),
        'internship_posts': Employment.objects.filter(post_type=2).order_by('-id'),
        'hackathon_posts':Hackathon.objects.all().order_by('-id')
    }
    print(context)
    return render(request, 'post/home.html', context)

class PostListView(ListView):
    model = Employment
    template_name = 'post/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = [-date_posted]

class PostDetailView(DetailView):
    model = Employment
    slug_field = 'post_type'
    slug_url_kwarg = 'post_type'
    template_name = 'post/jobPost.html'    # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    # post = Employment.objects.get(current.id)
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.views+=1
        obj.save()
        return obj



def newEmploymentPost(request):
    form = request.POST.dict()
    if request.method == 'POST':
        # print(form)
        company_logo = 'logo '+form.get("company_name")
        # print(company_logo)
        print(form.get("last_date"))
        result = resource.list(q=company_logo, cx='009788653011454125862:nwy48iuc4ai', searchType='image').execute()
        p = Employment(
                role=form.get("role"),
                salary = form.get("salary"),
                openings = form.get("openings"),
                desc = form.get("desc"),
                company_name = form.get("company_name"),
                author = form.get("author"),
                author_email = form.get("author_email"),
                eligibility = form.get("eligibility"),
                last_date = form.get("last_date"),
                website = form.get("website"),
                post_type = form.get("job_type"),
                company_logo_link = result['items'][0]['link'],
                status = 2
            )
        p.save()
        messages.add_message(request, messages.SUCCESS,"Job/Internship Post sent for review")
        return redirect('post-home')
    else:
        return render(request, 'post/job_post_form.html')

class HackthonPostDetailView(DetailView):
    model = Hackathon
    slug_field = 'hackathon_type'
    slug_url_kwarg = 'hackathon_type'
    template_name = 'post/hackathonPost.html'    # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    # post = Employment.objects.get(current.id)
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.views+=1
        obj.save()
        return obj

def newHackathontPost(request):
    if request.method == 'POST':
        form = request.POST.dict()
        print(form)
        company_logo = 'logo '+form.get("organizer") + form.get("title")
        # print(company_logo)
        result = resource.list(q=company_logo, cx='009788653011454125862:nwy48iuc4ai', searchType='image').execute()
        p = Hackathon(
                title=form.get("title"),
                team_size = form.get("team_size"),
                desc = form.get("desc"),
                organizer = form.get("organizer"),
                author = form.get("author"),
                author_email = form.get("author_email"),
                eligibility = form.get("eligibility"),
                start_date = form.get("start_date"),
                end_date = form.get("end_date"),
                website = form.get("website"),
                organizer_logo = result['items'][0]['link'],
                status = 2,
                last_date = form.get("last_date")
            )
        p.save()
        messages.add_message(request, messages.SUCCESS,"Hackathon Details sent for review.")
        return redirect('post-home')
    else:
        return render(request, 'post/hackathon_post_form.html')

def jobPost(request):
    context ={
        'posts':'posts'
    }
    return render(request, 'post/jobPost.html', context)
