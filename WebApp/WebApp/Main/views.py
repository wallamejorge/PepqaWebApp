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

#----------------------------------------------------------------------------- #
#--- Django Libs ------------------------------------------------------------- #
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Template,Context
from django.template.loader import get_template
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Models ------------------------------------------------------------------ #
from WebApp.Main.models import *
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Aux App Libs ------------------------------------------------------------ #
from WebApp.Main.libPaths import *
from WebApp.Main.libLogin import *
from WebApp.Main.libDatabase import *
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Python Libs  ------------------------------------------------------------ #
import datetime
#----------------------------------------------------------------------------- #	







#----------------------------------------------------------------------------- #	
#---     Function Modules 
#----------------------------------------------------------------------------- #




#----------------------------------------------------------------------------- #
#--- Login App --------------------------------------------------------------- #
def Login(request):
	# Abrir plantilla HTML-Mustache {{}} index
	fp=open(PATH_SITE+PATH_PAGES+'Login.html')
	# Abrir archivo de texto como Template
	page= Template(fp.read())
	# Cerrar archivo
	fp.close()	
	# Redenrizar la plantilla con las variables
	html=page.render(Context())
	return HttpResponse(html)
#----------------------------------------------------------------------------- #








#----------------------------------------------------------------------------- #
#--- AdminDashboard App ------------------------------------------------------ #
def AdminDashboard(request):
	# Abrir plantilla HTML-Mustache {{}} index
	fp=open(PATH_SITE+PATH_PAGES+'AdminDashboard.html')
	# Abrir archivo de texto como Template
	page= Template(fp.read())
	# Cerrar archivo
	fp.close()	
	# Redenrizar la plantilla con las variables
	html=page.render(Context({'usersList':User.objects.all(),'groupsList':Group.objects.all(),'offersList':Offer.objects.all()}))
	return HttpResponse(html)
#----------------------------------------------------------------------------- #








#----------------------------------------------------------------------------- #
#--- AdminSaveApp ------------------------------------------------------ #
def AdminSave(request):
	if 'usr_email' in request.GET and request.GET['usr_email']:
		try :
            #getUserDatabyRequest(request)
			Usuario = User.objects.get(user_email=request.GET['usr_email'])
			Usuario.user_email = request.GET['usr_email']
			Usuario.user_password = request.GET['usr_password']
			Usuario.user_firstname = request.GET['usr_firstname']
			Usuario.user_lastname = request.GET['usr_lastname']
			Usuario.user_age = request.GET['usr_age']
			Usuario.user_gender = request.GET['usr_gender']
			Usuario.user_country = request.GET['usr_country']
			Usuario.user_language = request.GET['usr_language']
			Usuario.user_category = request.GET['usr_category']
			Usuario.user_company = request.GET['usr_company']
			Usuario.user_studies = request.GET['usr_studies']
			Usuario.user_topics = request.GET['usr_topics']
			Usuario.user_photourl = request.GET['usr_photourl']
			Usuario.user_cvurl = request.GET['usr_cvurl']
			Usuario.user_abstract = request.GET['usr_abstract']
			Usuario.user_fburl = request.GET['usr_fburl']
			Usuario.user_twitterurl = request.GET['usr_twitterurl']
			Usuario.user_linkedlnurl = request.GET['usr_linkedlnurl']
			Usuario.user_englishReading = request.GET['usr_englishReading']
			Usuario.user_englishWriting = request.GET['usr_englishWriting']
			Usuario.user_englishListening = request.GET['usr_englishListening']	
			Usuario.user_skillCommunication = request.GET['usr_englishSpeaking']	
			Usuario.user_skillCommunication = request.GET['usr_skillCommunication']					
			Usuario.user_skillTeamwork = request.GET['usr_skillTeamwork']					
			Usuario.user_skillInitiative = request.GET['usr_skillInitiative']
			Usuario.user_skillProblemSolving = request.GET['usr_skillProblemSolving']
			Usuario.user_skillFlexibility = request.GET['usr_skillFlexibility']
			Usuario.user_skillComputer = request.GET['usr_skillComputer']					
			Usuario.user_skillTechnical = request.GET['usr_skillTechnical']
			Usuario.user_skillLeadership = request.GET['usr_skillLeadership']					

														
			Usuario.save()
			return HttpResponseRedirect('/Dash/')
		except:
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(request)
			return HttpResponse(html)
#----------------------------------------------------------------------------- #



#----------------------------------------------------------------------------- #
#--- AdminSaveApp ------------------------------------------------------ #
def AdminUserRemove(request):
	if 'usr_email' in request.GET and request.GET['usr_email']:
		try :
			Usuario = User.objects.get(user_email=request.GET['usr_email'])
			Usuario.delete()
			return HttpResponseRedirect('/Dash/')
		except:
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({'Message':'Thats email does not exist'}))
			return HttpResponse(html)
#----------------------------------------------------------------------------- #





















def upload(request):
	fp=open(PATH_SITE+PATH_PAGES+'Upload.html')
	t= Template(fp.read())
	fp.close()				
	html=t.render(request)
	return HttpResponse(html)

def upload_pic(request):
	try :
		if request.method == 'POST':
			form = ImageUploadForm(request.POST, request.FILES)
			if form.is_valid():
				m = Imagen.objects.get(pk=course_id)
				m.model_pic = form.cleaned_data['image']
				m.name = "DemoImage"
				m.save()
				return HttpResponse('image upload success')
			return HttpResponse('image upload success')
		else:
			return HttpResponse('image upload success')
	except:
		fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context({'Message':'No Method POST'}))
		return HttpResponse(html)



#----------------------------------------------------------------------------- #
#--- AdminNewUser App ------------------------------------------------------ #
def AdminNewUser(request):
	try :
		#getUserDatabyRequest(request)
		email = request.GET['usr_email']
		usuario=User.objects.create(user_email=email)
		usuario.save()
		return HttpResponseRedirect('/Dash/')
	except:
		fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context({'Message':'Thats email does not exist'}))
		return HttpResponse(html)
#----------------------------------------------------------------------------- #





# ***** Login Start Page ***************************************************** #
def StartPage(request):
	if 'username' in request.GET and request.GET['username']:
		now = datetime.datetime.now()
		usrname=request.GET['username']
		usrpass=request.GET['userpass']
		try :
			usuario=User.objects.get(user_email=usrname)
			email=getattr(usuario,'user_email')
			password=getattr(usuario,'user_password')
		except :
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({'Message':'User Does not Exist'}))
			return HttpResponse(html)

		if (password == usrpass) and (usrname == email) :
			fp=open(PATH_SITE+PATH_PAGES+'StartPage.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context(getUserData(usuario)))
			return HttpResponse(html)
		else:
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({'Message':'Invalid Username or Password..try again XD '}))
			return HttpResponse(html)
	else:
		return HttpResponse('Ingrese algo por el amor de  Dios!')





	
# ***** Login Start Page ***************************************************** #
def authentication(request):
	if 'username' in request.GET and request.GET['username']:
		now = datetime.datetime.now()

		usrname=request.GET['username']
		usrpass=request.GET['userpass']

		usuario=User.objects.get(user_email=usrname)
		
		email=getattr(usuario,'user_email')
		password=getattr(usuario,'user_password')

		if (password == usrpass) and (username == email) :
			
			# Profile Data
			myemail = getattr(usuario,'user_email');
			mypassword = getattr(usuario,'user_password');
			myfirstname = getattr(usuario,'user_firstname');
			mylastname  = getattr(usuario,'user_lastname');
			# Personal Data
			myage       = getattr(usuario,'user_age');
			mygender    = getattr(usuario,'user_gender');
			mycountry   = getattr(usuario,'user_country');
			mylanguage  = getattr(usuario,'user_language');
			# Professional Data
			mycategory  = getattr(usuario,'user_category');
			mycompany   = getattr(usuario,'user_company');
			mystudies   = getattr(usuario,'user_studies');
			mytopics    = getattr(usuario,'user_topics');
			# Social Data
			myphotourl  = getattr(usuario,'user_photourl');
			mycvurl     = getattr(usuario,'user_cvurl');
			myabstract  = getattr(usuario,'user_abstract');
			myfburl = getattr(usuario,'user_fburl');
			mytwitterurl  = getattr(usuario,'user_twitterurl');
			mylinkedlnurl = getattr(usuario,'user_linkedlnurl');
			
			# FriendsList
			myfriendslist = getMyFriendsList(email);
			# FriendsRequestList
			myfriendsrequestlist = getMyFriendsRequestList(email);
			# GroupsList
			mygroupslist = getMyGroupsList(email);
			# MyOffersList
			myofferlist= getMyOffersList(email);
			# MyOfferRequestedList
			myofferrquestedlist= getMyOffersRequestedList(email);
			# ArticlesList	
			myarticleslist = getMyArticlesList(email);
			# IdeasList	
			myideaslist = getMyIdeasList(email);
			# IdeasList	
			mycommentslist = getMyCommentsList(email);

			fp=open(PATH_SITE+PATH_PAGES+'Profile/index.html')
			t= Template(fp.read())
			fp.close()	
			html=t.render(Context())
			return HttpResponse(html)
		else:
			var = u'Usuario/Contraseña invalida'
			return HttpResponse(var)
	else:
		return HttpResponse('Ingrese algo por el amor de  Dios!')



#----------------------------------------------------------------------------- #	


#----------------------------------------------------------------------------- #
#--- Profile App  ------------------------------------------------------------ #
def Profile(request):
	# Abrir plantilla HTML-Mustache {{}} index
	fp=open(PATH_SITE+PATH_PAGES+'Profile.html')
	# Abrir archivo de texto como Template
	page= Template(fp.read())
	# Cerrar archivo
	fp.close()	
	# Redenrizar la plantilla con las variables
	email = request.GET['user_email']
	usuario = User.objects.get(user_email=email)
	html=page.render(Context(getUserData(usuario)))
	return HttpResponse(html)
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


