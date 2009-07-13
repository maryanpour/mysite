from books.models import Publisher

p1 = Publisher.objects.create(name='Apress',
     address='2855 Telegraph Avenue',
     city='Berkeley', state_province='CA', country='U.S.A.',
     website='http://www.apress.com/')
p2 = Publisher.objects.create(name="O'Reilly",
     address='10 Fawcett St.', city='Cambridge',
     state_province='MA', country='U.S.A.',
     website='http://www.oreilly.com/')
publisher_list = Publisher.objects.all()
publisher_list
