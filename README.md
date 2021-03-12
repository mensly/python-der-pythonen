# Python der Pythonen

This project aims to close to loop on making it relevant to segue from talking about Python back to
its namesake, Monty Python. The secondary goal is to provide new Monty Python content when this lot
all kick the bucket.

![Living Members of Monty Python](images/graph.png)

Note that the above graph explicitly recognises that Loretta no longer wants to be considered a 
white male for the purposes of finding blame for everything that is wrong with the world.


## Running

First clone the repository and install dependencies:
```
pip install -r requirements.txt
```

Next you will need to download some input data in the `input` directory, which can be found 
[online](https://www.intriguing.com/mp/scripts.php). If Monty Python's lawyers have this taken down,
I'll throw them under a camel. Assuming you're lazy, this can be done for you:
```
./fetch-data.py
```

You can then force your computer to read nonsense:
```
./training.py
```

Finally, you can generate something funny:
```
./generate.py
```


## Sample Output
TODO
