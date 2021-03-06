from django.urls import path, include
from backend import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('users', views.UserViewSet)
#router.register('comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', views.Search.as_view()),
    #search user by username
    path('users/<int:user_id>/follow/', views.FollowUser.as_view()),
    path('users/<int:user_id>/unfollow/', views.UnFollowUser.as_view()),
    path('posts/<int:pk>/comments/', views.CommentList.as_view()),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/',
         views.CommentDetail.as_view()),
    path('posts/<int:post_id>/likes/', views.LikePost.as_view()),
    path('posts/<int:post_id>/unlikes/', views.UnLikePost.as_view()),
]
