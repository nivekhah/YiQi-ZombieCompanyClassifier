from django import forms

class UploadForm(forms.Form):
    base_test_sum = forms.FileField(label='企业基本信息', required=True)
    knowledge_test_sum = forms.FileField(label='知识产权数据', required=True)
    money_report_test_sum = forms.FileField(label='融资数据', required=True)
    year_report_test_sum = forms.FileField(label='年报数据', required=True)

class SingleDataInputForm(forms.Form):
    company_id = forms.IntegerField(label='企业ID', required=True)
    zhuce_time = forms.IntegerField(label='注册时间', required=False)
    zhuce_ziben = forms.FloatField(label='注册资本', required=False)
    HANGYE_CHOICES = (('UN', '未知'), ('JT', '交通运输业'), ('SY', '商业服务业'), ('GY', '工业'), ('FW', '服务业'),
                      ('SQ', '社区服务'), ('LS', '零售业'))
    hangye = forms.TypedChoiceField(label='行业', required=False, choices=HANGYE_CHOICES, coerce=lambda x: str(x))
    QUYU_CHOICES = (('UN', '未知'), ('SD', '山东'), ('GD', '广东'), ('GX', '广西'), ('JX', '江西'), ('HB', '湖北'),
                    ('HN', '湖南'), ('FJ', '福建'))
    quyu = forms.TypedChoiceField(label='区域', required=False, choices=QUYU_CHOICES, coerce=lambda x: str(x))
    QIYELEIXING_CHOICES = (('UN', '未知'), ('NM', '农民专业合作社'), ('HH', '合伙企业'), ('YX', '有限责任公司'),
                           ('GF', '股份有限公司'), ('JT', '集体所有制企业'))
    qiyeleixing = forms.TypedChoiceField(label='企业类型', required=False, choices=QIYELEIXING_CHOICES, coerce=lambda x: str(x))
    KONGZHIREN_CHOICES = (('UN', '未知'), ('QY', '企业法人'), ('ZR', '自然人'))
    kongzhiren_leixing = forms.TypedChoiceField(label='控制人类型', required=False, choices=KONGZHIREN_CHOICES, coerce=lambda x: str(x))
    kongzhiren_chigubili = forms.FloatField(label='控制人持股比例', required=False)

    zhuanli = forms.TypedChoiceField(label='专利', required=False, choices=(('UN', '未知'), ('Y', '有'), ('N', '无')))
    shangbiao = forms.TypedChoiceField(label='商标', required=False, choices=(('UN', '未知'), ('Y', '有'), ('N', '无')))
    zhuzuoquan = forms.TypedChoiceField(label='著作权', required=False, choices=(('UN', '未知'), ('Y', '有'), ('N', '无')))

    zhaiquan_chengben1 = forms.FloatField(label='债权融资成本1', required=False)
    zhaiquan_edu1 = forms.FloatField(label='债权融资额度1', required=False)
    zhaiquan_chengben2 = forms.FloatField(label='债权融资成本2', required=False)
    zhaiquan_edu2 = forms.FloatField(label='债权融资额度2', required=False)
    zhaiquan_chengben3 = forms.FloatField(label='债权融资成本3', required=False)
    zhaiquan_edu3 = forms.FloatField(label='债权融资额度3', required=False)
    guquan_chengben1 = forms.FloatField(label='股权融资成本1', required=False)
    guquan_edu1 = forms.FloatField(label='股权融资额度1', required=False)
    guquan_chengben2 = forms.FloatField(label='股权融资成本2', required=False)
    guquan_edu2 = forms.FloatField(label='股权融资额度2', required=False)
    guquan_chengben3 = forms.FloatField(label='股权融资成本3', required=False)
    guquan_edu3 = forms.FloatField(label='股权融资额度3', required=False)
    neibu_chengben1 = forms.FloatField(label='内部融资和贸易融资成本1', required=False)
    neibu_edu1 = forms.FloatField(label='内部融资和贸易融资额度1', required=False)
    neibu_chengben2 = forms.FloatField(label='内部融资和贸易融资成本2', required=False)
    neibu_edu2 = forms.FloatField(label='内部融资和贸易融资额度2', required=False)
    neibu_chengben3 = forms.FloatField(label='内部融资和贸易融资成本3', required=False)
    neibu_edu3 = forms.FloatField(label='内部融资和贸易融资额度3', required=False)
    xiangmu_chengben1 = forms.FloatField(label='项目融资和政策融资成本1', required=False)
    xiangmu_edu1 = forms.FloatField(label='项目融资和政策融资额度1', required=False)
    xiangmu_chengben2 = forms.FloatField(label='项目融资和政策融资成本2', required=False)
    xiangmu_edu2 = forms.FloatField(label='项目融资和政策融资额度2', required=False)
    xiangmu_chengben3 = forms.FloatField(label='项目融资和政策融资成本3', required=False)
    xiangmu_edu3 = forms.FloatField(label='项目融资和政策融资额度3', required=False)

    congyerenshu1 = forms.IntegerField(label='从业人数1', required=False)
    congyerenshu2 = forms.IntegerField(label='从业人数2', required=False)
    congyerenshu3 = forms.IntegerField(label='从业人数3', required=False)
    zichanzonge1 = forms.FloatField(label='资产总额1', required=False)
    zichanzonge2 = forms.FloatField(label='资产总额2', required=False)
    zichanzonge3 = forms.FloatField(label='资产总额3', required=False)
    fuzhaizonge1 = forms.FloatField(label='负债总额1', required=False)
    fuzhaizonge2 = forms.FloatField(label='负债总额2', required=False)
    fuzhaizonge3 = forms.FloatField(label='负债总额3', required=False)
    yingshou1 = forms.FloatField(label='营业总收入1', required=False)
    yingshou2 = forms.FloatField(label='营业总收入2', required=False)
    yingshou3 = forms.FloatField(label='营业总收入3', required=False)
    zhuyingshou1 = forms.FloatField(label='主营业务收入1', required=False)
    zhuyingshou2 = forms.FloatField(label='主营业务收入2', required=False)
    zhuyingshou3 = forms.FloatField(label='主营业务收入3', required=False)
    lirun1 = forms.FloatField(label='利润总额1', required=False)
    lirun2 = forms.FloatField(label='利润总额2', required=False)
    lirun3 = forms.FloatField(label='利润总额3', required=False)
    jinglirun1 = forms.FloatField(label='净利润1', required=False)
    jinglirun2 = forms.FloatField(label='净利润2', required=False)
    jinglirun3 = forms.FloatField(label='净利润3', required=False)
    nashui1 = forms.FloatField(label='纳税总额1', required=False)
    nashui2 = forms.FloatField(label='纳税总额2', required=False)
    nashui3 = forms.FloatField(label='纳税总额3', required=False)
    suoyouzhe1 = forms.FloatField(label='所有者权益合计1', required=False)
    suoyouzhe2 = forms.FloatField(label='所有者权益合计2', required=False)
    suoyouzhe3 = forms.FloatField(label='所有者权益合计3', required=False)



