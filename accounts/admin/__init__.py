from django.contrib import admin
from rest_framework.authtoken.models import TokenProxy

from accounts.admin.chatroom_admin import ChatRoomAdmin
from accounts.admin.class_level_admin import ClassLevelAdmin
from accounts.admin.class_name_admin import ClassNameAdmin
from accounts.admin.class_student_admin import ClassStudentAdmin
from accounts.admin.direct_message_admin import DirectMessageAdmin
from accounts.admin.friendship_admin import FriendShipAdmin
from accounts.admin.message_admin import MessageAdmin
from accounts.admin.token_admin import FilterTokenAdmin
from accounts.admin.user_admin import UserAdmin
from accounts.models import User, ChatRoom, Message, DirectMessage, Friendship, ClassLevel, ClassName, ClassStudent

admin.site.register(User, UserAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(DirectMessage, DirectMessageAdmin)
admin.site.register(Friendship, FriendShipAdmin)

admin.site.unregister(TokenProxy)
admin.site.register(TokenProxy, FilterTokenAdmin)
admin.site.register(ClassLevel, ClassLevelAdmin)
admin.site.register(ClassName, ClassNameAdmin)
admin.site.register(ClassStudent, ClassStudentAdmin)
