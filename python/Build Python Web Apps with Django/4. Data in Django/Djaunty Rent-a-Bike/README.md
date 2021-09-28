#### DATA IN DJANGO

# [Djaunty Rent-a-Bike](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/projects/djaunty-rent-a-bike)

The owners of the Djaunty Rent-a-Bike company have asked that you help them revamp their old paper and pencil method of renting out bikes. 
They know that you’ve learned about Django models, databases, and “CRUD” — and they’re excited to see you apply your skills.

In your conversation with the owners, you realized that their booking system is rather streamlined. 
Their bikes are rented for the day at a set price and they mainly care about three things: 
bikes, renters, and rentals. You can boil it down to a schema like:
* `Bike`
  * `bike_type` (Rent-a-Bike offers standard, tandem, and electric bikes)
  * `color` (color of the bike)
* `Renter`
  * `first_name` (the first name of the renter)
  * `last_name` (the last name of the renter)
  * `phone` (the phone number of the renter)
  * `vip_num` (renter’s VIP status and number)
* `Rental`
  * `bike` (what bike is being rented)
  * `renter` (who is renting the bike)
  * `date` (the date of the rental)
  * `price` (how much does the bike rental cost)

The owners have asked you to solely focus your skills on the models and not worry about the templates or views.
