from django.shortcuts import render, redirect
from post.importData import posts
from .models import Employment
from django.views.generic import ListView, DetailView
from django.contrib import messages
from apiclient.discovery import build
api_key = "AIzaSyDJeSsqZU2ANJcMq1rACgfMqy86iXEgHW8"
resource = build("customsearch", 'v1', developerKey=api_key).cse()

def home(request):

    context = {
        'all_posts' : posts,
        'posts':Employment.objects.all().order_by('-id')
    }
    # p = Employment(
    #         role="Software Eng",
    #         desc = "This is from the home function",
    #         company_name = 'DELL',
    #         salary = '4-8',
    #         # eligibility = 'XII passed',
    #         # last_date = "2020-03-19 04:21:35",
    #         # openings = 4,
    #         # start_date = "2020-03-19 04:21:35",
    #         website = "heythere.com",
    #         # post_type = form.get("password"),
    #         # company_logo_link = result['items'][0]['link']
    #     )
    # p.save()
    # print(p)
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

def newEmploymentPost(request):
    if request.method == 'POST':
        form = request.POST.dict()
        print(form)
        # print(form.get("date"))
        # print(form.get("from"))
        # print(form.get("to"))
        print(form.get("eligibility"))
        # company_logo = 'logo '+form.get("company_name")
        # print(company_logo)
        # result = resource.list(q=company_logo, cx='009788653011454125862:nwy48iuc4ai', searchType='image').execute()
        # p = Employment(
        #         title=form.get("email"),
        #         content = form.get("email"),
        #         date_posted = "2020-03-19 04:21:35",
        #         author = form.get("email"),
        #         company = 'DELL',
        #         ctc = '4-8',
        #         eligibility = 'XII passed',
        #         end_date = "2020-03-19 04:21:35",
        #         experience = 5,
        #         openings = 4,
        #         start_date = "2020-03-19 04:21:35",
        #         website = "heythere.com",
        #         post_type = form.get("password"),
        #         company_logo_link = result['items'][0]['link']
        #     )
        # p.save()
        messages.add_message(request, messages.SUCCESS,form.get("eligibility"))
        return redirect('post-home')
    else:
        return render(request, 'post/job_post_form.html')


def jobPost(request):
    context ={
        'posts':'posts'
    }
    return render(request, 'post/jobPost.html', context)
