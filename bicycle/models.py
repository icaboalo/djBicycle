from django.db import models

TRACK_CHOICES = (
    ('24', '24'),
    ('26', '26'),
    ('27.5', '27.5'),
    ('29', '29'),
)

YEAR_CHOICES = (
    ('2000', '2000'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
)

# Create your models here.
class Bicycle(models.Model):
    class Meta:
        verbose_name = 'Bicycle'
        verbose_name_plural = 'Bicycles'

    brand = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)
    track = models.CharField(max_length=4, choices=TRACK_CHOICES, blank=False)
    color = models.CharField(max_length=10, blank=False)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, blank=True)


    def __str__(self):
        return self.brand + ' ' + self.model