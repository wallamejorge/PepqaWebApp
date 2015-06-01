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
#---     End of Import Module 
#----------------------------------------------------------------------------- #


























#----------------------------------------------------------------------------- #	
#---     Login & Auth Function 
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Login App --------------------------------------------------------------- #
def LoginApp(request):
	fp = open(PATH_SITE+PATH_PAGES+'Login.html')
	page = Template(fp.read())
	fp.close()	
	Data = LoginProcess(request)
	html=page.render(Context(Data))
	return HttpResponse(html)
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Auth App ---------------------------------------------------------------- #
def AuthenticationApp(request):
	if 'usr_name' in request.GET and request.GET['usr_name']:
		vStatus = AuthProcess(request)
		if (vStatus['Status'] == 'Logged Succesfull'):
			qUrl = '/setCookie/?user_email='+vStatus['User']
			
			return HttpResponseRedirect(qUrl)
		else:
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({'Message':vStatus['Status']}))
			return HttpResponse(html)
	else:
		fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context({'Message':'Input not valid'}))
		return HttpResponse(html)
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- SetCookie App --------------------------------------------------------------- #
def setCookie(request):
	html = setCookieProcess(request)
	return html
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
def getCookie(request):
	vUser = getCookieProcess(request)
	if vUser == "NaN":
		fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context({'Message':'Login and Athentication Process'}))
		return HttpResponse(html)
	else:
		return HttpResponseRedirect('/StartPageApp/?')
#----------------------------------------------------------------------------- #
#----------------------------------------------------------------------------- #	
#----------------------------------------------------------------------------- #














#----------------------------------------------------------------------------- #	
#---     Admin & Dashboard Functions 
#----------------------------------------------------------------------------- #


#----------------------------------------------------------------------------- #
#--- AdminDashboard App ------------------------------------------------------ #
def AdminDashboard(request):
	fp =open(PATH_SITE+PATH_PAGES+'AdminDashboard.html')
	page = Template(fp.read())
	fp.close()	
	Data = {'usersList':User.objects.all(),
			'groupsList':Group.objects.all(),
			'offersList':Offer.objects.all(),
			'friendsList':Friendship.objects.all(),
			'articlesList':Article.objects.all()
			}
	html = page.render(Context(Data))
	return HttpResponse(html)
#----------------------------------------------------------------------------- #


#----------------------------------------------------------------------------- #
#--- AdminSaveApp ------------------------------------------------------------ #
def AdminSave(request):
	if 'usr_email' in request.GET and request.GET['usr_email']:
		try :
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
			html=t.render(Context({'Message':'Thats email does not exist'}))
			return HttpResponse(html)
	else:
		if 'off_name' in request.GET and request.GET['off_name']:
			try :
				Oferta = Offer.objects.get(offer_name=request.GET['off_name'])
				Oferta.offer_name = request.GET['off_name']
				Oferta.offer_owner = request.GET['off_owner']
				Oferta.offer_photourl = request.GET['off_photourl']
				Oferta.offer_date = request.GET['off_date']
				Oferta.offer_deadline = request.GET['off_deadline']	
				Oferta.offer_abstract = request.GET['off_abstract']		
				Oferta.save()
				return HttpResponseRedirect('/Dash/')
			except:
				fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
				t= Template(fp.read())
				fp.close()				
				html=t.render(Context({'Message':'Thats offers does not exist'}))
				return HttpResponse(html)
		else:
			if 'grp_name' in request.GET and request.GET['grp_name']:
				try :
					Grupo = Group.objects.get(group_name=request.GET['grp_name'])
					Grupo.group_name = request.GET['grp_name']
					Grupo.group_owner = request.GET['grp_owner']
					Grupo.group_photourl = request.GET['grp_photourl']
					Grupo.group_date = request.GET['grp_date']
					Grupo.group_abstract = request.GET['grp_abstract']		
					Grupo.save()
					return HttpResponseRedirect('/Dash/')
				except:
					fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
					t= Template(fp.read())
					fp.close()				
					html=t.render(Context({'Message':'Thats group does not exist'}))
					return HttpResponse(html)
		
#----------------------------------------------------------------------------- #


















#----------------------------------------------------------------------------- #
#--- AdminSaveApp ----------------------------------------------------------- #
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
#----------------------------------------------------------------------------- #
#--- AdminOfferRemove -------------------------------------------------------- #
def AdminOfferRemove(request):
	if 'off_name' in request.GET and request.GET['off_name']:
		try :
			Oferta = Offer.objects.get(offer_name=request.GET['off_name'])
			Oferta.delete()
			return HttpResponseRedirect('/Dash/')
		except:
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({'Message':'Thats offer does not existe, please check up'}))
			return HttpResponse(html)
#----------------------------------------------------------------------------- #
#----------------------------------------------------------------------------- #
#--- AdminOfferRemove -------------------------------------------------------- #
def AdminGroupRemove(request):
	if 'grp_name' in request.GET and request.GET['grp_name']:
		try :
			Grupo = Group.objects.get(offer_name=request.GET['grp_name'])
			Grupo.delete()
			return HttpResponseRedirect('/Dash/')
		except:
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({'Message':'Thats group does not existe, please check up'}))
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
#----------------------------------------------------------------------------- #
#--- AdminNewOffer App ------------------------------------------------------ #
def AdminNewOffer(request):
	try :
		name = request.GET['off_name']
		Oferta=Offer.objects.create(offer_name=name)
		Oferta.save()
		return HttpResponseRedirect('/Dash/')
	except:
		fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context({'Message':'Thats email does not exist'}))
		return HttpResponse(html)
#----------------------------------------------------------------------------- #
#----------------------------------------------------------------------------- #
#--- AdminNewGroup App ------------------------------------------------------- #
def AdminNewGroup(request):
	try :
		name = request.GET['grp_name']
		Grupo=Group.objects.create(group_name=name)
		Grupo.save()
		return HttpResponseRedirect('/Dash/')
	except:
		fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context({'Message':'Thats Group Name are invalid'}))
		return HttpResponse(html)
#----------------------------------------------------------------------------- #
#----------------------------------------------------------------------------- #
#--- AdminNewArticle App ----------------------------------------------------- #
def AdminNewArticle(request):
	try :
		name = request.GET['art_name']
		Articulo=Article.objects.create(article_name=name)
		Articulo.save()
		return HttpResponseRedirect('/Dash/')
	except:
		fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context({'Message':'Thats Article/Project Name are invalid'}))
		return HttpResponse(html)
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- AdminNewFrienship App --------------------------------------------------- #
def AdminNewFriendship(request):
	try :
		UserFrom = request.GET['FromFriend']
		ToFrom = request.GET['ToFriend']
		FriendshipFrom =Friendship.objects.create(friendship_from=UserFrom,friendship_to=ToFrom)
		FriendshipFrom.save()
		UserFrom = request.GET['ToFriend']
		ToFrom = request.GET['FromFriend']
		FriendshipFrom =Friendship.objects.create(friendship_from=UserFrom,friendship_to=ToFrom)
		FriendshipFrom.save()
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
	if 'CurrentUser' in request.COOKIES:
		try :
			usuario=User.objects.get(user_email=request.COOKIES['CurrentUser'])
			email=getattr(usuario,'user_email')
		except :
			fp=open(PATH_SITE+PATH_PAGES+'PopUp.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({'Message':'User Does not Exist'}))
			return HttpResponse(html)
		
		fp=open(PATH_SITE+PATH_PAGES+'StartPage.html')
		t= Template(fp.read())
		fp.close()				
		html=t.render(Context(getUserData(usuario)))
		return HttpResponse(html)
	else:
		return HttpResponse('Ingrese algo por el amor de  Dios!')





	
	


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
#----------------------------------------------------------------------------- #
#--- Offers App  ------------------------------------------------------------ #
def Offers(request):
	fp=open(PATH_SITE+PATH_PAGES+'Offers.html')
	page= Template(fp.read())
	fp.close()	
	html=page.render(Context({'offersList':Offer.objects.all()}))
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


