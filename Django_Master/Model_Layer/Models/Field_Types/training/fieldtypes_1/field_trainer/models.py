from django.db import models

# Create your models here.

data_for_choice = (
    ('choice1', 'choice1'),
    ('choice2', 'choice2'),
    ('choice3', 'choice3'),
    ('choice4', 'choice4'),
)

class BigModelForTrainingFields(models.Model):
    #this is new primary key
    myAuto = models.AutoField(primary_key=True)
    #big integer can hold numbers from 1 to 9223372036854775807
    bigInteger = models.BigIntegerField(verbose_name="bigInteger")
    #this type store raw binary data
    binaryField= models.BinaryField()
    # true or false
    booleanField = models.BooleanField(default=False)
    #not big text field
    mychar = models.CharField(max_length=50, unique=True, help_text="This is displayed help for my char")
    #datetime filed
    datetimee = models.DateTimeField(unique_for_date="slug")
    #only data field
    onlydate = models.DateField(unique_for_month="text")
    #this type storing duration in time
    durf = models.DurationField()
    #special field for mail addresses
    mail = models.EmailField()
    #Field for files
    files = models.FileField()
    #field for PATH to files
    path = models.FilePathField()
    #Only for float
    gitfloat = models.FloatField()
    #Field dedicated for images, maybe avatar or something
    addImage = models.ImageField()
    #Here we got integers
    integers = models.IntegerField()
    #IP addresses in DB
    ip_address = models.GenericIPAddressField()
    #Very good idea, json in db
    json_data = models.JSONField()
    #boolean but with null=true it will be deprecated in future
    nullBool = models.NullBooleanField()
    #only positive digits
    positiveBig = models.PositiveBigIntegerField()
    #only positive digits, Values from 0 to 2147483647
    positive = models.PositiveIntegerField()
    #only positive digits but small values
    positive_small = models.PositiveSmallIntegerField()
    #This is slugfield, for example it is good for blog
    slug = models.SlugField(unique=True, db_column="slug_column", db_index=True, null=False, blank=False)
    #small integers with positive and negative digits
    smallInteger = models.SmallIntegerField()
    #Text field is for a long text data
    text = models.TextField(choices=data_for_choice, editable=True)
    #This field is for time
    nowTime = models.TimeField()
    #Here i can store urls
    url = models.URLField()
    #this is for universal identificators
    uuid = models.UUIDField()

class RelationshipsModel(models.Model):
    #this is relation many to one
    foreign_key = models.ForeignKey(BigModelForTrainingFields, on_delete=models.CASCADE)
    #this type can make relation many to many
    many_keys = models.ManyToManyField(BigModelForTrainingFields, on_delete=models.CASCADE)
    #this One to one field making relationship type one to one
    one_to_one = models.OneToOneField(BigModelForTrainingFields, on_delete=models.CASCADE)