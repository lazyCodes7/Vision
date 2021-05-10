# Vision
Social Media has changed the way we live our lives a lot. Still, this technology has not yet been made accessible to the blind. With Vision, I plan to overcome this barrier that exists for the disabled and let them enjoy social media as well!

## Voice commands provided.
- Providing voice command for loading facebook
- Logging
- Adding posts 
- Reading posts 
- Checking safety around(if speaking passwords)
- Logging out 

## Privacy
- We are not saving anything and ensuring user safety is top priority
- Moreover, we are providing command for checking your surroundings to find persons if any. This would help in being alert to speak credentials

## About Wit.ai
Wit.ai makes it easy for developers to build applications and devices that you can talk or text to. Our vision is to empower developers with an open and extensible natural language platform. 


## Using an automator.
### Usage:
```python
from FacebookAutomater import *
fb = FacebookAutomater()
```
### Initiate chrome:
```python
fb.initiate_chrome()
```

### Load facebook:
```python
fb.page_load()
```
### Login to facebook

```python
fb.do_login("Number","Password")
```

### Create a post:
```python
fb.page_posting("This is a post")
```

### Logout:
```python
fb.do_logout()
```
### How to get ChromeDriver?
![Screenshot from 2021-05-10 10-48-58](https://user-images.githubusercontent.com/53506835/117609318-6c3e9080-b17d-11eb-81e7-d468057e4119.png)

## Ingredients
- Python
- Telegram API
- Graph API
- Wit.ai speech to text
- gTTS
- openCV
- haar-cascades
- Selenium
## Whats next for Vision?
- Covering many more social media sites
- Making a webapp, which would make it even more accessible
- Using Graph API to add features like making a comment, liking a post etc

