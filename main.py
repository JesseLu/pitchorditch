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
        str = cgi.escape(self.request.get('deckurl')).split('?id=')
        self.redirect('/b?id=' + str[1])

class Submission(webapp.RequestHandler):
    def get(self):
        deck = cgi.escape(self.request.url).split('?id=')[1]
        self.response.out.write('<html><body>')
        self.response.out.write("""
            <iframe src="https://docs.google.com/present/embed?id=%s" 
                frameborder="0" width="410" height="342">
            </iframe>
            """ % deck)
        self.response.out.write("""
            <div id="disqus_thread"></div>
            <script type="text/javascript">
                /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
                var disqus_shortname = 'pitch-ditch'; // required: replace example with your forum shortname

                /* * * DON'T EDIT BELOW THIS LINE * * */
                (function() {
                    var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                    dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
                    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
                })();
            </script>
            <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
            <a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>
            """)
        self.response.out.write('</body></html>')

        

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/redirect', Redirect),
                                      ('/b', Submission)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ 	== "__main__":
    main()	
