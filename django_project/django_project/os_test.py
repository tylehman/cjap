import os
print 'os.path.dirname(os.path.realpath(__file__)) = ' + os.path.dirname(os.path.realpath(__file__))
print 'os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))' + os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

STATICFILES_DIRS = [
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "static"),
]

print 'STATICFILES_DIRS = ' , STATICFILES_DIRS
