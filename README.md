# dash_ex: 

simple plot.ly dash examples running on a multi page app fully writtend with @Plotly dash. 

[live demo](https://dash-ex.herokuapp.com/)
- loading on heroku free tier takes time (may require page refresh)

### installation

- clone repository
- `pip install -r requirements.txt`
- `cd dash_ex`
- `gunicorn index:server --chdir multi-page-app`
