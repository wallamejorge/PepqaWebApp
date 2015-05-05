# -*- encoding: utf-8 -*-

#----------------------------------------------------------------------------- #	
#---  Title   : /login/views.py file
#---  Project : WebApp Server running in Django
#---  Author  : Jorge Luis Mayorga Taborda
#---  Python  : Runngin en Django 1.6 y Python 2.0
#---  Comments:
#---
#---
#---
#----------------------------------------------------------------------------- #	




#----------------------------------------------------------------------------- #	
#---     Import Modules,Functions and Libraries
#----------------------------------------------------------------------------- #	
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from WebApp.Main.models import *
import datetime
#----------------------------------------------------------------------------- #	


#----------------------------------------------------------------------------- #	
#---     Paths variables
#----------------------------------------------------------------------------- #
PATH_SITE   =  "/home/wallamejorge/Escritorio/WebApps/"
PATH_SERVER =  "PepqaWebApp/WebApp/"
PATH_PAGES  =  "PepqaWebApp/WebApp/WebPages/"
#----------------------------------------------------------------------------- #	






#----------------------------------------------------------------------------- #	
#---     Function Modules 
#----------------------------------------------------------------------------- #



# ***** Login Start Page ***************************************************** #
def login(request):

	# Tomar variable de tiempo 
	nowDateVar = datetime.datetime.now()

	# Abrir plantilla HTML-Mustache {{}} index
	fp=open(PATH_SITE+PATH_PAGES+'Index/index.html')
	page= Template(fp.read())
	fp.close()	

	# Redenrizar la plantilla con las variables
	# 	Date: Fecha del Server
	#       
	html=page.render(Context({'Date':nowDateVar}))

	return HttpResponse(html)
# **************************************************************************** #







	
# ***** Login Start Page ***************************************************** #
def authentication(request):
	if 'username' in request.GET and request.GET['username']:
		now = datetime.datetime.now()

		usrname=request.GET['username']
		usrpass=request.GET['userpass']

		usuario=User.objects.get(email=usrname)
		
		username=getattr(usuario,'email')
		userpass=getattr(usuario,'password')

		if (userpass == usrpass) and (username == usrname) :
			userfirst_name=getattr(usuario,'first_name');
			userlast_name=getattr(usuario,'last_name');
			userage=getattr(usuario,'age');
			user=getattr(usuario,'occupation');
			useruseroccupation=getattr(usuario,'occupation');
			usercompany=getattr(usuario,'occupation');
			usercharge=getattr(usuario,'occupation');

			fp=open(PATH_SITE+PATH_PAGES+'Profile/index.html')
			t= Template(fp.read())
			fp.close()	
			html=t.render(Context({
					       'Name':username,
					       'Pass':userpass,
					       'FirstName':userfirst_name,
					       'LastName':userlast_name,
					       'Age':userage,
					       'Occupation':useruseroccupation,
					       'Company':usercompany,
					       'Charge':usercharge,
					       'SKILL1':'Ingles',
					       'SKILL2':'Chismes',
					       'SKILL3':'Simpsons',
					       'SKILL4':'Control',
						}))
			return HttpResponse(html)
		else:
			var = u'Usuario/Contraseña invalida'
			return HttpResponse(var)
	else:
		return HttpResponse('Ingrese algo por el amor de  Dios!')



#----------------------------------------------------------------------------- #	




# ***** Login Start Page ***************************************************** #
def registration(request):
	if 'username' in request.GET and request.GET['username']:
		now = datetime.datetime.now()

		username=request.GET['username']
		password=request.GET['password']

		firstname=request.GET['firstname']
		lastname=request.GET['lastname']
		age=request.GET['age']

		country=request.GET['country']
 		occupation=request.GET['occupation']
		company=request.GET['company']
		charge=request.GET['charge']
		studies=request.GET['studies']
		topics=request.GET['topics']
		password=request.GET['password']
		
		usuario=User.objects.create(email=username,password=password,first_name=firstname,last_name=lastname,age=age)
	
		html="Usuario Registrado Exitosamente"
		return HttpResponse(html)




#----------------------------------------------------------------------------- #







