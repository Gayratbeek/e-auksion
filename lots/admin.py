from django.contrib import admin
from .models import Amount, News, Category, Lots, LotDate


class LotDateInlines(admin.TabularInline):
    model = LotDate
    extra = 1


class AmountInlines(admin.TabularInline):
    model = Amount
    extra = 1


@admin.register(Amount)
class AmAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Amount._meta.get_fields()]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.get_fields()]


@admin.register(Lots)
class LotsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "status", "category", "photo")
    inlines = [LotDateInlines, AmountInlines]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "category_photo", "slug")


@admin.register(LotDate)
class LotDateAdmin(admin.ModelAdmin):
    list_display = ("lot", "start_date", "date_of_applying", "first_date_osmotr", "second_date_osmotr", "third_date_osmotr")




