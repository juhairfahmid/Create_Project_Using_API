# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from .views import   BlogList , CrudBlog
# #contetn_list, content_detail ,All_content, Crud_content
# urlpatterns = [
#     # path('contents/', contetn_list),
#     # path('content_detail/<int:pk>', content_detail),
#     # path('all-blog/', All_content.as_view()),
#     # path('detail-blog/<int:pk>', Crud_content.as_view()),
#     # path('blog-list/', BlogList.as_view()),
#     # path('blog-detail/<int:pk>', CrudBlog.as_view())

# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet

router = DefaultRouter()
router.register(r'content', ContentViewSet, basename="content")

urlpatterns = [
    path('', include(router.urls)),
]