id=1

def admin_only(f):
    def wrapper():
        print("Start")
        if id==1:
            f()
        print("End")
    
    return wrapper


@admin_only
def link():
    print("Create link")
    
link()
  

