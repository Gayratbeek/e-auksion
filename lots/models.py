from django.db import models
from django.contrib.auth.models import User
from account.models import Account
from django.urls import reverse


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    description = models.TextField()
    desc = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Pages(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=150)
    content = models.TextField()

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class Category(models.Model):
    name = models.CharField(verbose_name="Category", db_index=True, max_length=128)
    description = models.CharField(verbose_name="Description", max_length=255)
    category_photo = models.ImageField("Изображение", upload_to="category_photo/", blank=True, null=True)
    banner_photo = models.ImageField("Баннерное изображение", upload_to="category_photo/", blank=True, null=True)
    slug = models.SlugField(unique=True)
    # count = models.Count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories:detail", kwargs={"slug": self.slug})


class CategoryFilter(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    field1 = models.CharField(verbose_name="Поле-1", db_index=True, max_length=128)
    field2 = models.CharField(verbose_name="Поле-2", db_index=True, max_length=128)


class Lots(models.Model):
    name = models.CharField("Наименование товара", db_index=True, unique=True, max_length=128)
    description = models.TextField(verbose_name="Description", max_length=255)
    STATUS_OF_LOT = (
        (1, 'Еще не начат'),
        (2, 'В ожидании оплаты'),
        (3, 'Успешно завершено'),
    )
    status = models.IntegerField(verbose_name="Status of lot", choices=STATUS_OF_LOT, default=1)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="children")
    user = models.ForeignKey(Account, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="accounts", default=User)
    photo = models.ImageField("Изображение", upload_to="lot_photo/", blank=True, null=True)

    def __str__(self):
        return self.name


class LotDate(models.Model):
    lot = models.ForeignKey(Lots, verbose_name="Лот", on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Дата начала лота")
    date_of_applying = models.DateField(verbose_name="Дата срока подачи заявки")
    first_date_osmotr = models.DateField(verbose_name="Первый день осмотра")
    second_date_osmotr = models.DateField(verbose_name="Второй день осмотра", blank=True, null=True)
    third_date_osmotr = models.DateField(verbose_name="Третий день осмотра", blank=True, null=True)


class Amount(models.Model):
    lot = models.ForeignKey(Lots, verbose_name="Лот", on_delete=models.CASCADE)
    starting_amount = models.FloatField(verbose_name="Стартовая цена")
    assessed_value = models.FloatField(verbose_name="Оценочная стоимость", blank=True, null=True)
    percent_deposit = models.FloatField(verbose_name="Закладные проценты")
    deposit_amount = models.FloatField(verbose_name="Сумма закалата", blank=True, null=True)
    percent_step = models.FloatField(verbose_name="Процент шага")
    first_step = models.FloatField(verbose_name="Первый шаг", blank=True, null=True)

    def __str__(self):
        return self.lot.name

    class Meta:
        verbose_name = "Сумма за лот"
        verbose_name_plural = "Суммы за лоты"

    def save(self, **kwargs):
        super(Amount, self).save()
        if self.deposit_amount != ((self.starting_amount) * (self.percent_deposit)/100):
            self.deposit_amount = ((self.starting_amount) * (self.percent_deposit)/100)
            self.first_step = ((self.starting_amount) * (self.percent_step) / 100)
            super(Amount, self).save()
        elif self.first_step != ((self.starting_amount) * (self.percent_step)/100):
            self.first_step = ((self.starting_amount) * (self.percent_step)/100)
            self.deposit_amount = ((self.starting_amount) * (self.percent_deposit) / 100)
            super(Amount, self).save()




