# xkcd password generator
![](http://imgs.xkcd.com/comics/password_strength.png)
### Languages in which I've implemented this
* Python (compatible with both 2 and 3)
* Ruby

### What word list are you using?
I'm using a word list I found at (a GitHub repo called 'google-10000-english')[https://github.com/first20hours/google-10000-english]. However, you can use pretty much any word list for this.

### How the heck do I use this thing?
If you just want a password then just clone the repo and run either the Python or Ruby script. The Python script will run on both Python 2 and  Python 3 (:D).

In case you want to use the code, usage in Python and Ruby is pretty much the same. Initialize the XkcdPasswordGenerator object with the word list you want to use. Call the generate() method [optional arguments: number of words (4 by default), character by which the words should be separated (if you provide the nil / None object as the separator an array / list is returned instead and if you don't provide anything then a space is used)]. You can retrieve individual words with the random_word() method.
* In case you are using an external word list file, there's a parse() function in both the Ruby and Python versions. Arguments: file you want to parse and delimiter ("\n" by default)

Python example:
```python
generator = XkcdPasswordGenerator(parse('dictionary.csv', ','))
generator.generate() #=> 'correct horse battery staple'
generator.generate(3, None) #=> ['correct', 'horse', 'battery', 'staple']
generator.random_word() #=> 'battery'
generator
```
Ruby example:
```ruby
generator = XkcdPasswordGenerator.new(parse('dictionary.csv', delimiter: ','))
generator.generate #=> 'correct horse battery staple'
generator.generate(words: 4, separator: nil) #=> ['correct', 'horse', 'battery', 'staple']
generator.random_word #=> 'horse'
```
