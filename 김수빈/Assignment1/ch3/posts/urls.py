# 얘도 이름을 urls.py라고 해야됨 왜냐면 \wow urls의 22행에서 posts.urls라고 했기때문

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', view = views.post_list, name = 'list'), # 아무것도 없으므로 posts의 기본 경로가 들어옴
    path('create/', view = views.post_create, name = 'create'),
    path('<int:pk>/update/', view = views.post_update, name = 'update'),
    # view = <-이거는 사실상 안 써도 됨
    path('<int:pk>/delete/', view = views.post_delete, name= 'delete'),
    path('<int:pk>/detail/', view = views.post_detail, name= 'detail'),
]