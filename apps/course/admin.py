"Модуль настройки админ панели"

from django.contrib import admin

from .models import Course, CourseAssignment

class AssignmentInline(admin.StackedInline):
    "Assignment inline"
    model = CourseAssignment
    extra = 0
    show_change_link = True


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    "Course admin panel"
    list_display = ('id', 'name', 'created')
    list_display_links = list_display
    search_fields = ('id', 'name')

    inlines = [AssignmentInline]


@admin.register(CourseAssignment)
class CourseAssignmentInline(admin.ModelAdmin):
    "Course assignments admin panel"
    list_display = ('id', 'created')
    list_display_links = list_display
    list_filter = ('owner',)
