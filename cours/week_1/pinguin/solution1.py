p_hair      = '   _~_    '
p_eye       = '  (o o)   '
p_mounth    = ' /  V  \  '
p_body      = '/(  _  )\ '
p_legs      = '  ^^ ^^   '
print('Write pls number of pinguins')
number = int(input()) # количество пингвинов
print(p_hair * number, p_eye * number, p_mounth * number, p_body * number, p_legs * number, sep='\n')