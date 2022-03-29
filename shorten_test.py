import pytest 
import app



def test_shorten_lengthen():
    assert app.expand(app.shorten("https://www.google.com")) == "https://www.google.com"
    assert app.expand(app.shorten("https://www.google.com/search?q=test")) == "https://www.google.com/search?q=test"
    assert app.expand(app.shorten("www.google.com/search?q=test&q=test")) in ["http://www.google.com/search?q=test&q=test", "https://www.google.com/search?q=test&q=test"]
