from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
	def create_user(self, email, password):
		"""
		Creates and saves a User with the given email, first and last 
		names, and password.
		"""
		if not email:
			raise ValueError('Users must have a valid email address')

		if not password:
			raise ValueError('Users must have a valid password')

		user = self.model(
			email = MyUserManager.normalize_email(email),
			#user.set_password(password)
			)
		user.set_password(password)

		# if first_name:
		#	user.first_name = first_name
		# if last_name:
		#	user.last_name = last_name	

		user.save(using=self.db)
		return user

	def create_superuser(self, email, password):	
		"""
		Creates and saves a superuser with the given email, name, 
		and password.
		"""
		user = self.create_user(email, 
			password, 
		)
		user.is_admin = True
		user.save(using = self.db)

class CustomUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name = 'email address',
		max_length = 255,
		unique = True,
		db_index = True,
	)					
	# It may not be necessary to declare a password attribute
	# password = models.PasswordField()
	is_active = models.BooleanField(default = True)
	is_admin = models.BooleanField(default = False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __unicode__(self):
		return self.email

	# Consider editing permissions so that admin is not accessible 
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perm(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest answer: Yes, always
		return True				

	@property 
	def is_staff(self):
		"Is the user a member of staff?"
		# If the user is an admin, they are staff
		return self.is_admin
		