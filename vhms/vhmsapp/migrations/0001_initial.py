# Generated by Django 4.2 on 2023-06-16 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissiondate', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Admission Date')),
                ('dischargedate', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Discharge Date')),
            ],
            options={
                'verbose_name_plural': 'Admissions',
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalname', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Animal Name if any')),
                ('species', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Animal Species')),
                ('breed', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Animal Breed')),
                ('colour', models.CharField(blank=True, default='Black', max_length=30, null=True, verbose_name='Animal Colour')),
                ('age', models.IntegerField(default=1)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('note', models.CharField(blank=True, default='', max_length=225, verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'Animals',
            },
        ),
        migrations.CreateModel(
            name='AnimalTreatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=6, null=True, verbose_name='Quantity of Medicine')),
                ('treatmentdate', models.DateField(default=django.utils.timezone.now, verbose_name='Date of Treatment')),
                ('doctorfee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name="Doctor's Fee")),
                ('nursingfee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Nursing Fees')),
                ('hospitalfee', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True, verbose_name='Hospital Fees')),
                ('note', models.CharField(default='', max_length=255, null=True, verbose_name='Note of Treatment')),
                ('admission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.admission', verbose_name='Treatment Admission Id')),
            ],
            options={
                'verbose_name_plural': 'Animal Treatments',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentdate', models.DateField(default=django.utils.timezone.now, verbose_name='Appointment Date')),
                ('starttime', models.TimeField(default=django.utils.timezone.now, verbose_name='Start Time')),
                ('endtime', models.TimeField(default=django.utils.timezone.now, verbose_name='End Time')),
                ('note', models.CharField(blank=True, default='', max_length=225, verbose_name='Note')),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.animal', verbose_name='Animal_ID')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billdate', models.DateField(default=django.utils.timezone.now, verbose_name='Bill Date')),
                ('admission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.admission', verbose_name='Animal on Treatment Admission')),
            ],
            options={
                'verbose_name_plural': 'Bills',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(default='Doctor', max_length=60, verbose_name='Designation')),
                ('joindate', models.DateField(blank=True, null=True, verbose_name='Date of Join')),
                ('exitdate', models.DateField(blank=True, null=True, verbose_name='Date of Exit')),
                ('qualifications', models.CharField(default=' DVM, DACVIM', max_length=100)),
                ('experience', models.TextField()),
                ('specialty', models.CharField(blank=True, max_length=100, null=True)),
                ('education', models.TextField(blank=True, max_length=1000, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.department')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicinename', models.CharField(blank=True, max_length=100, null=True, verbose_name='Medicine Name')),
                ('cost_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Cost Price')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Sale Price')),
                ('quantity_in_stock', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Quantity in Stock')),
                ('make', models.CharField(blank=True, max_length=60, null=True, verbose_name='Manufacturing Company')),
            ],
            options={
                'verbose_name_plural': 'Medicines',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Mr', max_length=10, verbose_name='Title')),
                ('fname', models.CharField(default='', max_length=50, verbose_name='First Name')),
                ('lname', models.CharField(default='', max_length=50, verbose_name='Last Name')),
                ('house', models.CharField(blank=True, max_length=50, verbose_name='House Name')),
                ('street', models.CharField(blank=True, max_length=50, verbose_name='Street')),
                ('locality', models.CharField(blank=True, max_length=50, verbose_name='Locality')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('state', models.CharField(blank=True, default='Kerala', max_length=50, verbose_name='State')),
                ('pin', models.IntegerField(default=670645, verbose_name='PIN Code')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Phone Numbers')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email Id')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('loginid', models.CharField(blank=True, max_length=40, null=True, verbose_name='Login Id')),
                ('password', models.CharField(blank=True, max_length=20, null=True, verbose_name='Password')),
                ('forget_password_hint_question', models.CharField(blank=True, default='Name of the first school you studied', max_length=100, null=True, verbose_name='Forget Password Hint Question')),
                ('forget_password_hint_answer', models.CharField(blank=True, default='vjec@fml', max_length=100, null=True, verbose_name='Forget Password Hint Answer')),
                ('address', models.CharField(default='Chemberi', max_length=30)),
                ('zip_code', models.CharField(default='670764', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Treatment Name')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Treatment Cost')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='Duration')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Available')),
            ],
            options={
                'verbose_name_plural': 'Treatments',
            },
        ),
        migrations.CreateModel(
            name='VeterinaryRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_address', models.CharField(max_length=42)),
                ('transaction_hash', models.CharField(max_length=66)),
                ('block_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.person', verbose_name='Person Data')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Registrations',
            },
        ),
        migrations.CreateModel(
            name='MedicinePurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchasedate', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date of Purchase')),
                ('pquantity', models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='Purchasing Quantity')),
                ('supplier', models.CharField(blank=True, max_length=100, null=True, verbose_name='Supplier of the Medicine')),
                ('supplier_invoice_no', models.CharField(blank=True, max_length=50, verbose_name='Supplier Invoice Number')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.medicine', verbose_name='Medicine_ID')),
            ],
            options={
                'verbose_name_plural': 'Medicine Purchases',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Phone Numbers')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email Id')),
                ('departments', models.ManyToManyField(blank=True, to='vhmsapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(default='Staff', max_length=60, verbose_name='Designation')),
                ('joindate', models.DateField(blank=True, null=True, verbose_name='Date of Join')),
                ('exitdate', models.DateField(blank=True, null=True, verbose_name='Date of Exit')),
                ('department', models.CharField(default='Administration', max_length=100)),
                ('qualifications', models.CharField(default='Degree in relevant field', max_length=100)),
                ('experience', models.TextField()),
                ('person', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.person', verbose_name='Person Data')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='DoctorAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.appointment', verbose_name='Appointment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointments', to='vhmsapp.doctor', verbose_name='Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.hospital', verbose_name='Hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.person', verbose_name='Person Data'),
        ),
        migrations.CreateModel(
            name='BillEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.IntegerField(default=1, verbose_name='Serial no on bill')),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.bill', verbose_name='Bill of the Entry')),
                ('treatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.animaltreatment', verbose_name='Treatment on Bill')),
            ],
            options={
                'verbose_name_plural': 'Bill Entries',
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='vhmsapp.doctor', verbose_name='Doctor_ID'),
        ),
        migrations.AddField(
            model_name='animaltreatment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.doctor', verbose_name='Treatment giving doctor'),
        ),
        migrations.AddField(
            model_name='animaltreatment',
            name='medicine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.medicine', verbose_name='Medicine_ID'),
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.person', verbose_name='Owner'),
        ),
        migrations.AddField(
            model_name='admission',
            name='animal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vhmsapp.animal', verbose_name='Animal_ID'),
        ),
    ]
