from distutils import command
from django.contrib import admin
# Register your models here.
from .models import Post , Comment
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

class PostResources(resources.ModelResource):
    
    author = Field()
    liked = Field()
    created = Field()
    comments = Field()

    class Meta:
        model = Post
        fields = ('id' , 'author', 'body', 'liked', 'created')
        export_order = fields

    def dehydrate_author(self, obj):
        return str(obj.author.username)

    def dehydrate_liked(self, obj):
        data = [x.username for x in obj.liked.all()]
        users_liked = ", ".join(data)
        return users_liked

    def dehydrate_created(self , obj):
        return obj.created.strftime('%d-%m-%Y')

    def dehydrate_comments(self, obj):
        data = [x.body for x in obj.comments]
        comments  = ", ".join(data)
        return comments

   
class PostAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = PostResources

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)