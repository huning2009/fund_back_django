from django.db import models

from api.models import Fund


class BasicInfo(models.Model):
    windcode = models.ForeignKey(Fund, to_field="windcode", on_delete=models.CASCADE)
    sec_name = models.CharField(max_length=30, verbose_name="简称")
    fullname = models.CharField(db_column="fund_fullname", max_length=100, null=True, verbose_name="全称")
    setup_date = models.DateField(db_column="fund_setupdate", verbose_name="成立日期")
    benchmark = models.TextField(db_column="fund_benchmark", verbose_name="业绩基准", null=True)
    company = models.CharField(max_length=20, db_column="fund_fundmanagementcompany", null=True, verbose_name="管理人")
    invest_scope = models.TextField(db_column="fund_investscope", null=True, verbose_name="投资范围")
    structured = models.IntegerField(db_column="fund_structuredfundornot", choices=((0, "是"), (1, "否")),
                                     verbose_name="分级基金")
    first_invest_type = models.CharField(max_length=25, db_column="fund_firstinvesttype", null=True,
                                         verbose_name="投资类型(一级)")
    invest_type = models.CharField(max_length=25, db_column="fund_investtype", null=True, verbose_name="投资类型")
    update_date = models.DateField(verbose_name="更新日期")

    class Meta:
        db_table = "t_ff_basic_info"
        verbose_name = "基金基础信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"{self.windcode}-{self.sec_name}>"