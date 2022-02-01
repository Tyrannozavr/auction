from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class auctionlist(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    desc = models.TextField()           #CharField cannot be left without giving a max_length, Textfield can
    starting_bid = models.IntegerField()        
    image_url = models.CharField(max_length=228, default=None, blank=True, null=True)
    category = models.CharField(max_length=64)
    active_bool = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'список объявлений'
        verbose_name = 'объявление'


    def __str__(self):
        return self.title

class bids(models.Model):
    user = models.CharField(max_length=30)
    listingid = models.IntegerField()
    bid = models.IntegerField()

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

class comments(models.Model):
    user = models.CharField(max_length=64)
    comment = models.TextField()
    listingid = models.IntegerField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    

class watchlist(models.Model):
    watch_list = models.ForeignKey(auctionlist, on_delete=models.CASCADE)
    user = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Наблюдение'
        verbose_name_plural = 'Список наблюдений'

class winner(models.Model):
    bid_win_list = models.ForeignKey(auctionlist, on_delete=models.CASCADE)
    user = models.CharField(max_length=64, default=None)

    class Meta:
        verbose_name = 'Победитель'
        verbose_name_plural = 'Победители'