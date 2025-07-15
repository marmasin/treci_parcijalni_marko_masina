from django.db import models
from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(
        max_length=250, help_text="Customer name", null=False, blank=False
    )
    last_name = models.CharField(max_length=150, null=True, blank=True)
    vat_id = models.CharField(max_length=11, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the save method to include any custom logic.
        Django automatically handles insert/update based on whether the instance has a primary key.
        """
        super().save(*args, **kwargs)


    @classmethod
    def from_tuple(cls, data):
        """
        Creates a Product instance from a tuple.
        Args:
            data (tuple): A tuple containing (id, name, description, price).
        Returns:
            Product: An instance of Product.
        """
        return cls(id=data[0], name=data[1], last_name=data[2], vat_id=data[3], street=data[4], city=data[5], country=data[6])

    @classmethod
    def get_all(cls):
        """
        Retrieves all Product instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Product objects.
        """
        return cls.objects.all()
