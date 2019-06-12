from django.db import models


# Create your models here.
class category(models.Model):
    TYPE_CHOICES = (
        ('CU', 'Custom'),
        ('ST', 'Standard'),
    )

    title = models.CharField(max_length=20, help_text='عنوانش چی باشه')
    description = models.TextField(max_length=200, default='',
                                   help_text='توضیحات مربوط به دسته بندی رو اینجا بنویس. یچیزی که مشتری رو جذب کنه')
    image = models.ImageField(upload_to='category/', help_text='تصویرش چی باشه')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, help_text='نوعش چی باشه. ساختی باشه یا نه')

    def __str__(self):
        return self.title


class customCategory(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='subs',
                                 help_text='این تو کدوم دسته بندی قرار میگیره')
    title = models.CharField(max_length=20, help_text='عنوانش چی باشه')
    image = models.ImageField(upload_to='subCategory/', help_text='تصویرش چی باشه')

    def __str__(self):
        return self.title


class product(models.Model):
    sub = models.ForeignKey(customCategory, on_delete=models.CASCADE, blank=True,null=True, related_name='subs',
                            help_text='اگر ساختنی هست این قسمت رو انتخاب کن وگرنه خالی بزارش')
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='cat')
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=9, decimal_places=0, default=0)

    def __str__(self):
        return self.title

#
# class order(models.Model):
#     PAYMENT_CHOICES = (('P', 'Payed'),
#                        ('N', 'Not Payed'))
#     order = models.TextField(max_length=10000)
#     total_cost = models.DecimalField(max_digits=9, decimal_places=3)
#     status = models.CharField(max_length=5, choices=PAYMENT_CHOICES)
