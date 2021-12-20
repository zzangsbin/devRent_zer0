from django.contrib import admin
from .models import Post # 이 파일에 모델스 파일 찾아서 post 갖고 등록해줘
# Register your models here.
admin.site.register(Post) #변경사항 저항