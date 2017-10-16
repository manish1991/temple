from django.core.validators import RegexValidator
from django.db import models
from base.models import AuditModel

# Create your models here.

class Donation(AuditModel):
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must" + \
		"be entered in the format: '9999999999'. Only digits allowed.")
	phone_no = models.CharField(validators=[phone_regex], max_length=10, blank=True)
	amount = models.FloatField(null=True, blank=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name + '-' + str(self.amount)
