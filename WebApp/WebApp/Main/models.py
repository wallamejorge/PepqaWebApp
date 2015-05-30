from django.db import models



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  Main Class's
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
# --- Offer: Modelo de base de datos que identifica cada Offer ------------------------ #
# -------------------------------------------------------------------------------------- #
class Offer(models.Model):

	offer_name =  models.CharField(max_length=200)
	offer_owner = models.CharField(max_length=200)
	offer_photourl = models.CharField(max_length=200)
	offer_abstract =  models.CharField(max_length=5000)
	offer_deadline = models.CharField(max_length=200)
	offer_date = models.CharField(max_length=200)
	def __str__(self):
		return self.offer_name


# -------------------------------------------------------------------------------------- #
# --- Group : Modelo de base de datos que identifica un Group  ------------------------- #
# -------------------------------------------------------------------------------------- #
class Group(models.Model):

	group_name =  models.CharField(max_length=200)
	group_owner =  models.CharField(max_length=200)
	group_photourl =  models.CharField(max_length=200)
	group_abstract =  models.CharField(max_length=200)
	def __str__(self):
		return self.group_name

# -------------------------------------------------------------------------------------- #
# --- Article: Modelo de base de datos que identifica un Article ----------------------- #
# -------------------------------------------------------------------------------------- #
class  Article(models.Model):

	article_name =  models.CharField(max_length=200)
	article_published =  models.CharField(max_length=200)
	article_date = models.CharField(max_length=200)
	article_url = models.CharField(max_length=200)
	article_abstract = models.CharField(max_length=5000)
	def __str__(self):
		return self.article_name

# -------------------------------------------------------------------------------------- #
# --- Ads: Modelo de base de datos que identifica un Advertisement  -------------------- #
# -------------------------------------------------------------------------------------- #
class  Ad(models.Model):

	ad_name =  models.CharField(max_length=200)
	ad_owner =  models.CharField(max_length=200)
	ad_photourl =  models.CharField(max_length=200)
	ad_link = models.CharField(max_length=5000)
	ad_abstract = models.CharField(max_length=5000)
	def __str__(self):
		return self.ad_name

# -------------------------------------------------------------------------------------- #
# --- Topics: Modelo de base de datos que identifica un Topics      -------------------- #
# -------------------------------------------------------------------------------------- #
class  Topic(models.Model):

	topic_name =  models.CharField(max_length=200)
	topic_abstract =  models.CharField(max_length=5000)
	ad_photourl =  models.CharField(max_length=200)
	def __str__(self):
		return self.topic_name

# -------------------------------------------------------------------------------------- #
# --- Ideas: Modelo de base de datos que identifica una Idea      -------------------- #
# -------------------------------------------------------------------------------------- #
class  Idea(models.Model):

	idea_name =  models.CharField(max_length=200)
	idea_owner =  models.CharField(max_length=200)
	idea_photourl = models.CharField(max_length=200)
	idea_abstract =  models.CharField(max_length=5000)
	def __str__(self):
		return self.idea_name

# -------------------------------------------------------------------------------------- #
# --- Comments: Modelo de base de datos que identifica un Comments  -------------------- #
# -------------------------------------------------------------------------------------- #
class  Comment(models.Model):

	comment_name =  models.CharField(max_length=200)
	comment_owner =  models.CharField(max_length=200)
	comment_group =  models.CharField(max_length=200)
	comment_abstract =  models.CharField(max_length=5000)

	def __str__(self):
		return self.comment_name
		
		



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#  Relationships Class's
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
		
		
		
# -------------------------------------------------------------------------------------- #
# --- Friendship : Modelo de base de datos que relaciona User's ------------------------ #
# -------------------------------------------------------------------------------------- #
class Friendship(models.Model):

	friendship_from =  models.CharField(max_length=200)
	friendship_to =  models.CharField(max_length=200)
	friendship_date=  models.CharField(max_length=200)
	friendship_level =  models.CharField(max_length=200)
	def __str__(self):
		return self.friendship_from
		
class FriendshipRequest(models.Model):

	friendshiprequest_from =  models.CharField(max_length=200)
	friendshiprequest_to =  models.CharField(max_length=200)
	friendshiprequest_date=  models.CharField(max_length=200)
	def __str__(self):
		return self.friendshiprequest_from


# -------------------------------------------------------------------------------------- #
# --- GroupMembership: Modelo de base de datos que relaciona Groups con User's --------- #
# -------------------------------------------------------------------------------------- #
class GroupMembership(models.Model):
	
	groupmembership_name =  models.CharField(max_length=200)
	groupmembership_user =  models.CharField(max_length=200)
	groupmembership_date =  models.CharField(max_length=200)
	def __str__(self):
		return self.groupmembership_name

class GroupMembershipRequest(models.Model):
	
	groupmembershiprequest_name =  models.CharField(max_length=200)
	groupmembershiprequest_from =  models.CharField(max_length=200)
	groupmembershiprequest_date =  models.CharField(max_length=200)
	def __str__(self):
		return self.groupmembershiprequest_name



# -------------------------------------------------------------------------------------- #
# --- Offer: Modelo de base de datos que relaciona  Offers con Users  ------------------ #
# -------------------------------------------------------------------------------------- #
class OfferAssigned(models.Model):
	
	offerassigned_name =  models.CharField(max_length=200)
	offerassigned_user =  models.CharField(max_length=200)
	offerassigned_date =  models.CharField(max_length=200)
	def __str__(self):
		return self.offerassigned_name

class OfferRequest(models.Model):
	
	groupmembershiprequest_name =  models.CharField(max_length=200)
	groupmembershiprequest_from =  models.CharField(max_length=200)
	groupmembershiprequest_date =  models.CharField(max_length=200)
	groupmembershiprequest_comment =  models.CharField(max_length=5000)
	groupmembershiprequest_status =  models.CharField(max_length=200)
	def __str__(self):
		return self.groupmembershiprequest_name


# -------------------------------------------------------------------------------------- #
# --- ArticleAuthors: Modelo de base de datos que relaciona Articles con User's -------- #
# -------------------------------------------------------------------------------------- #
class ArticleAuthor(models.Model):
	
	articleauthor_articlename =  models.CharField(max_length=200)
	articleauthor_articleauthor =  models.CharField(max_length=200)
	def __str__(self):
		return self.articleauthors_articlename



# -------------------------------------------------------------------------------------- #
# --- Files : Subir Archivos/Fotos  ---------------------------------------------------- #
# -------------------------------------------------------------------------------------- #
class Imagen(models.Model):
	model_name = models.CharField(max_length=200)
	model_pic = models.ImageField(upload_to = 'Photos/', default = 'Photos/no-image.jpg')



