SendGrid Python Django Sample App
=================================

This git repository helps you to send emails quickly and easily through SendGrid using Python and Django.

Create an SendGrid account at http://sendgrid.com/pricing.html

Clone SendGrid application on your local machine
<pre>
    git clone https://github.com/sendgrid/sendgrid-python-django-sample-app.git
</pre>

###Install SendGrid library###

    pip install sendgrid==0.3.1

###Configuration###

Configure `SGapp/views.rb` file with your information:

Update the *&lt;sendgrid_username&gt;* and *&lt;sendgrid_password&gt;* with your SendGrid credentials.
```python
    sg = sendgrid.SendGridClient('<sendgrid_username>', '<sendgrid_password>')
```

###Start python server ###

    python manage.py runserver
    # or
    python manage.py runserver 0.0.0.0:8000
    
For more information you can visit our [Python Library](https://github.com/sendgrid/sendgrid-python)