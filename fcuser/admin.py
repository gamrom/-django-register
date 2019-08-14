from django.contrib import admin
from .models import Fcuser
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') #어드민페이지에서 모델필드 리스트를 쓰게 함.

admin.site.register(Fcuser, FcuserAdmin)
