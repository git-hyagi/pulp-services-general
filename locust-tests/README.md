# INSTALL

```
pip3 install locust
```

# CONFIGURING

* create a settings.py file with the following format:
```
cert = (<my certificate>,<my cert private key>)
proxy = {<proxy proto (http|https)>: <proxy url>}
```

* for example:
```
cert = ('/home/user/my_cert.crt','/home/user/my_cert.key')
proxy = {"https": "http://my-proxy.example.com:1234"}
```

# RUNNING

```
locust -f test1.py --host https://<pulp host> --users 10 --spawn-rate 10
```


* let it running for 5 minutes
```
locust -f test1.py --host https://<pulp host> --users 10 --spawn-rate 10 -t 5m  --headless
```


# DOC

[Locust quickstart](https://docs.locust.io/en/stable/quickstart.html)