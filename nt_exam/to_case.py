def to_case(s):
    if '_' in s:
        # Convert to camelCase
        words = s.split('_')
        return words[0] + ''.join(word.capitalize() for word in words[1:])
    else:
        # Convert to snake_case
        return ''.join('_' + c.lower() if c.isupper() else c for c in s).lstrip('_')


print(to_case('camel_case'))   # 'camel_case'
print(to_case('snakeCase'))    # 'snakeCase'


