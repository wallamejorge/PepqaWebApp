# -*- encoding: utf-8 -*-

#----------------------------------------------------------------------------- #	
#---  Title   : Authentication 
#---  Project : WebApp Server running in Django
#---  Author  : Jorge Luis Mayorga Taborda
#---  Python  : Runngin en Django 1.6 y Python 2.0
#---  Comments:
#---
#---
#---
#----------------------------------------------------------------------------- #









###############################################################################

#----------------------------------------------------------------------------- #	
#---     Import Modules,Functions and Libraries
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Django Libs ------------------------------------------------------------- #

#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Models ------------------------------------------------------------------ #
from WebApp.Main.models import *
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Aux App Libs ------------------------------------------------------------ #
from WebApp.Main.libPaths import *
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Python Libs  ------------------------------------------------------------ #
import datetime
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #	
#-------------------------------  END   -------------------------------------- # #----------------------------------------------------------------------------- #

###############################################################################





###############################################################################

#----------------------------------------------------------------------------- #	
#---     Authentication : Validate User and Pass, Active Session
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- getUserData--------------------------------------------------------- #
def getUserData(usuario):
# Single Data :
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
	# Skills Data
	myreading=getattr(usuario,'user_englishReading'); 
	mywriting=getattr(usuario,'user_englishWriting');   
	mylistening=getattr(usuario,'user_englishListening'); 
	myspeaking=getattr(usuario,'user_englishSpeaking');  
	mycommunication=getattr(usuario,'user_skillCommunication');    
	myteamwork=getattr(usuario,'user_skillTeamwork');         
	myinitiative=getattr(usuario,'user_skillInitiative');      
	myproblemsolving=getattr(usuario,'user_skillProblemSolving');   
	myflexibility=getattr(usuario,'user_skillFlexibility');      	
	mycomputer=getattr(usuario,'user_skillComputer');         
	mytechnical=getattr(usuario,'user_skillTechnical');        
	myleadership=getattr(usuario,'user_skillLeadership');     
  
# List's Data :
	# FriendsList
	myfriendslist = getMyFriendsList(myemail);
	# FriendsRequestList
	myfriendsrequestlist = getMyFriendsRequestList(myemail);
	# GroupsList
	mygroupslist = getMyGroupsList(myemail);
	# MyOffersList
	myofferlist= getMyOffersList(myemail);
	# MyOfferRequestedList
	myofferrquestedlist= getMyOfferAcceptedList(myemail);	

	contextList = {
			'user_email'     :  myemail,
			'user_password'  :  mypassword,
			'user_firstname' :  myfirstname,
			'user_lastname'  :  mylastname,
			'user_age'       :  myage,
			'user_gender'    :  mygender,
			'user_country'   :  mycountry,
			'user_language'  :  mylanguage,
			'user_category'  :  mycategory,
			'user_company'   :  mycompany,
			'user_studies'   :  mystudies,
			'user_topics'    :  mytopics,	
			'user_photourl'  :  myphotourl,
			'user_cvurl'     :  mycvurl,
			'user_abstract'  :  myabstract,
			'user_fburl'     :  myfburl,
			'user_twitterurl':  mytwitterurl,
			'user_linkedlnurl'  : 	mylinkedlnurl,
			'user_englishReading'   :  myreading,
			'user_englishWriting'   :  mywriting,
			'user_englishListening' :  mylistening,
			'user_englishSpeaking'  :  myspeaking,
			'user_skillCommunication'   :   mycommunication,
			'user_skillTeamwork'        :   myteamwork,
			'user_skillInitiative'      :  myinitiative,
			'user_skillProblemSolving'  :  myproblemsolving,
			'user_skillFlexibility'     :  myflexibility,	
			'user_skillComputer'        :  mycomputer,
			'user_skillTechnical'       :  mytechnical,
			'user_skillLeadership'      :  myleadership,
			}

	return contextList;
#----------------------------------------------------------------------------- #


def getUserDatabyRequest(request):
	puser_email = request.GET['user_email']
	puser_password = request.GET['user_password']
	puser_firstname = request.GET['user_firstname']
	puser_lastname = request.GET['user_lastname']
	puser_age= request.GET['user_age']
	puser_gender = request.GET['user_gender']
	puser_country = request.GET['user_country']
	puser_language = request.GET['user_language']
	puser_category = request.GET['user_category']
	puser_company = request.GET['user_company']
	puser_studies = request.GET['user_studies']
	puser_topics = request.GET['user_topics']
	puser_photourl = request.GET['user_photourl']
	puser_cvurl = request.GET['user_cvurl']
	puser_abstract = request.GET['user_abstract']
	puser_fburl = request.GET['user_fburl']
	puser_twitterurl = request.GET['user_twitterurl']
	puser_linkedlnurl = request.GET['user_linkedlnurl']
	puser_englishReading = request.GET['user_englishReading']
	puser_englishWriting = request.GET['user_englishWriting']
	puser_enlishListening = request.GET['user_enlishListening']
	puser_englishSpeaking = request.GET['user_englishSpeaking']
	puser_skillCommunication = request.GET['user_skillCommunication']
	puser_skillTeamwork = request.GET['user_skillTeamwork']
	puser_skillInitiative = request.GET['user_skillInitiative']
	puser_skillProblemSolving = request.GET['user_skillProblemSolving']
	puser_skillFlexibility = request.GET['user_skillFlexibility']
	puser_skillComputer = request.GET['user_skillComputer']
	puser_skillTechnical = request.GET['user_skillTechnical']
	puser_skillLeadership = request.GET['user_skillLeadership']	
	
	Usuario = User.objects.get(user_email=puser_email)
	Usuario.user_password = puser_password
	Usuario.user_firstname = puser_firstname
	Usuario.user_lastname = puser_lastname
	Usuario.save()

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


