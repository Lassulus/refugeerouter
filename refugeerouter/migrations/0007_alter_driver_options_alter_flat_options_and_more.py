# Generated by Django 4.0.2 on 2022-03-25 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refugeerouter', '0006_flat_interim_alter_booking_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={},
        ),
        migrations.AlterModelOptions(
            name='notifier',
            options={},
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='interim',
            new_name='is_interim',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='bath',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='contact_data',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='kitchen',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='rooms',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='shared_bath',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='shared_kitchen',
        ),
        migrations.RemoveField(
            model_name='group',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_relation',
        ),
        migrations.AddField(
            model_name='booking',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='driver',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='flat',
            name='is_barrier_free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='is_pets_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='group',
            name='contact_refugee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_group', to='refugeerouter.refugee'),
        ),
        migrations.AddField(
            model_name='group',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='notifier',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='refugee',
            name='has_pets',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='refugee',
            name='need_barrier_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='refugee',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='trip',
            name='notes',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='group',
            name='wish_city',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]