from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 생성 된 시간 (고정))
    updated_at = models.DateTimeField(auto_now=True) # 데이터가 업데이트 된 시간 (업데이트 할 때마다 계속 시간이 변경)

    class Meta:
        abstract = True # DB에 테이블을 추가하지 마시오.