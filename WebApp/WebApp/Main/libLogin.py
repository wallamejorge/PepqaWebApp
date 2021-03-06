# -*- encoding: utf-8 -*-

#----------------------------------------------------------------------------- #	
#---  Title   : Login Python Functions 
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
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- Python Libs  ------------------------------------------------------------ #
import datetime
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #	
#---                                END                                        #
#----------------------------------------------------------------------------- #

###############################################################################








###############################################################################

#----------------------------------------------------------------------------- #	
#---     Login's Function : Render Login HTML Template
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- LoginApp ---------------------------------------------------------------- #
def LoginProcess(request):
	vOut = {}
	return vOut
#----------------------------------------------------------------------------- #

#----------------------------------------------------------------------------- #
#--- LoginApp ---------------------------------------------------------------- #
def AuthProcess(request):
	vOut = {}
	
	rEmail = request.GET['usr_name']
	rpassword = request.GET['usr_password']
	
	Usuario = User.objects.get(user_email=rEmail)
	
	pEmail=getattr(Usuario,'user_email')
	pPassword=getattr(Usuario,'user_password')
	
	if (rEmail == pEmail ):		
		vOut = {'Status':'Logged Succesfull','User':rEmail}
	else:
		vOut = {'Status':'Invalid User-Password'}
		
	return vOut
#----------------------------------------------------------------------------- #

#--------------------------------------------------------------------------------- #
#--- setCookieApp ---------------------------------------------------------------- #
def setCookieProcess(request):
	if 'user_email' in request.GET and request.GET['user_email']:
		response = HttpResponseRedirect('/getCookie/')
		response.set_cookie("CurrentUser",request.GET['user_email'])
	return response
#--------------------------------------------------------------------------------- #
#--- GetCookieApp ---------------------------------------------------------------- #	
def getCookieProcess(request):
	if "CurrentUser" in request.COOKIES:
		vUser = request.COOKIES['CurrentUser']
	else:
		vUser = "NaN" 
	return vUser

###############################################################################




