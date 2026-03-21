import re

for filename in ['ldn_full_script.ipynb', 'OD_full_script.ipynb']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<<<<<<< HEAD\n(.*?)=======\n.*?>>>>>>> [^\n]+\n',
        r'\1',
        content,
        flags=re.DOTALL
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Fixed: {filename}')

