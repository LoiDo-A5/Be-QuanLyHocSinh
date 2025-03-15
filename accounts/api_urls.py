from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter

from accounts.api.chatroom_list import ChatRoomList
from accounts.api.friendship_api import FriendshipViewSet
from accounts.api.login_api import LoginApi
from accounts.api.me import MeApi
from accounts.api.message_list import ListMessage
from accounts.api.register_phone import RegisterPhoneApi
from accounts.api.direct_messages import DirectMessages
from accounts.api.users import UserViewSet

router = SimpleRouter()
router.register(r'friendship', FriendshipViewSet, basename='friendship')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('login/', LoginApi.as_view()),
    path('register/phone/', RegisterPhoneApi.as_view()),
    path('me/', MeApi.as_view()),
    path('rooms/', ChatRoomList.as_view(), name='rooms'),
    path('messages/', ListMessage.as_view(), name='messages'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('direct_messages/', DirectMessages.as_view(), name='direct_messages'),

]

urlpatterns += router.urls
