from models import Author, Quote
from seed import get_autor

from cache import cache


def input_parser(user_input: str):
    try:
        u_input = user_input.split(':')
        if len(u_input) >=2:
            command = u_input[0].casefold()
            args = u_input[1].strip()
            return command, args
        else:
            raise IndexError
    except IndexError as err:
        print('\033[31m\tWrong input - no args found')


@cache
def quotes_by_author(name: str):
    author = get_autor(name)
    if not author:
        return f"\033[31m\tAuthor {name} not found\033[0m"

    quotes = Quote.objects(author=author)
    if not quotes:
        return f"\033[31m\tNo quotes found for {name}.\033[0m"

    return f"\033[32m{name} said:\n \033[0m" + '\n'.join(['\t' + quote.quote for quote in quotes])


@cache
def quotes_by_single_tag(tag: str):

    quotes = (Quote.objects(tags=tag))

    if not quotes:
        return f"\033[31m\tNo quotes found for tag/tags: \"{tag}\"\033[0m"

    return f"\033[32mTag {tag} is for notes:\n \033[0m" + '\n'.join(['\t' + quote.quote for quote in quotes ])


@cache
def quotes_by_list_of_tags(tags: str):
    tags_to_search = tags.split(',')
    quotes = (Quote.objects(tags__in=tags_to_search))

    if not quotes:
        return f"\033[31m\tNo quotes found for tag/tags: \"{tags}\"\033[0m"

    return f"\033[32mTags {tags} are for notes:\n \033[0m" + '\n'.join(['\t' + quote.quote for quote in quotes])


def main():
    while True:
        user_input = input('\033[33mPlease, enter the command: parameter(s): \033[0m')

        if user_input == 'exit':
            break

        elif ':' not in user_input or len(user_input.split(':'))<1:
            print('\033[31m\tWrong command\033[0m')

        else:
            command, args = input_parser(user_input)

            if command == 'name':
                print(quotes_by_author(args))

            elif command == 'tag':
                print(quotes_by_single_tag(args))

            elif command == 'tags':
                print(quotes_by_list_of_tags(args))


            else:
                print('\033[31m\tWrong command. Please, use "name", "tag" or "tags".\033[0m')

        
if __name__ == '__main__':
    main()
