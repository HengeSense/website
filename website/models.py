from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
	('M', _("Male")),
	('F', _("Female"))
)

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)

	date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
	gender = models.CharField(_("Gender"), max_length=1, blank=True, null=True, choices=GENDER_CHOICES)

	receive_updates = models.BooleanField(_("Receive updates from this Web site"), default=True)

	class Meta:
		verbose_name = _("user profile")
		verbose_name_plural = _("user profiles")
		order_with_respect_to = "user"

	def __unicode__(self):
		return _("User profile for %s") % self.user.get_full_name()

def user_registered_callback(sender, user, request, **kwargs):
	UserProfile.objects.get_or_create(user=user)
user_registered.connect(user_registered_callback)
