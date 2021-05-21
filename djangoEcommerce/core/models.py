from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.

class customUser(AbstractUser):
    user_type_choices = ((1, "Admin"), (2, "Staff"), (3, "Merchant"), (4, "Customer"))
    user_type = models.CharField(max_length=255, choices=user_type_choices, default=1)


class adminUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id = models.OneToOneField(customUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class staffUser(models.Model):
    profile_pic=models.FileField(default="")
    auth_user_id = models.OneToOneField(customUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class merchantUser(models.Model):
    auth_user_id = models.OneToOneField(customUser, on_delete=models.CASCADE)
    profile_pic=models.FileField(default="")
    company_name = models.CharField(max_length=255)
    gst_details = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class customerUser(models.Model):
    auth_user_id = models.OneToOneField(customUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)


class categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse("category_list")

    def __str__(self):
        return self.title

class subCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def get_absolute_url(self):
        return reverse("sub_category_list")


class products(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.CharField(max_length=255)
    sub_categories_id = models.ForeignKey(subCategories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    product_max_price = models.CharField(max_length=255)
    product_discount_price = models.CharField(max_length=255)
    product_description = models.TextField()
    product_long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    added_by_merchant = models.ForeignKey(merchantUser, on_delete=models.CASCADE)
    total_stock = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1)


class productMedia(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    media_type_choice = ((1, "Image"), (2, "Video"))
    media_type = models.CharField(choices=media_type_choice, max_length=255)
    media_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    transaction_type_choices = ((1, "BUY"), (2, "SELL"))
    transaction_product_count = models.IntegerField(default=1)
    transaction_type = models.CharField(choices=transaction_type_choices, max_length=255)
    transcation_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class productDetails(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productAbout(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productTags(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
    question = models.TextField()
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productReviews(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(customUser, on_delete=models.CASCADE)
    review_image = models.FileField()
    rating = models.CharField(default="5", max_length=255)
    review = models.TextField(default="")
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productReviewVote(models.Model):
    id = models.AutoField(primary_key=True)
    product_review_id = models.ForeignKey(productReviews, on_delete=models.CASCADE)
    user_id_vote = models.ForeignKey(customUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productVarient(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class productVarientItems(models.Model):
    id = models.AutoField(primary_key=True)
    product_varient_id = models.ForeignKey(productVarient, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class customerOrders(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    purchase_price = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=255)
    discount_amount = models.CharField(max_length=255)
    product_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class orderDeliveryStatus(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(customerOrders, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=customUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created: 
        if instance.user_type==1:
            adminUser.objects.create(auth_user_id=instance)

        if instance.user_type==2:
            staffUser.objects.create(auth_user_id=instance)

        if instance.user_type==3:
            merchantUser.objects.create(auth_user_id=instance, company_name="", gst_details="", address="")

        if instance.user_type==4:
            customerUser.objects.create(auth_user_id=instance)
        
@receiver(post_save, sender=customUser)
def save_user_profile(sender, instance, **kwargs):
    
    if instance.user_type==1:
        instance.adminuser.save()

    if instance.user_type == 2:
        instance.staffuser.save()

    if instance.user_type== 3:
        instance.merchantuser.save()
    
    if instance.user_type == 4:
        instance.customeruser.save()
