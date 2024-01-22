from models import Author, Quote
import json
from connect import db
from mongoengine import ObjectIdField

def get_autor(autors, name):
    for i in autors:
        if i['fullname'] == name:
            return(i)

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
        # quote_author = get_autor(autors,i['author'])
        quote = Quote(
            tags = i['tags'],
            author =i['author'],
             
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

    

