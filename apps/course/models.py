"Модели курсов в учебных заведениях и работ студентов"

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    "Модель дисциплины"
    name = models.CharField(verbose_name="Name", max_length=100)
    description = models.TextField(verbose_name="Description")
    students = models.ManyToManyField(
        User, related_name="courses", verbose_name="Students"
    )
    created = models.DateField(verbose_name="Creation date", auto_now_add=True)

    class Meta:
        "Meta data"
        verbose_name_plural = "Courses"


class CourseAssignment(models.Model):
    "Модель сданной работы"
    owner: User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignments", verbose_name="Owner"
    )
    course: Course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="assignments", verbose_name="Course"
    )
    comment = models.TextField(verbose_name="Comment")
    file = models.FileField(verbose_name="File", upload_to="assignments/")
    created = models.DateTimeField(verbose_name="Creation date", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Update date", auto_now=True)

    class Meta:
        "Meta data"
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"
