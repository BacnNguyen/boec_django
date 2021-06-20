from django.urls import path
from .views import *
app_name='order'
urlpatterns = [
 
    # path('',CartView.as_view(),name="index"),
    path('addOrder/',AddOrder.as_view(),name="addOrder"),
    path('getOrder/',GetRatingOrder.as_view(),name="getOrder"),
    path('manage/',OrderManage.as_view(),name="manage"),
    path('feedback/',FeedBack.as_view(),name="feedback"),
    path('viewfeedback/',ViewFeedback.as_view(),name="viewfeedback"),
    path('checkfeedback/',CheckFeedback.as_view(),name="checkfeedback"),
    path('status/update/',UpdateStatus.as_view(),name="updateStatus"),
    path('status/<int:type>',OrderStatus.as_view(),name="status"),
    path('delete_comment/',Delete_Comment.as_view(),name="delete_comment"),
    path('ignore_comment/',Ignore_Comment.as_view(),name="ignore_comment"),
    path('reply_comment/',Reply_Comment.as_view(),name="reply_comment"),
    
]
