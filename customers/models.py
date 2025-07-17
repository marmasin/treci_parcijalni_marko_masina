from django.db import models

# Create your models here.
def create_customer_model():
    """
    Function to create the Customer model.
    This function is used to ensure that the model is created only once.
    """
    class Meta:
        app_label = 'customers'
class Customer(models.Model):
    name = models.CharField(max_length=30)
    vat_it = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


    def __str__(self):
            return f"{self.name}"
        

    def save(self, *args, **kwargs):

            super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):

        return cls(id=data[0], name=data[1], vat_it=data[2], street=data[3], city=data[4], country=data[5])

    
    @classmethod
    def get_all(cls):

        return cls.objects.all()    