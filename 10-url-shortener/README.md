# Challenge: Build a URL Shortener

Write a RESTful web application that registers shortened URLs with their full URL counterpart.

When a short URL is requested the application should redirect to the matching full URL.

The goal of this exercise is to play with data persistence and dabble with some HTTP interactions.  With that in mind, the focus is not to be feature rich or observe standard web security concerns.

## Requirements

- Your application should persist data in between restarts (you're encouraged to try out [sqlite3][sqlite] in the standard library).
- You may use the web framework of your choice.  If you're not sure where to start, check out [Flask][flask] and a decent [introduction][flask_intro].

You have flexibility in how you design the API, but in general:
- Accept the long form of a URL and generate a corresponding short URL that can be requested later.
- The service should redirect to the long URL when the short URL is requested.   If the short URL isn't registered the service should respond with an `HTTP 404`.
- *Optional:* keep statistics for each short URL showing information about how many times it has been requested.


[sqlite]: https://docs.python.org/3/library/sqlite3.html
[flask]: http://flask.pocoo.org/
[flask_intro]: https://www.fullstackpython.com/flask.html
