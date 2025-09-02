from django.db import models

class SchoolLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # --- Change this line from FileField to URLField ---
    pdf_file = models.FileField(upload_to='chapters/', blank=True, null=True)

    def __str__(self):
        return self.title

# courses/models.py

class Exercise(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='exercises/', blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Exam(models.Model):
    title = models.CharField(max_length=200)
    level = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='exams/')
    with_solution = models.BooleanField(default=False)

    def __str__(self):
        return self.title