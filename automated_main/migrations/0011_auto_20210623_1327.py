# Generated by Django 3.1.3 on 2021-06-23 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('automated_main', '0010_remove_uitestresult_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uitestresult',
            name='error',
        ),
        migrations.RemoveField(
            model_name='uitestresult',
            name='failure',
        ),
        migrations.RemoveField(
            model_name='uitestresult',
            name='run_time',
        ),
        migrations.RemoveField(
            model_name='uitestresult',
            name='successful',
        ),
        migrations.AddField(
            model_name='uitestresult',
            name='ui_error_total_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='失败总数'),
        ),
        migrations.AddField(
            model_name='uitestresult',
            name='ui_successful_total_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='成功总数'),
        ),
        migrations.AddField(
            model_name='uitestresult',
            name='ui_total_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='UI测试用例总数'),
        ),
        migrations.AddField(
            model_name='uitestresult',
            name='updata_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
