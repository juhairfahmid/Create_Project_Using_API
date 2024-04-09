from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import   products , categories
#contetn_list, content_detail ,All_content, Crud_content
urlpatterns = [
    path('products/', products),
    path('categories/', categories),
    # path('content_detail/<int:pk>', content_detail),
    # path('all-blog/', All_content.as_view()),
    # path('detail-blog/<int:pk>', Crud_content.as_view()),
    # path('blog-list/', BlogList.as_view()),
    # path('blog-detail/<int:pk>', CrudBlog.as_view())

]
