from flask import Flask
from flask_mail import Mail, Message
   
app = Flask(__name__)

# Mail Global Configuration
# https://pythonhosted.org/Flask-Mail/
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'spof.flood@gmail.com'
app.config['MAIL_PASSWORD'] = 'c3Nrt8VdE3ToYNIBEmVl'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# the mail object instantiated from the class Mail
mail = Mail(app)
   
# message object mapped to the index route
@app.route("/")
def index():
   msg = Message('Hello, this is a test', sender ='spof.flood@gmail.com', recipients = ['xixeko6152@dedatre.com'])
   msg.body = 'This is a Flask message sent from Flask-Mail'
   mail.send(msg)

   return 'Your message has been sent'
   
if __name__ == '__main__':
   app.run(debug = True)