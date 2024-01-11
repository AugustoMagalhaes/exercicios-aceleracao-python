from jinja2 import Template


TEMPLATE_STRING = "Eu sou um {{ nome }}!"
template = Template(TEMPLATE_STRING)

output = template.render(nome='template')

print(output)
