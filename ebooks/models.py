from django.db.models import (
    CharField, TextField, Model, PositiveIntegerField, DateField, DateTimeField, ForeignKey, CASCADE
)
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Ebook(Model):
    title = CharField(max_length=140)
    author = CharField(max_length=60)
    description = TextField()
    publication_date = DateField()

    def __str__(self):
        return self.title


class Review(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    review_author = ForeignKey(User, on_delete=CASCADE)
    review = TextField(blank=True, null=True)
    rating = PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    ebook = ForeignKey(Ebook, on_delete=CASCADE, related_name="reviews")

    def __str__(self):
        return str(self.rating)
