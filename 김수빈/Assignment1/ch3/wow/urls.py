"""wow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include도 잊지마라제발...
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # post '''앱'''!!!!!!으로 가는 url 등록
    path('', include('posts.urls'))
    # '' 안의 주소를 요청받으면 include 안의 주소로 가달라~~~  
    #따옴표붙이는거잊지마라진짜제발...
    # 지금 이 탭은 wow 자체의 urls를 짠거고 posts.urls를 내가 또 만들어줘야 함
    # 근데 아직 urls탭을 안 만들어줘서 그것도 내가 직접 짜야됨
    # 경로는 탐색기에 있는 것들에서 따와야됨
    # 제일 큰 (유일무이... app) posts를 말함!
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)