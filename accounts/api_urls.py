from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import SimpleRouter

from accounts.api.add_student_to_class import AddStudentToClass
from accounts.api.chatroom_list import ChatRoomList
from accounts.api.class_level import ClassLevelViewSet
from accounts.api.class_list import ClassListAPIView
from accounts.api.class_name import ClassNameViewSet
from accounts.api.friendship_api import FriendshipViewSet
from accounts.api.list_subject_score import SubjectScoreList
from accounts.api.login_api import LoginApi
from accounts.api.me import MeApi
from accounts.api.message_list import ListMessage
from accounts.api.register_phone import RegisterPhoneApi
from accounts.api.direct_messages import DirectMessages
from accounts.api.semester_report import SemesterReportAPIView
from accounts.api.subject import SubjectListAPIView, SubjectCreateAPIView
from accounts.api.subject_report import SubjectReportView
from accounts.api.subject_score import SubjectScoreCreateUpdateAPIView
from accounts.api.users import UserViewSet

router = SimpleRouter()
router.register(r'friendship', FriendshipViewSet, basename='friendship')
router.register(r'user', UserViewSet, basename='user')
router.register(r'class_level', ClassLevelViewSet, basename='class_level')
router.register(r'class_name', ClassNameViewSet, basename='class_name')

urlpatterns = [
    path('login/', LoginApi.as_view()),
    path('register/phone/', RegisterPhoneApi.as_view()),
    path('me/', MeApi.as_view()),
    path('rooms/', ChatRoomList.as_view(), name='rooms'),
    path('messages/', ListMessage.as_view(), name='messages'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('direct_messages/', DirectMessages.as_view(), name='direct_messages'),
    path('add_student_to_class/', AddStudentToClass.as_view(), name='add_student_to_class'),
    path('class_list/', ClassListAPIView.as_view(), name='class_list'),
    path('subjects/', SubjectListAPIView.as_view(), name='subject-list'),
    path('subjects/create/', SubjectCreateAPIView.as_view(), name='subject-create'),
    path('subject_score/create_update/', SubjectScoreCreateUpdateAPIView.as_view()),
    path('subject_score/', SubjectScoreList.as_view(), name='subject_score'),
    path('subject_report/', SubjectReportView.as_view(), name='subject_report'),
    path('semester_report/', SemesterReportAPIView.as_view(), name='semester_report'),
]

urlpatterns += router.urls
