from django.urls import path,include,re_path
from .views import LogoutView, MyCourseView, UpdateEmailView, UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView

app_name = 'users'

urlpatterns = [
    # 用户信息
    path("info/", UserinfoView.as_view(), name='user_info'),
    # 图片上传
    path('image/upload', UploadImageView.as_view(), name='image_upload'),
    # 用户个人中心修改密码
    path("update/pwd/", UpdatePwdView.as_view(), name='update_pwd'),
    # 发送邮箱验证码
    path("sendemail_code/", SendEmailCodeView.as_view(), name='sendemail_code'),
    # 修改邮箱
    path("update_email/", UpdateEmailView.as_view(), name='update_email'),
    # 我的课程
    path("mycourse/", MyCourseView.as_view(), name='mycourse'),
    # 注销
    path('logout/', LogoutView.as_view(), name="logout"),

]