import graphene
from graphene_django import DjangoObjectType
from books.models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields= ("id","title","desc", "created_at", "updated_at")

class CreateBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        desc = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, title, desc):
        book = Book(title=title, desc=desc)
        book.save()
        return CreateBookMutation(book=book)
    
class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    message = graphene.String()

    def mutate(self, info, id):
        book= Book.objects.get(pk=id)
        book.delete()
        return DeleteBookMutation(message="Book Deleted")
class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello World!")
    books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID())

    def resolve_books(self, info):
        return Book.objects.all()

    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)
    
class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    delete_book = DeleteBookMutation.Field() 

schema = graphene.Schema(query=Query, mutation = Mutation)