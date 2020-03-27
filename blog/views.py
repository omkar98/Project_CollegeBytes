from django.shortcuts import render

def home(request):
    context = {
        'test':'test',
    }
    # for item in result['items']:
    #     print(item['title'], item['link'])
    print("This is the first image " + result['items'][0]['link'])



    return render(request, 'blog/home.html', context)
