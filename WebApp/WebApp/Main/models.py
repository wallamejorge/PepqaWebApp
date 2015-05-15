from django.db import models



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  					Users
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# -------------------------------------------------------------------------------------- #
# --- USER : Modelo de base de datos para cada usuario  -------------------------------- #
# -------------------------------------------------------------------------------------- #
class User(models.Model):

    #Atributos de cada usuario

	# ----------------------------------------------- #
	# --- Profile Atributes ------------------------- #
	# ----------------------------------------------- #
	user_email     =  models.CharField(max_length=200)
	user_password  =  models.CharField(max_length=200)
	user_firstname =  models.CharField(max_length=200)
	user_lastname  =  models.CharField(max_length=200)

	# ----------------------------------------------- #
	# --- Personal Atributes ------------------------ #
	# ----------------------------------------------- #
	user_age       =  models.CharField(max_length=200)
	user_gender    =  models.CharField(max_length=200)
	user_country   =  models.CharField(max_length=200)
	user_language  =  models.CharField(max_length=200)

	# ----------------------------------------------- #
	# --- Professional Atributes -------------------- #
	# ----------------------------------------------- #
	user_category  =  models.CharField(max_length=200)
	user_company   =  models.CharField(max_length=200)
	user_studies   =  models.CharField(max_length=200)
	user_topics    =  models.CharField(max_length=200)	
	
	# ----------------------------------------------- #
	# --- Social Atributes -------------------------- #
	# ----------------------------------------------- #
	user_photourl  =  models.CharField(max_length=200)
	user_cvurl     =  models.CharField(max_length=200)
	user_abstract  =  models.CharField(max_length=200)
	user_fburl       =  models.CharField(max_length=200)
	user_twitterurl  =  models.CharField(max_length=200)
	user_linkedlnurl  =  models.CharField(max_length=200)

	# ----------------------------------------------- #
	# --- English Skills Atributes ------------------ #
	# ----------------------------------------------- # 
	user_englishReading   =  models.CharField(max_length=200)
	user_englishWriting   =  models.CharField(max_length=200)
	user_englishListening =  models.CharField(max_length=200)
	user_englishSpeaking  =  models.CharField(max_length=200)
	
	# ----------------------------------------------- #
	# --- Professional Skills Atributes ------------- #
	# ----------------------------------------------- # 
	user_skillCommunication   =   models.CharField(max_length=200)
	user_skillTeamwork        =   models.CharField(max_length=200)
	user_skillInitiative      =   models.CharField(max_length=200)
	user_skillProblemSolving  =   models.CharField(max_length=200)
	user_skillFlexibility     =   models.CharField(max_length=200)	
	user_skillComputer        =   models.CharField(max_length=200)
	user_skillTechnical       =   models.CharField(max_length=200)
	user_skillLeadership      =   models.CharField(max_length=200)

	def __str__(self):
		return self.user_email


# -------------------------------------------------------------------------------------- #
# --- Friendship : Modelo de base de datos que relaciona User's ------------------------ #
# -------------------------------------------------------------------------------------- #
class Friendship(models.Model):

	friendship_from =  models.CharField(max_length=200)
	friendship_to =  models.CharField(max_length=200)

	def __str__(self):
		return self.friendship_from

class FriendshipRequested(models.Model):

	friendship_owner =  models.CharField(max_length=200)
	friendship_requester =  models.CharField(max_length=200)

	def __str__(self):
		return self.friendship_owner


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  					Groups
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# -------------------------------------------------------------------------------------- #
# --- Group : Modelo de base de datos que identifica un Group  ------------------------- #
# -------------------------------------------------------------------------------------- #
class Group(models.Model):

	group_name =  models.CharField(max_length=200)
	grou_admin =  models.CharField(max_length=200)

	def __str__(self):
		return self.group_name

# -------------------------------------------------------------------------------------- #
# --- GroupMembers: Modelo de base de datos que relaciona Groups con User's ------------ #
# -------------------------------------------------------------------------------------- #
class GroupMembers(models.Model):
	
	groupmembers_groupname =  models.CharField(max_length=200)
	groupmembers_groupmember =  models.CharField(max_length=200)

	def __str__(self):
		return self.groupmembers_groupname



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  					Articles
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# -------------------------------------------------------------------------------------- #
# --- Article: Modelo de base de datos que identifica un Article ----------------------- #
# -------------------------------------------------------------------------------------- #
class  Article(models.Model):

	article_name =  models.CharField(max_length=200)
	article_published =  models.CharField(max_length=200)
	article_date = models.CharField(max_length=200)
	article_abstract = models.CharField(max_length=5000)
	article_topic = models.CharField(max_length=200)

	def __str__(self):
		return self.article_name

# -------------------------------------------------------------------------------------- #
# --- ArticleAuthors: Modelo de base de datos que relaciona Articles con User's -------- #
# -------------------------------------------------------------------------------------- #
class ArticleAuthors(models.Model):
	
	articleauthors_articlename =  models.CharField(max_length=200)
	articleauthors_articleauthor =  models.CharField(max_length=200)

	def __str__(self):
		return self.articleauthors_articlename

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  					Offers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# -------------------------------------------------------------------------------------- #
# --- Offer: Modelo de base de datos que identifica cada Offer ------------------------ #
# -------------------------------------------------------------------------------------- #
class Offer(models.Model):

	offer_name =  models.CharField(max_length=200)
	offer_owner = models.CharField(max_length=200)
	offer_abstract =  models.CharField(max_length=5000)
	offer_deadline = models.CharField(max_length=5000)

	def __str__(self):
		return self.offer_name

# -------------------------------------------------------------------------------------- #
# --- OfferAcepted: Modelo de base de datos que relaciona Offer con User's ------------- #
# -------------------------------------------------------------------------------------- #
class OfferAccepted(models.Model):

	offer_name =  models.CharField(max_length=200)
	offer_user = models.CharField(max_length=200)

	def __str__(self):
		return self.offer_name

class OfferRequested(models.Model):

	offer_name =  models.CharField(max_length=200)
	offer_user = models.CharField(max_length=200)

	def __str__(self):
		return self.offer_name


