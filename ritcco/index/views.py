from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from .models import Applicant
from django.core.exceptions import ValidationError
# Create your views here.

def index(request):
    save = True
    app_data = Applicant.objects.all()
    if request.method == 'POST' and request.FILES['myfile']:
        app = Applicant()
        myfile = request.FILES['myfile']
        app.cv = myfile.name
        app.name = request.POST['name']
        app.mail = request.POST['mail']
        app.phone = request.POST['mobi']
        app.exp = request.POST['expr']
        app.domain = request.POST['post']
        app.status = 'Processing'

        try:
            app.full_clean()
        except ValidationError as e:
            save = False
            return render(request, 'Process.html', {'mail': request.POST['mail'], 'phone': request.POST['mobi']})

        if(save):
            fs = FileSystemStorage()
            file = fs.save(myfile.name, myfile)
            app.save()
            return render(request, 'Process.html', {'message': 'Successful'})

    return render(request, 'index.html', {'data': app_data})
