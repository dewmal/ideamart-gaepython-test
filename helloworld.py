from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import simplejson as json
from google.appengine.api import urlfetch


class MainPage(webapp.RequestHandler):    
    
    def get(self):
        logging.info(self.request)        
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Accept'] = 'application/json'
        self.response.out.write('Hello, webapp Worldasdas dada!')
        
        
    def post(self):    
        
        url='http://localhost:7000/sms/send'
        
        res = { 'message':'Hello',
"destinationAddresses":["tel:94771122336"],
"password":"password",
"applicationId":"APP_000001"
}

        logging.info(res)
        form_data = json.dumps(res)
        logging.info(form_data)
        result = urlfetch.fetch(url=url,
                        payload=form_data,
                        method=urlfetch.POST,
                        headers={'Content-Type': 'application/json','Accept':'application/json'})
        
        
        logging.info(result.content)
        
        if result.status_code == 200:
            logging.info(result.content)  
        


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    
    main()
