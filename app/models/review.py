from peewee import CharField, DateTimeField, BigAutoField, IntegerField, FloatField

from app.repository.base_model import BaseModel
from app.utils.constants import TABLE_REVIEW


class Review(BaseModel):

    id = BigAutoField(primary_key=True)
    book_id = IntegerField(null=False)
    rating = IntegerField(null=False)
    review = CharField(max_length=250)
    create_date = DateTimeField(null=False)
    update_date = DateTimeField(null=False)

    class Meta:
        table_name = TABLE_REVIEW
