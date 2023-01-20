import screeninfo
print(screeninfo.get_monitors())


si = str(screeninfo.get_monitors())
si = si.split()
dp = """name='\\\\.\\DISPLAY2',"""
if dp in si:
    print(ok)

else:
    pass

