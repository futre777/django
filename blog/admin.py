from django.contrib import admin
from .models import Post
from .models import Profile, Gallery, Message, Contact
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Gallery)
admin.site.register(Message)
admin.site.register(Contact)