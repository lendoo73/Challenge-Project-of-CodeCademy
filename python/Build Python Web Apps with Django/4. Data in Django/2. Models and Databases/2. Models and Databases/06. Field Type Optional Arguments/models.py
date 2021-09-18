from django.db import models

class Owner(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)

class Patient(models.Model):
  breed = models.CharField(max_length=200)
  pet_name = models.CharField(max_length=200)
  age = models.IntegerField(default=0)
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
  # Add your code below:
  DOG = "DO"
  CAT = "CA"
  BIRD = "BI"
  REPTILE = "RE"
  OTHER = "OT"

  ANIMAL_TYPE_CHOICES = [
    (DOG, "Dog"),
    (CAT, "Cat"),
    (BIRD, "Bird"),
    (REPTILE, "Reptile"),
    (OTHER, "Other")
  ]

  animal_type = models.CharField(
    max_length = 2,
    choices = ANIMAL_TYPE_CHOICES,
    default = OTHER
  )
  

  
