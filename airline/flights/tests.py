from django.db.models import Max
from django.test import Client,TestCase
from .models import Aiport,Flights,Passenger

# Create your tests here.
class FlightTestCase(TestCase):

    def setUp(self):
        #Creating airports
        a1=Aiport.objects.create(code="AAA",city="city-A")
        a2=Aiport.objects.create(code="BBB",city="city-B")

        #create flights
        Flights.objects.create(origin=a1,destination=a2,duration=100)
        Flights.objects.create(origin=a1,destination=a1,duration=200)
        Flights.objects.create(origin=a1,destination=a2,duration=-100)

    def test_departure_count(self):
       a=Aiport.objects.get(code="AAA")
       #assertEqual compares the given two values
       self.assertEqual(a.departure.count(),3)

    def test_arrival_count(self):
        a=Aiport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(),1) 

    def test_valid_flight(self):
        a1=Aiport.objects.get(code="AAA")
        a2=Aiport.objects.get(code="BBB")

        #now the flight is satisfying both 1 and 2 conditions so,we use assertTrue to the function from views.py
        f=Flights.objects.get(origin=a1,destination=a2,duration=100)
        self.assertTrue(f.is_valid)

    def test_invalid_flight(self):
        #now the flight is not satisfying 1st condition i.e origin and dest is same,so,we use assertFalse to the function from views.py
        a1=Aiport.objects.get(code="AAA")
        f=Flights.objects.get(origin=a1,destination=a1)
        self.assertFalse(f.is_valid())

    def test_invalid_duration(self):
        a1=Aiport.objects.get(code="AAA")
        a2=Aiport.objects.get(code="BBB")
        #now the flight is not satisfying 2nd condition i.e duration>0,so,we use assertFalse to the function from views.py
        f=Flights.objects.get(origin=a1,destination=a2,duration=-100)
        self.assertFalse(f.is_valid())


