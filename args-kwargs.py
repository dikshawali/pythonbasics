def jointogether(*args111, **kwargs):
    newstr=', '.join(args111)
    newstr1=kwargs.keys+' is the meaning of '+kwargs.values
    return newstr+'\n'+' is the result'

print(jointogether('Diksha', 'wali', 'ishani', 'wali', 'hello'))