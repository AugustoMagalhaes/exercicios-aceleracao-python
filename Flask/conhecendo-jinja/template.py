from jinja2 import Template


template_file = open('template.html').read()
template = Template(template_file)


SAUDACAO = 'Eu sou um template HTML'

output = template.render(saudacao=SAUDACAO)

print(output)
