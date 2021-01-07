from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Course)
admin.site.register(Taken)
admin.site.register(Module)
admin.site.register(Result)
admin.site.register(Question)
admin.site.register(Answer_Sheet)
#admin.site.register(i)