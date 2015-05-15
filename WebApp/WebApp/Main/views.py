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
def demologin(request):
	nowDateVar = datetime.datetime.now()
	fp=open(PATH_SITE+PATH_PAGES+'Demo/index.html')
	page= Template(fp.read())
	fp.close()	
	html=page.render(Context({'Date':nowDateVar}))
	return HttpResponse(html)
def demostartpage(request):
	if 'username' in request.GET and request.GET['username']:
		now = datetime.datetime.now()
		usrname=request.GET['username']
		usrpass=request.GET['userpass']
		usuario=User.objects.get(user_email=usrname)
		email=getattr(usuario,'user_email')
		password=getattr(usuario,'user_password')
		if (password == usrpass) and (usrname == email) :
			
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
			myofferrquestedlist= getMyOfferAcceptedList(email);

			fp=open(PATH_SITE+PATH_PAGES+'Demo/startpage.html')
			t= Template(fp.read())
			fp.close()				
			html=t.render(Context({
					        'Email':myemail,
					        'Password':mypassword,
						'FirstName':myfirstname,
						'LastName':mylastname,
						'Age':myage,
						'Gender':mygender,
						'Country':mycountry,
						'Language':mylanguage,
						'Category':mycategory,
						'Company':mycompany,
						'Studies':mystudies,
						'Topics':mytopics,
						'Photo':myphotourl,
						'CV':mycvurl,
						'Facebook':myfburl,
						'Twitter':mytwitterurl,
						'Linkedln':mylinkedlnurl,
						'FriendsList':myfriendslist,
						'FriendsRequestList':myfriendsrequestlist,
						'GroupsList':mygroupslist,
						'OfferList':myofferlist,
						'OfferRequestList':myofferrquestedlist,
						}))
			return HttpResponse(html)
		else:
			var = u'Usuario/Contraseña invalida'
			return HttpResponse(var)
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
			html=t.render(Context({
					       'Name':username,
					       'profile_photo':profile_photo,
					       'Pass':userpass,
					       'FirstName':userfirst_name,
					       'LastName':userlast_name,
					       'Age':userage,
					       'Occupation':useruseroccupation,
					       'Company':usercompany,
					       'Charge':usercharge,
					       'List':userlist,
					       'SKILL1':'English',
					       'SKILL2':'Programming',
					       'SKILL3':'Managment Skills',
					       'SKILL4':'Human Resources'
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

def getMyFriendsList(email):
	OwnerList = Friendship.objects.filter(friendship_from=email)
	friends = []
	for fi in OwnerList:
    		friends.append(fi.friendship_to)
	return friends

def getMyFriendsRequestList(email):
	OwnerList = FriendshipRequested.objects.filter(friendship_owner=email)
	friends = []
	for fi in OwnerList:
    		friends.append(fi.friendship_requester)
	return friends


def getMyGroupsList(email):
	MyGroups = GroupMembers.objects.filter(groupmembers_groupmember=email)
	groups= []
	for fi in MyGroups:
    		groups.append(fi.groupmembers_groupname)
	return groups


def getMyOffersList(email):
	MyOffers = Offer.objects.filter(offer_owner=email)
	offers= []
	for fi in MyOffers:
    		offers.append(fi.offer_name)
	return offers


def getMyOfferAcceptedList(email):
	MyOffers = Offer.objects.filter(offer_owner=email)
	offers= []
	for fi in MyOffers:
    		offers.append(fi.offer_name)
	return offers



def getMyArticleAuthorsList(email):
	MyArticles = ArticleAuthors.objects.filter(articleauthors_articleauthor=email)
	articles= []
	for fi in MyArticles:
    		articles.append(fi.articleauthors_articlename )
	return articles


