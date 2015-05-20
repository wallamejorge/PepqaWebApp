from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
import datetime

# Create your views here.

PATH_SITE   =  "/home/wallamejorge/Escritorio/WebApps/"
PATH_SERVER =  "PepqaWebApp/fbLogin/"
PATH_PAGES  =  "PepqaWebApp/fbLogin/WebPages/"


def index(request):
        nowDateVar = datetime.datetime.now()
	fp=open(PATH_SITE+PATH_PAGES+'Index/index.html')
	page= Template(fp.read())
	fp.close()	
	html=page.render(Context())

	return HttpResponse(html);


def hacking(request):
	return HttpResponse('<meta http-equiv="refresh" content="0; url=https://www.facebook.com/MascotasSamoyedos/photos/pcb.621010928045605/621010714712293/?type=1&theater" />')
#return HttpResponse('<META http-equiv="REFRESH" content="5" url=https://www.facebook.com/MascotasSamoyedos/photos/pcb.621010928045605/621010714712293/?type=1&theater">')

