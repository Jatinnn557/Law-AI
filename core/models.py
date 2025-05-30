from django.db import models
from django.contrib.auth.models import User
import uuid  #unique id

class PasswordReset(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)   #unique id will be generated
    created_when=models.DateTimeField(auto_now_add=True)                         #time stamp which is 10mins after which id resets

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"   

class UploadedPDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.file.name

class ChatHistory(models.Model):
    pdf = models.ForeignKey(UploadedPDF, on_delete=models.CASCADE, related_name='chats')
    question = models.TextField()
    answer = models.TextField()
    asked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question[:30]}..."
    
class Section(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class LegalDocument(models.Model):
    title = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='legal_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
