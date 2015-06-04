import web  #this is the library import = #include<web.h>
import os   #python built in library

# this is setting up a route and running "hello" class        
urls = (
    '/', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self):  #self is "this"
    	os.system("mkdir mydir")
        return 'Hello world'

if __name__ == "__main__":
    app.run()