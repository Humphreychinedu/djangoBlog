from django.conf.urls import url
from .views import (
    UserCreateAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name="register"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    # url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name="thread"),
    # # url(r'^(?P<pk>\d+)/edit/$', CommentEditAPIView.as_view(), name="edit"),
    # #url(r'^(?P<id>\d+)/delete/$', comment_delete, name="delete" ),
]