from django import forms
from django import http
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
	"""
	Subclass for authenticating users. Extended to get a form 
	that accepts email/password logins.
	"""
	email = forms.EmailField(max_length=254)
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	def __init__(self, request=None, *args, **kwargs):
		"""
		The 'request' parameter is set for custom auth use by subclasses.
		The form data comes in via the standard 'data' kwarg. 
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)

	def get_user(self):
		return self.user_cache