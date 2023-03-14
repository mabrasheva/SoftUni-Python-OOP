def tags(tag):
    def decorator(function_ref):
        def wrapper(*args):
            return f"<{tag}>{function_ref(*args)}</{tag}>"

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


@tags('h1')
def to_upper(text):
    return text.upper()


print(join_strings("Hello", " you!"))
print(to_upper('hello'))
