from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import sqlite3
from .models import File


@login_required
def deleteView(request):
	f = File.objects.get(pk=request.POST.get('id'))
	f.delete()
	return redirect('/')
	

@login_required
def downloadView(request, fileid):
	f = File.objects.get(pk=fileid)

	filename = f.data.name.split('/')[-1]
	response = HttpResponse(f.data, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename

	return response


@login_required
def addView(request):
	data = request.FILES.get('file')
	f = File(owner=request.user, data=data)
	f.save()
	return redirect('/')


@login_required
def homePageView(request):
	files = File.objects.filter(owner=request.user)
	uploads = [{'id': f.id, 'name': f.data.name.split('/')[-1]} for f in files]	
	return render(request, 'pages/index.html', {'uploads': uploads})

def phishing(request):
	return render(request, 'pages/phishing.html')
def removingimage(request):
	return render(request, 'pages/csrf.html')
def query():
	return ".%' UNION SELECT * FROM auth_user --"
def admininfoleaked(request):
	conn = sqlite3.connect('src/db.sqlite3')
	cursor = conn.cursor()
	leaked = cursor.execute("SELECT * FROM auth_user WHERE username='%s' and username LIKE '%%%s%%'" % (request.user.username, query())).fetchall()
	return HttpResponse(leaked)