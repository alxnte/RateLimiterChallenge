# RateLimiterChallenge
API rate limiting coding exercise. 

A rate limiter is a tool that monitors the number of requests per a window of time a service agrees to allow. 
If the request count exceeds the number agreed by the service owner in a decided window time, the rate limiter will reject subsequent calls. 
The rate limiter should limit requests per client by IP address.


Verified acceptance criteria:
- A class that can be used by an API to rate limit incoming requests.
- A function, constructor, or factory method to instantiate an instance that takes an interval in milliseconds and a count that specifies the numbers of calls allowed.
- A function that checks to see if the limit has been reached.
- Limits requests per unique IP address and support any number of clients.
- Verified via HTTP server built using Flask.
