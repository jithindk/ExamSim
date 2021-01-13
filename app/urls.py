from django.urls import path
from . import Views

urlpatterns = [
    path('', Views.Home, name='home'),

    path('login/', Views.Login, name='login'),
    path('reg/', Views.Register, name='reg'),
    path('logout/', Views.Logout, name='logout'),

    path('dashboard/<str:pk>', Views.Dashboard, name='dashboard'),
    path('courses/', Views.Courses, name='courses'),
    path('yourCourses/<str:pk>', Views.Your_Courses, name='yourCourses'),
    path('results/<str:pk>', Views.Results, name='results'),
    path('about/', Views.About, name='about'),

    path('updateUser/', Views.Update_User, name='updateUser'),
    path('deleteUser/', Views.Delete_User, name='deleteUser'),
    path('resetPassword/', Views.Password_Reset, name='resetPassword'),

    path('courseDetails/<str:pk>', Views.Course_Details, name='courseDetails'),
    path('moduleDetails/<str:pk>', Views.Module_Details, name='moduleDetails'),
    path('resultDetails/<str:pk>', Views.Result_Details, name='resultDetails'),
    path("takenCourse/<str:pk>", Views.Taken_Courses, name='takenCourses'),

    path('createCourse/<str:pk>', Views.Create_Course, name='createCourse'),
    path('updateCourse/<str:pk>', Views.Update_Course, name='updateCourse'),
    path('deleteCourse/<str:pk>', Views.Delete_Course, name='deleteCourse'),

    path('createModule/<str:pk>', Views.Create_Module, name='createModule'),
    path('updateModule/<str:pk>', Views.Update_Module, name='updateModule'),
    path('deleteModule/<str:pk>', Views.Delete_Module, name='deleteModule'),

    path('createQuestion/<str:pk>', Views.Create_Question, name='createQuestion'),
    path('updateQuestion/<str:pk>', Views.Update_Question, name='updateQuestion'),
    path('deleteQuestion/<str:pk>', Views.Delete_Question, name='deleteQuestion'),

    path('Exam/<str:m>/<int:i>', Views.Exam, name='exam'),
]