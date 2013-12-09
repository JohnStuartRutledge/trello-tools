## Just tinkering with the Trello API

#### To test counting burndown totals
```
python run.py
```

#### Or if you have your auth_token already
```
python run.py <auth_token>
```

#### You should get some output like this
```python
Initializing Trello Client...
Visit this URL in your browser: https://trello.com/1/OAuthAuthorizeToken?oauth_token=d0d2dc09f6314123dab478f2297f472d
Enter PIN from browser: c9f594b4b038695312a730e1709f1152
Connected to Trello!
* could not parse: Backend support for m. sites (add app_domain)
{'estimated': 349.5, 'actual': 296.5}
```

