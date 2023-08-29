import graphene
from graphene_django import DjangoObjectType
from books.models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields= ("id","title","desc", "created_at", "updated_at")
class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello World!")
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())

    def resolve_books(self, info):
        return Book.objects.all()

    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)

schema = graphene.Schema(query=Query)