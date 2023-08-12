from django.urls import path
from . import views


urlpatterns=[
    path('', views.PostListCreateAPIView.as_view(), name="post-list"),
    path('<int:pk>/update/', views.PostUpdateAPIView.as_view(), name ="post-edit"),
    path('<int:pk>/delete/', views.PostDestroyAPIView.as_view()),
    path('<int:pk>/', views.PostDetailAPIView.as_view(), name="post-detail"),
]



