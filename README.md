# Icelander generator
Icelander generator is a tool made to generate a bunch of icelanders.

## Details
Icelander generator uses a list of male and female names scraped from is.wikipedia.org and
the kennitala pypi package (https://pypi.org/project/kennitala/) to generate random people
with proper icelandic names and kennitala. It can be very useful for testing purposes where
a bunch of icelanders are required. Can also just be used for fun, I guess.

## Installation
Inside your virtualenv run
```
$ pip install icelander-generator
```

## Usage
```python
from icelander_generator import Icelander

icelander = Icelander()

icelander.get_random_person()
# Returns {
#   'ssn': '{random ssn}',
#   'gender': '{randomly selected gender},
#   'firstname': '{randomly selected first name based on gender}',
#   'lastname': '{randomly selected last name based on gender}',
# }

icelander.get_random_person(gender='female', year=1981)
# Returns {
#   'ssn': '{random ssn from year 1981}',
#   'gender': 'female',
#   'firstname': '{randomly selected first name based on gender}',
#   'lastname': '{randomly selected last name based on gender}',
# }

icelander.get_random_people(10)
# Returns a list of randomly generated people of random age and gender

icelander.get_random_people(10, gender='female', year=1981)
# Returns a list of randomly generated women born in 1981

icelander.dump_random_people_to_file(filename='dump.json', num_people=10, gender='female', year='1981')
# Dumps result from get_random_people to a json file
```


## Future ideas
- Add proper addresses and postal codes
- Add method to create families of various family types
- More gender options?
- Middle names
- Company generator

I'm also open for suggestions and pull requests on https://github.com/7oi/IcelanderGenerator
