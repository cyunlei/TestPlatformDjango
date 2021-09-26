# Generated by Django 3.1.3 on 2021-07-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automated_main', '0011_auto_20210623_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='apitestcase',
            name='api_documentation',
            field=models.CharField(max_length=800, null=True, verbose_name='API接口文档地址'),
        ),
        migrations.AlterField(
            model_name='apitestcase',
            name='api_key_variable',
            field=models.CharField(max_length=800, null=True, verbose_name='关键字变量名称'),
        ),
        migrations.AlterField(
            model_name='apitestcase',
            name='api_test_case_name',
            field=models.CharField(max_length=800, verbose_name='API测试用例名称'),
        ),
        migrations.AlterField(
            model_name='apitestcase',
            name='api_value_variable',
            field=models.CharField(max_length=800, null=True, verbose_name='提取变量'),
        ),
        migrations.AlterField(
            model_name='apitestcase',
            name='api_variable_results',
            field=models.CharField(max_length=800, null=True, verbose_name='变量提取结果'),
        ),
    ]
