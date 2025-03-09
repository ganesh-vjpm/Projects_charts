from django.db import models

# Create your models here.

class Line_plot(models.Model):
    month=models.CharField(max_length=50)
    sales=models.IntegerField()

    class Meta:
        db_table='line_plot'

class Bar_plot(models.Model):
    department=models.CharField(max_length=50)
    revenue=models.IntegerField()

    class Meta:
        db_table='bar_plot'

class Radar_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    aspect=models.CharField(max_length=50)
    score=models.IntegerField()

    class Meta:
        db_table='radar_plot'

class Scatter_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    hoursstudied=models.CharField(max_length=50)
    examscore=models.IntegerField()

    class Meta:
        db_table='scatter_plot'

class Area_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    month=models.CharField(max_length=50)
    newcustomer=models.IntegerField()
    oldcustomer=models.IntegerField()

    class Meta:
        db_table='area_plot'

class Pie_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    company=models.CharField(max_length=50)
    marketshare=models.IntegerField()

    class Meta:
        db_table='pie_plot'

class Histogram_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    agegroup=models.CharField(max_length=50)
    customers=models.IntegerField()

    class Meta:
        db_table='histogram_plot'


class Box_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    department=models.CharField(max_length=50)
    mean=models.IntegerField()
    q1=models.IntegerField()
    median=models.IntegerField()
    q2=models.IntegerField()
    max=models.IntegerField()

    class Meta:
        db_table='box_plot'

class StackedBar_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    quater,electronics,furniture,clothing,total=models.CharField(max_length=50),models.IntegerField(),models.IntegerField(),models.IntegerField(),models.IntegerField()

    class Meta:
        db_table='stackedbar_plot'

class Heatmap_plot(models.Model):
    id=models.IntegerField(primary_key=True)
    region,january,february,march,april,may=models.CharField(max_length=50),models.IntegerField(),models.IntegerField(),models.IntegerField(),models.IntegerField(),models.IntegerField()

    class Meta:
        db_table='heatmap_plot'