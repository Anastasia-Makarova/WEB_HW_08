from models import Author, Quote
import json
from connect import db
from mongoengine import ObjectIdField
from cache import cache

@cache
def get_autor( name):
    return Author.objects(fullname__exact=name).first() or Author.objects(fullname__istartswith=name).first()

if __name__ == '__main__':


    with open ('authors.json', 'r', encoding='utf-8') as file:
        autors = json.load(file)
    for i in autors:
        author=Author(
            fullname = i['fullname'],
            born_date = i['born_date'],
            born_location = i['born_location'],
            description = i['description']
            )
        author.save()
        

    with open ('quotes.json', 'r', encoding='utf-8') as file:
        quotes = json.load(file)
    for i in quotes:
 
        quote = Quote(
            tags = i['tags'],
            author = get_autor(i['author']),
             
            #   [ObjectIdField for _ in Author.objects(fullname=i['author'])][0]

                    # fullname = quote_author['fullname'],
                    # born_date = quote_author['born_date'],
                    # born_location = quote_author['born_location'],
                    # description = quote_author['description']
            # ),
            quote = i['quote']
        )
        quote.save()
    #     # print(get_autor(autors,i['author']))

    

