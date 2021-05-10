# Vision
Making Facebook accessible to the blind!\
About FacebookAutomater.py:\
Usage:
```python
fb = FacebookAutomater()
```
Initiate chrome:
```python
fb.initiate_chrome()
```
Make sure to have Chromedriver installed!

Load facebook:
```python
fb.page_load()
```
Login to facebook
```python
fb.do_login("Number","Password")
```

Create a post:
```python
fb.page_posting("This is a post")
```

Logout:
```python
fb.do_logout()
```
