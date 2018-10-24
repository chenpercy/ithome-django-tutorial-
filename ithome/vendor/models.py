from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Vendor(models.Model):
	vendor_name = models.CharField(max_length = 20) # 攤販的名稱
	store_name = models.CharField(max_length = 10) # 攤販店家的名稱
	phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
	address = models.CharField(max_length = 100) # 攤販的地址

	def get_absolute_url(self):
		return reverse("vendors:vendor_id", kwargs={"id": self.id})

	def __str__(self):
		return self.vendor_name



class Food(models.Model):
	food_name = models.CharField(max_length = 30) # 食物名稱
	price_name = models.DecimalField(max_digits = 3, decimal_places=0) # 食物價錢
	food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的

	def __str__(self):
		return self.food_name

class morethanfourty(admin.SimpleListFilter):

	title = _('price')
	parameter_name = 'compareprice'

	def lookups(self, request, model_admin):
		return (
			('>50',_('>50')),
			('<=50',_('<=50')),
		)

	def queryset(self, request, queryset):
		if self.value() == '>50':
			return queryset.filter(price_name__gt=50)
		if self.value() == '<=50':
			return queryset.filter(price_name__lte=50)

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	#list_display = [field.name for field in Vendor._meta.get_fields]
	list_display = [field.name for field in Vendor._meta.fields]

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Food._meta.fields]
	# list_display =['id', 'food_name']
	list_filter = (morethanfourty,)
	search_fields = ('food_name','price_name')
	ordering = ('-price_name',)
	# fields = ['price_name']
	# exclude=['food_name', 'food_vendor']
