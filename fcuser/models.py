from django.db import models

# Create your models here.
class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name = '사용자명')
    useremail = models.EmailField(max_length=128,
                                  verbose_name= '사용자이메일')
    password = models.CharField(max_length=64,
                                verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    def __str__(self): #문자열로 변환되는 클래스를 반환하는 함수. (기본내장임)
        return self.username  #클래스이름을 문자열로 받아서 원래 그냥 출력하는데, 그 이름을 변경하기 위해 여기를 만들어 수정한다.

    class Meta:
        db_table = 'fastcampus_fcuser'
        #보여지는 모델이름 바꾸기
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
