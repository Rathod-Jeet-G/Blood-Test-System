from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('user_profile/',views.user_profile,name='user profile'),
    path('book_appointment/',views.book_appointment,name='book appointment'),
    path('user_feedback/',views.user_feedback,name='user feedback'),
    path('view_appointment/',views.view_appointment,name = 'view appointment'),
    path('view_test/<int:id>/',views.view_test,name='view_test'),
    path('delete_appointment/<int:id>',views.delete_appointment,name='delete_appointment'),
    path('logout/',views.logout,name='logout')
]