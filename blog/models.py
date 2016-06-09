from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
	title = models.CharField('Title',max_length=150)
	author = models.CharField('Author', max_length=250,default='admin')
	text = models.TextField('Text')
	create_date = models.DateTimeField('Creation Date',auto_now_add=True)

	class Meta:
		verbose_name = "Manual"
		verbose_name_plural = "Manuals"
		ordering = ['-create_date']

	def __str__(self):
		return '{} {}'.format(self.title, self.create_date)

# class About(models.Model):
# 	about = models.TextField('About')

# 	class Meta:
# 		verbose_name = "About"
# 		verbose_name_plural = "About"

# 	def __str__(self):
# 		return self.about