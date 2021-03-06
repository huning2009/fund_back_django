from django.db import models

from api.models import Fund, Index


class IndicatorForPlot(models.Model):
    windcode = models.ForeignKey(Fund, to_field="windcode", on_delete=models.CASCADE)
    fund_setupdate = models.DateField(verbose_name="成立日期")
    fund_corp_fundmanagementcompany = models.CharField(max_length=25, verbose_name="管理人")
    fund_fundscale = models.FloatField(verbose_name="规模", null=True)
    prt_netasset = models.FloatField(verbose_name="净资产", null=True)
    rpt_date = models.DateField(verbose_name="报告期")
    update_date = models.DateField(verbose_name="更新日期")

    class Meta:
        db_table = "t_ff_indicator_for_plot"
        verbose_name = "画图用数据"
        verbose_name_plural = verbose_name


class Indicator(models.Model):
    windcode = models.ForeignKey(Fund, to_field="windcode", on_delete=models.CASCADE)
    indicator = models.CharField(max_length=50, verbose_name="指标名称")
    numeric = models.FloatField(null=True, verbose_name="数值")
    text = models.TextField(null=True, verbose_name="文本数据")
    note = models.CharField(max_length=2, null=True, verbose_name="年份")
    rpt_date = models.DateField(verbose_name="报告期")
    update_date = models.DateField(verbose_name="更新日期")

    class Meta:
        db_table = "t_ff_indicator_for_filter"
        verbose_name = "筛选用数据"
        verbose_name_plural = verbose_name
        ordering = ['id']


class IndicatorIndex(models.Model):
    windcode = models.ForeignKey(Index, to_field="windcode", on_delete=models.CASCADE, verbose_name="证券代码")
    indicator = models.CharField(max_length=50, verbose_name="指标名称")
    numeric = models.FloatField(null=True, verbose_name="数值")
    text = models.TextField(null=True, blank=True, verbose_name="文本数据")
    note = models.CharField(max_length=2, null=True, blank=True, verbose_name="年份")
    rpt_date = models.DateField(verbose_name="报告期")
    update_date = models.DateField(verbose_name="更新日期")

    class Meta:
        db_table = "t_ff_indicator_for_filter_index"
        verbose_name = "指数筛选用数据"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.windcode.windcode
