from django.db import models


class User(models.Model):

	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	age = models.CharField(max_length=3)

	gender = models.CharField(max_length=20)
	
	country =  models.CharField(max_length=200)
	occupation =  models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	charge = models.CharField(max_length=200)

	studies = models.CharField(max_length=200)

	topics =  models.CharField(max_length=800)

	def __str__(self):
		return self.email



class Friendship(models.Model):

	user1 =  models.CharField(max_length=200)
	user2 =  models.CharField(max_length=200)

	def __str__(self):
		return self.user1



