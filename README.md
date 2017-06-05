elastic-beanstalk-nginx-uwsgi-django
====================================

A Django sample app running with uWSGI and Nginx on AWS Elastic Beanstalk.


```
$ eb init
$ eb create dev-env -p "64bit Amazon Linux 2017.03 v2.4.0 running Python 2.7" --single -i t2.micro --service-role aws-elasticbeanstalk-service-role --sample 
```

Setup environment properties:

```
$ eb setenv ALLOWED_HOSTS=ebsample.guoyong.me,dev-env.jtfiebamft.us-west-2.elasticbeanstalk.com \
  DATABASE_URL=mysql://user:pass@host:3306/dbname?charset=utf8mb4 \
  DEBUG=off \
  DJANGO_SETTINGS_MODULE=ebsample.settings \
  SECRET_KEY=<secret key> \
  WSGI_MODULE=ebsample.wsgi 
```

![Software Configuration](https://raw.githubusercontent.com/wolfg1969/elastic-beanstalk-nginx-uwsgi-django/master/static/images/Software%20Configuration.png)

```
$ eb deploy
or 
$ eb deploy --staged

$ eb open
```

Change History:

* (06/05/2017): Works with latest platform '64bit Amazon Linux 2017.03 v2.4.0 running Python 2.7'. 
* (04/07/2017): Create a super user 'admin' for Admin Site, the initial password is **first 8 characters of your SECRET_KEY**. 
* (04/07/2017): Upgraded platform to 64bit Amazon Linux 2016.09 v2.3.3 running Python 2.7. 
* (01/29/2017): Configure uWSGI module parameter via environment variable.
* (01/29/2017): Upgraded platform to 64bit Amazon Linux 2016.09 v2.3.1 running Python 2.7.
* (12/26/2016): Now running on "64bit Amazon Linux 2016.09 v2.3.0 running Python 2.7".
* (12/12/2016): Works with "64bit Amazon Linux 2016.09 v2.2.0 running Python 2.7".
* (07/02/2016): Works with "64bit Amazon Linux 2016.03 v2.1.3 running Python 2.7".
* (05/29/2016): Use django-environ to read configurations from EB env file.
* (05/29/2016): Works with "64bit Amazon Linux 2016.03 v2.1.0 running Python 2.7".
* (02/21/2016): Works with "64bit Amazon Linux 2015.09 v2.0.7 running Python 2.7".
* (07/09/2015): Now it's compatible with "64bit Amazon Linux 2015.03 v1.4.3 running Python 2.7".
