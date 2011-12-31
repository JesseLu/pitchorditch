import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/redirect" method="post">
                <div><input type="field" name="deckurl"></div>
                <div><input type="submit" value="Submit"></div>
              </form>
            </body>
          </html>""")


class Redirect(webapp.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('deckurl')))
        self.response.out.write(cgi.escape(self.request.url))
        self.response.out.write('</pre></body></html>')
        str = cgi.escape(self.request.get('deckurl')).split('?id=')

        self.redirect('/b?id=' + str[1])
        # self.redirect('/id')

class Submission(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.url))
        self.response.out.write('</pre></body></html>')

        

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/redirect', Redirect),
                                      ('/b', Submission)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
