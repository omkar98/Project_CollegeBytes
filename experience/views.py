from django.shortcuts import render, redirect
from django.contrib import messages
from apiclient.discovery import build
from .models import Experience, Organizer, Subscriber
from django.views.generic import ListView, DetailView

api_key = "AIzaSyDJeSsqZU2ANJcMq1rACgfMqy86iXEgHW8"
resource = build("customsearch", 'v1', developerKey=api_key).cse()


def home(request):
	ids = Experience.objects.values_list('organization', flat=True).filter(status=1)
	print(ids)
	organizers = Organizer.objects.filter(pk__in=set(ids)).order_by('organization_name')
	# organizers = Organizer.objects.filter(status=1).order_by('organization_name')
	print(organizers)
	all_companies=[]
	for organizer in organizers:
		company={}
		company['id']=organizer.id
		company['name']=organizer.organization_name
		company['count']=organizer.experience_set.filter(status=1).count()
		all_companies.append(company)
	print(all_companies)
	context = {
		'posts' : all_companies
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
		user, created = Subscriber.objects.get_or_create(
			user_name = form.get("author_name"),
			user_email = form.get("author_email"),
		)
		if created:
			user.user_about = form.get("author_about")
			user.save()
		p = Experience(
				author = user,
				result_field = form.get("result_field"),
				experience_result_more = form.get("experience_result_more"),
				experience_type_field = form.get("experience_type_field"),
				organization = obj,
				organization_role = form.get("organization_role"),
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


class ExperienceListView(ListView):
	template_name = 'experience/experience-list.html'
	paginate_by = 10
	ordering = ['-experience_date_posted']
	# model = Experience
	def get_queryset(self, *args, **kwargs):
		objects = Experience.objects.filter(organization=self.kwargs['organization'])
		# objects['org_id'] = self.kwargs['organization']
		return objects

class ExperienceDetailView(DetailView):
	template_name = 'experience/experience-detail.html'
	# ordering = ['-experience_date_posted']
	# # model = Experience
	# def get_queryset(self, *args, **kwargs):
	# 	objects = Experience.objects.filter(organization=self.kwargs['organization'])
	# 	# objects['org_id'] = self.kwargs['organization']
	# 	return objects
