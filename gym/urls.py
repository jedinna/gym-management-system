from django.urls import path
from gym import views


urlpatterns = [
   # path('admin/', admin.site.urls),
    path('',views.Home, name='home'),
    path('about/',views.About, name = 'about'),
    path('contact/',views.Contact, name = 'contact'),
    #path('admin_login',views.Login, name='login'),
    path('logout/',views.Logout, name='logout'),

    path('add_enquiry/',views.Add_Enquiry,name='add_enquiry'),
    path('view_enquiry/',views.View_Enquiry,name='view_enquiry'),
    path('delete_enquiry(?p<int:pid>)',views.Delete_Enquiry, name='delete_enquiry'),

    path('add_equipment/',views.Add_Equipment,name='add_equipment'),
    path('view_equipment/',views.View_Equipment,name='view_equipment'),
    path('delete_equipment(?p<int:pid>)', views.Delete_Equipment, name='delete_equipment'),

    path('add_plan/',views.Add_Plan,name='add_plan'),
    path('view_plan/',views.View_Plan,name='view_plan'),
    path('delete_plan(?p<int:pid>)',views. Delete_Plan, name='delete_plan'),

    path('add_member/',views.Add_Member,name='add_member'),
    path('view_member/',views.View_Member,name='view_member'),
    path('delete_member(?p<int:pid>)',views. Delete_Member, name='delete_member'),
]