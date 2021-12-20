#포스틍레서 클라이언트에게 가는 길
from django.urls import path
from . import views #이 파일 내부에 있는 view 파일을 갖고 와줘
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
  path('list/', view= views.post_list, name='list'), #포스트 리스트로 가는 유알엘
  path('create/', view = views.post_create, name = 'create'),
  path("", views.index, name="index"),
  path('<int:pk>/update/', view=views.post_update, name='update'),
  path('<int:pk>/detail/',views.detail, name='detail'),
  path('<int:pk>/cat/', views.cat, name = 'cat')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)