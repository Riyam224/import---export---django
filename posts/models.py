
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    body = models.TextField(_("body"))
    liked = models.ManyToManyField(User, related_name='liked', verbose_name=_("liked"))
    created = models.DateTimeField(_("created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return f"post pk: {self.pk}"
    @property
    def comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    body = models.TextField(_("body"))
    created = models.DateTimeField(_("created"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"comment pk:  {self.pk}"

