elastic-beanstalk-nginx-uwsgi-django
====================================

Configuration sample to setup an Elastic Beanstalk env with custom container settings with Nginx, uWSGI and Django.


```
$ eb init
$ eb create dev-env -p "64bit Amazon Linux 2016.03 v2.1.0 running Python 2.7" --single -i t2.micro --service-role aws-elasticbeanstalk-service-role --sample 
```

Setup environment properties:

![Software Configuration](https://raw.githubusercontent.com/wolfg1969/elastic-beanstalk-nginx-uwsgi-django/feature/use_eb_env_file/static/images/Software%20Configuration.png)

```
$ eb deploy
or 
$ eb deploy --staged
$ eb open
```

Update:
* (05/29/2016): Use django-environ to read configurations from EB env file.
* (05/29/2016): Works with "64bit Amazon Linux 2016.03 v2.1.0 running Python 2.7".
* (02/21/2016): Works with "64bit Amazon Linux 2015.09 v2.0.7 running Python 2.7".
* (07/09/2015): Now it's compatible with "64bit Amazon Linux 2015.03 v1.4.3 running Python 2.7".
