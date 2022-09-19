import os 

if os.path.exists('env.py'):
    import env

print(os.getenv('test'))