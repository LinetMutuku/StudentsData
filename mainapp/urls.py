
from django.urls import path
from mainapp import views
from Studentdata import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('all_students',views.all_students, name = 'all_students'),
    path('student_details/<int:student_id>/', views.student_details, name='student_details'),
    path('delete_student/delete/<int:student_id>/', views.delete_student, name= 'delete_student'),
    path('update_student/update/<int:student_id>/', views.update_student, name='update_student'),
    path('search_students', views.search_students, name= 'search_students'),
    path ('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
