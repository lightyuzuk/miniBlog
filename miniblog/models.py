from django.db import models
from django.utils.encoding import force_unicode

class Blog(models.Model):
	name = models.CharField(max_length=40)
	owner = models.CharField(max_length=40)
	description = models.CharField(max_length=500)
	counts = models.IntegerField(default=1)
		
	def __unicode__(self):
		return u'%s by %s' % (self.name, self.owner) 