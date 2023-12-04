from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    return render(request, 'Budget/project-list.html')

def project_detail(request, project_slug):
    #fetching the correct project

    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'Budget/project-detail.html', {'project': project, 'expense_list': project.expenses.all()})