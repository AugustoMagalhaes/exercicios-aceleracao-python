from jinja2 import Environment, FileSystemLoader

# Configurando um loader
loader = FileSystemLoader('filters')

environment = Environment(loader=loader)

template = environment.get_template('filters.html')


data = {
    'name': 'a primeira letra vai ficar maiúscula',
    'to_upper': 'todas as letras vão ficar maiúsculas',
    'to_lower': 'TODAS AS LETRAS VÃO FICAR MINÚSCULAS',
    'my_list': [0, 1, 2, 3, 4, 5],
    'text': 'Esse texto irá ser truncado'
}

output = template.render(data)

print(output)
