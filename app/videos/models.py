from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.
# - title
# - description
# - link
# - category
# - views_count
# - thumbnail
# - video_file
# - User : FK

class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank = True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default = 0)
    thumbnail = models.URLField() # S3 Bucket -> Save File -> URL -> save URL
    video_file = models.FileField(upload_to = 'storage/') # 파일을 저장하는 방법

    user = models.ForeignKey(User, on_delete = models.CASCADE)