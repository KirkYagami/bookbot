content = 'sdhjkgcsdhjgc'

def character_count(content):
    d = {}
    for i in content:
        d[i] =d.get(i, 0)+1
    return  d

print(character_count(content))