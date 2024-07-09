from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Trang chính hiển thị danh sách sinh viên
    path('add/', views.add_student, name='add_student'),  # Trang để thêm sinh viên
    path('edit/<int:id>/', views.edit_student, name='edit_student'),  # Trang để chỉnh sửa sinh viên dựa trên ID
    path('delete/<int:id>/', views.delete_student, name='delete_student'),  # Trang để xóa sinh viên dựa trên ID
    path('search/', views.search_student, name='search_student'),  # Trang để tìm kiếm sinh viên dựa trên mã sinh viên
]
