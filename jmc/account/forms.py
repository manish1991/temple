from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from account.models import UserProfile

from django import forms
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator


GENDER_CHOICES = (
                  ('M', 'Male'),
                  ('F', 'Female'),
                )


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'},
                                                                  render_value=False))

    def clean(self):
    	user = self.authenticate_via_email()
    	if not user:
    		raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
    	else:
    		self.user = user
    	return self.cleaned_data

    def authenticate_user(self):
        return authenticate(
            username=self.user.username,
            password=self.cleaned_data['password'])

    def authenticate_via_email(self):
        """
            Authenticate user using email.
            Returns user object if authenticated else None
        """
        email = self.cleaned_data['email']
        if email:
            try:
            	user = User.objects.get(email__iexact=email)
            	if user.check_password(self.cleaned_data['password']):
            	   return user
            except ObjectDoesNotExist:
            	pass
        return None
    

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'New Password'},
                                                              render_value=False))
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 
                                                                             'Confirm New Password'},
                                                                              render_value=False))

    def clean(self):
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']
        if new_password != confirm_new_password:
            raise forms.ValidationError("Both password doesn't match. Please try again.")
        return self.cleaned_data


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))

    def clean(self):
        pass
        return self.cleaned_data


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Old Password'},
                                                              render_value=False))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'New Password'},
                                                              render_value=False))


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50,required=False,
                                 widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly':'readonly',
                                                            'placeholder': 'Email'})) 
    gender = forms.ChoiceField(choices=GENDER_CHOICES,required=False,widget=forms.Select(attrs={
                                                                        'placeholder': 'Gender'}))
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must" + \
                                                            "be entered in the format: '9999999999'. Only digits allowed.")
    phone_no = forms.CharField(validators=[phone_regex],max_length=10,required=False,widget=
                                            forms.TextInput(attrs={'placeholder': 'Phone No'}))

    @classmethod
    def populate_form(self, user_profile):
        form = EditProfileForm(
            initial={'first_name': user_profile.user.first_name,
                     'last_name': user_profile.user.last_name,
                     'email': user_profile.user.email,
                     'gender': user_profile.gender,
                     'phone_no': user_profile.phone_no,
                     })
        return form
