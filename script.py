from marketing.models import KidsCanCode  # Import your data table
from django.contrib.auth.models import User # Import the staff

# Grab the KidsCanCode table and assign to staff
def update_marketing_field():

    p = KidsCanCode.objects.filter(timestamp__year='2021', timestamp__month='11')
    timothy = User.objects.get(username='BlueTimothyOsadebeb')
    ods = User.objects.get(username='ODS')

    count = 0

    for pa in p:
        if (count % 2) == 0:  # Check if there is no remainder
            pa.staff = timothy
        else:
            pa.staff = ods
        pa.save()
        count += 1
