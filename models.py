from django.db import models

# Create your models here.

class Customer (models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    time_interval = 60 # interval
    working_day_start = 10  # starts working at 10 am
    working_day_end = 20    # ends working at 8 pm
    duratin = service_duration # how long service takes
    initial_date= models.DateTimeField('reservation start')
    final_date= models.DateField('reservation end')
  
    

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Reservation (models.Model):
    start_date = datetime.datetime(2021, 10, 05)
    end_date = datetime.datetime (2021, 10, 30)
    this_period_end = start + datetime.timedelta (hours=duration)
    existing_reservation = customer.reservation_set.filter(startime_It=this_period_end,endtime_gt=start)
    tool= models.ForeignKey(Tool, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #customer = Customer.objects.get(pk=customer:id)

    #reservation=set(values['customer_id']for values in Booking.objects.objects.filter
    #(initial_date_Ite=end_date, final_date_gte=start_date).values('customer_id'))


    def __str__(self):
        return not existing_reservation.exists()




      


