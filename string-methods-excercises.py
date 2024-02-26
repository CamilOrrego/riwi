## Capitalize firs letter of each word
my_name = "juan perez"
print(my_name.title())

## Capitalize the whole word
book_name = "el hombre en busca de sentido"
print(book_name.upper())

## Replace upper and spaces for lower and hyphen
slug = "Hola Mundo Python"
print(slug.lower().replace(" ","-"))

## Remove spaces at the start and the end
spaces = " hola mundo "
print(spaces.strip())

## Extract e-mail domain
domain = "usuario@example.com"
print(domain.split("@")[1])

## Replace dots with spaces
dots = "hola.mundo"
print(dots.replace(".", " "))

## Find first occurrence of Python
occurrence = "Aprendiendo Python en OpenAI"
print(occurrence.find("Python")) 

## Find if the string is numeric
number = "1234"
print(number.isnumeric())

## Capitalize the fisrt letter of the sentence
sentence = "este es un titulo"
print(sentence.capitalize())

## Convert to lower cases
warning = "¡ESTE ES UN AVISO!"
print(warning.lower())

## Remove the quotation marks
quotes = "¨importante¨"
print(quotes.replace("¨", ""))

## Split a sentence in words
text = "hola mundo python"
print(text.split(" "))

## Replace spaces by underscores
under = "hola mundo python"
print(under.replace(" ", "_"))

## Find the position of a word
keyword = "la palabra clave esta aqui"
print(keyword.index("clave"))

## Verify if the string is numeric
zipcode = "33166"
print(zipcode.isnumeric())

