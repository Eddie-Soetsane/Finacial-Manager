from django.shortcuts import render

def project_list(request):
    return render(request, 'Budget/project-list.html')

def project_detail(request, project_slug):
    #fetching the correct project
    return render(request, 'Budget/project-detail.html')