from django.contrib import admin

# Register your models here.
from .models import Grades, Students


# 注册
class StudentsInfo(admin.TabularInline):  # StackedInline
    """需求：在创建一个班级时，可以直接添加2个学生"""
    model = Students
    extra = 2


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]

    def pk(self):
        return self.pk

    def gname(self):
        return self.gname

    def gdate(self):
        return self.gdate

    def ggirlnum(self):
        return self.ggirlnum

    def gboynum(self):
        return self.gboynum

    def isDelete(self):
        if self.isDelete:
            return "已删除"
        else:
            return "未删除"

    isDelete.short_description = "是否删除"
    gname.short_description = "班级名称"
    gdate.short_description = "创立时间"
    ggirlnum.short_description = "女生人数"
    gboynum.short_description = "男生人数"
    pk.short_description = "主键"

    """列表页属性"""
    list_display = [pk, gname, gdate, ggirlnum, gboynum, isDelete]  # 显 示字段
    list_filter = ['gname']  # 过滤字段
    search_fields = ['gname']  # 搜索字段
    list_per_page = 5  # 分页

    """
        添加修改页属性
        注意：fields与fieldsets不能同时使用
    """
    # fields = ['ggirlnum', 'gboynum', 'gname', 'gdate', 'isDelete']      #规定属性的先后顺序
    fieldsets = [
        ("人数", {"fields": ['ggirlnum', 'gboynum']}),
        ("基本信息", {"fields": ['gname', 'gdate', 'isDelete']}),
    ]  # 给属性分组


# admin.site.register(Grades, GradesAdmin)


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):

    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    def age(self):
        return self.sage

    def name(self):
        return self.sname

    def pk(self):
        return self.pk

    def contend(self):
        return self.scontend

    def grade(self):
        return self.sgrade

    def isDelete(self):
        if self.isDelete:
            return "已删除"
        else:
            return "未删除"

    # 设置页的列的名称
    gender.short_description = "性别"
    age.short_description = "年龄"
    name.short_description = "姓名"
    pk.short_description = "主键"
    contend.short_description = "说明"
    grade.short_description = "所在班级"
    isDelete.short_description = "是否删除"
    list_display = [pk, name, age, gender, contend, grade, 'lastTime', 'createTime', isDelete]  # 显 示字段
    list_filter = ['sname']  # 过滤字段
    search_fields = ['sname']  # 搜索字段
    list_per_page = 5  # 分页
    
    readonly_fields = ('lastTime', 'createTime')

    fieldsets = [
        ("班级", {"fields": ['sgrade']}),
        ("基本信息", {"fields": ['sname', 'sage', 'sgender', 'scontend', 'isDelete']}),
        ("时间", {"fields": ['lastTime', 'createTime']}),
    ]

    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True


# admin.site.register(Students, StudentAdmin)
