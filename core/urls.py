from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # <-- this is now the homepage
    path('register/',views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot_password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent' ),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'), 
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('chat/<int:pdf_id>/', views.chat_about_pdf, name='chat_pdf'),
    path('download/<int:pdf_id>/', views.download_summary, name='download_summary'),
    path('generate-documents/', views.document_selector, name='document_selector'),
    path('generate-rental/', views.generate_rental_agreement, name='generate_rental'),
    path('generate-divorce/', views.generate_divorce_agreement, name='generate_divorce'),
    path('generate-land/', views.generate_land_agreement, name='generate_land'),
    path('preview-rental/', views.preview_rental_doc, name='preview_rental'),
    path('preview-divorce/', views.preview_divorce_doc, name='preview_divorce'),
    path('preview-land/', views.preview_land_doc, name="preview_land"),
    path('upload2/', views.auto_classify_upload, name='auto_classify_upload'),
    path('documents/', views.document_list, name='document_list'),
    path('sections/<int:pk>/edit/', views.edit_section, name='edit_section'),
    path('sections/<int:section_id>/upload/', views.upload_to_section, name='upload_to_section'),
    path('documents/<int:doc_id>/delete/', views.delete_document, name='delete_document'),
    path('sections/create/', views.create_section, name='create_section'),
]