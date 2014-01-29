from django.db import models

# Create your models here.
class User(models.Model):
  user_name = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  blog_name = models.CharField(max_length=75)
  email = models.EmailField(max_length=50)
  password_digest = models.CharField(max_length=255)
  about_blog = models.TextField(max_length=2000)
  created_at = models.DateField()
  updated_at = models.DateField()

  def __unicode__(self):
    return u"%s %s: %s %s" % (self.first_name, self.last_name, self.user_name, self.blog_name)

class Post(models.Model):
  user = models.ForeignKey(User)
  title = models.CharField(max_length=75)
  content = models.TextField(max_length=25000, null=True)
  published = models.BooleanField(default=False)
  created_at = models.DateField()
  updated_at = models.DateField()

  def __unicode__(self):
    return u"%s by %s %s" % (self.title, self.user.first_name, self.user.last_name)