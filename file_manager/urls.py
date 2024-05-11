from django.urls import path

from .views import GetFileListView, UploadFileView, DeleteFileView, DownloadFileView

app_name = 'file_manager'

urlpatterns = [
    path('list/', GetFileListView.as_view(), name='file-list'),
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('delete/<int:pk>/', DeleteFileView.as_view(), name='delete-file'),
    path('download/<int:pk>/', DownloadFileView.as_view(), name='download-file'),
]
