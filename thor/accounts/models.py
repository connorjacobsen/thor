from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		"""
		Creates and saves a User with the given email and password.
		"""
		now = timezone.now()
		if not email:
			raise ValueError('Users must have a valid email address')

		email = CustomUserManager.normalize_email(email)

		user = self.model(
			email = email,
			)
		user.set_password(password)
		is_active = True
		is_staff = False
		is_admin = False
		is_superuser = False
		last_login = now
		date_joined = now

		# if first_name:
		#	user.first_name = first_name
		# if last_name:
		#	user.last_name = last_name	

		user.save(using=self.db)
		return user

	def create_superuser(self, email, password):	
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(email, password)
		user.is_staff = True
		is_admin = True
		user.is_active = True
		user.is_superuser = True
		user.save(using = self.db)
		return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
		verbose_name = 'email address',
		max_length = 255,
		unique = True,
		db_index = True,
	)			
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	full_name = '%s %s' % (first_name, last_name)		

	is_admin = models.BooleanField('admin', default=False)
	is_active = models.BooleanField(default=True)

	objects = CustomUserManager()

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
