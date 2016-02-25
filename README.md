# xkcd password generator
![](http://imgs.xkcd.com/comics/password_strength.png)
### Languages in which I've implemented this
* Python (compatible with both 2 and 3)
* [Ruby](https://github.com/kbrgl/xkcd-password-rb)

### "How the heck do I use this thing?"
If you just want a password then just clone the repo and run the Python script. The script will run on both Python 2 and Python 3 (:D).

#### Using the code
1. Initialize the XkcdPasswordGenerator object with the a list of words you want to use.
2. Call the generate() method. It accepts 2 arguments: the number of words, and, optionally, a separator. The words in the returned string will be separated by separator. If you pass in None as a separator, an array is returned instead.

Tip: You can retrieve individual words with the random_word() method.

Here's an example:
```python
with open('words.csv') as f:
  words = [line for line in f.read().split(sep=',')]

generator = XkcdPasswordGenerator(words)
generator.generate() #=> 'correct horse battery staple'
generator.generate(4, None) #=> ['correct', 'horse', 'battery', 'staple']
generator.random_word() #=> 'battery'
```

