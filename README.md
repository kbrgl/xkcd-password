# xkcd password generator
![](http://imgs.xkcd.com/comics/password_strength.png)
### Languages in which I've implemented this
* Python (compatible with both 2 and 3)
* [Ruby](https://github.com/kbrgl/xkcd-password-rb)

### "What word list are you using?"
I'm using a word list I found at [a GitHub repo called 'google-10000-english'](https://github.com/first20hours/google-10000-english). However, you can use pretty much any word list for this.

### "How the heck do I use this thing?"
If you just want a password then just clone the repo and run the Python script. The script will run on both Python 2 and Python 3 (:D).

#### Using the code
Initialize the XkcdPasswordGenerator object with the word list you want to use. Call the generate() method. You can retrieve individual words with the random_word() method.
* In case you are using an external word list file, there's a parse() function that you can use.

Here's an example:
```python
generator = XkcdPasswordGenerator(parse('dictionary.csv', delimiter=',')) # you can omit the delimiter because it is ',' by default, but I've included it here for clarity
generator.generate() #=> 'correct horse battery staple'
generator.generate(3, None) #=> ['correct', 'horse', 'battery', 'staple']
generator.random_word() #=> 'battery'
```

