from django.db import models

# Create your models here.
# class Employee(models.Model):
#     eid = models.CharField(max_length=20)
#     ename = models.CharField(max_length=100)
#     eemail = models.EmailField()
#     econtact = models.CharField(max_length=15)
#     class Meta:
#         db_table = "employee"
#
# class Manager(models.Model):
#     eid = models.CharField(max_length=20)
#     ename = models.CharField(max_length=100)
#     eemail = models.EmailField()
#     econtact = models.CharField(max_length=15)
#     class Meta:
#         db_table = "Manager"

# Voice sensor data model
class VoiceCommand(models.Model):
    CmdID = models.CharField(max_length=20)
    CmdDate = models.CharField(max_length=100)
    CmdTime = models.CharField(max_length=15)
    CmdStatus= models.CharField(max_length=15)
    class Meta:
        db_table = "command"

# Food bowl weight sensor data model
class BowlWeight(models.Model):
    BowlWeightID = models.CharField(max_length=20)
    BowlWeightDate = models.CharField(max_length=20)
    BowlWeightAfter = models.FloatField()
    BowlWeightBefore = models.FloatField()
    class Meta:
        db_table = "bowlWeight"

# Container weight sensor data model
class FoodContainerWeight(models.Model):
    ContainerWeightID = models.CharField(max_length=20)
    ContainerDate = models.CharField(max_length=20)
    WeightAfterRelease = models.FloatField()
    WeightBeforeRelease = models.FloatField()
    class Meta:
        db_table = "containerWeight"

# IR sensor data model
class FoodLevelMonitor(models.Model):
    FoodLevelMonitorID = models.CharField(max_length=20)
    RecordedTime = models.CharField(max_length=15)
    FoodLevelStatus = models.BooleanField()
    class Meta:
        db_table = "FoodLevel"
