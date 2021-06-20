from django.contrib import admin
from user.models import Address, Comment, CustomerUser, ReplyComment
# Register your models here.
admin.site.register(CustomerUser)
admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(ReplyComment)