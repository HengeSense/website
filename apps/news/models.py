from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.comments.moderation import CommentModerator, moderator
from taggit.managers import TaggableManager

from apps.news.managers import PublishedNewsManager

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return u"%s" % self.name

	class Meta:
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")

class News(models.Model):
	user = models.ForeignKey(User)
	site = models.ManyToManyField(Site)
	title = models.CharField(max_length=255) 
	category = models.ForeignKey(Category)
	slug = models.SlugField(unique=True)
	body = models.TextField()
	published = models.BooleanField(default=False)
	comments_enabled = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	pubs_objects = PublishedNewsManager()
	tags = TaggableManager()

	def __unicode__(self):
		return u"%s" % self.title

	def get_absolute_url(self):
		return "/news/%s/" % self.slug

	class Meta:
		verbose_name = _("News")
		verbose_name_plural = _("News")
		ordering = ["-created_at"]

class NewsCommentModerator(CommentModerator):
	"""
	News comments moderator.
	The following logic applies:
	 - unauthenticated users' comments are always moderated
	   and an email is sent to the administrators
	 - respect the ``comments_enabled`` flag on news
	 - comments are closed after 30 days the news item was
	   created
	"""
	email_notification = True
	auto_close_field = "created_at"
	close_after = 30
	enable_field = "comments_enabled"

	def email(self, comment, content_object, request):
		if not request.user.is_authenticated():
			return True
		return False

	def moderate(self, comment, content_object, request):
		if not request.user.is_authenticated():
			return True
		return False
moderator.register(News, NewsCommentModerator)
