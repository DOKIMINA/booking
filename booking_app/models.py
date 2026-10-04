from django.db import models

# Create your models here.
class Apart(models.Model):

    apart_Types = [
        ('studio', 'Studio'),
        ('one_bed', 'one_bedroom'),
        ('two_beds', 'two_bedrooms'),
        ('squad', 'for squad of people')]

    name = models.CharField(max_length=100)
    number_of_room = models.IntegerField()
    prize = models.DecimalField()
    description = models.TextField(max_length=750)
    capacity = models.IntegerField(max_length=100)
    description = models.TextField(max_length=750, null=True, blank=True)
    image = models.ImageField(upload_to='apartments/', null=True, blank=True)
    type_of_room = models.CharField(max_length=100, choices=apart_Types, default='one_bed')
    is_able = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'Apartment'
    verbose_name_plural = 'Apartments'
    ordering = ['is_able', 'name']


class Booking(models.Model):

    status_choices = [
        ('pending', 'pending'),
        ('conf', 'confirmed'),
        ('canc', 'cancelled')]

    apart = models.ForeignKey(Apart, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=status_choices)

    def __str__(self):
        return self.id