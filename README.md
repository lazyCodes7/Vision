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
How to get ChromeDriver?
![Screenshot from 2021-05-10 10-48-58](https://user-images.githubusercontent.com/53506835/117609318-6c3e9080-b17d-11eb-81e7-d468057e4119.png)

