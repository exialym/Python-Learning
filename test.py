data = {'name': "Albert O'Connor", 'favorite_color': 'green'}
print('{0}'.format(data)) # This prints the dictionary as text
data = {'name': "Albert O'Connor", 'favorite_color': 'green'}
# There we go, name and favorite_color are passed as keywords.
# 这里只将字典的键传了进去
print('Hello, {name}! Your favorite color is {favorite_color}.'.format(**data))