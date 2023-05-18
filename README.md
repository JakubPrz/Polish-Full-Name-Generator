# Polish Full Name Generator
**Author:** Jakub Przepiórka \
**Version:** 1.0.2


## About
The pfng is powered by thousands of Polish names and surnames, which allows you to generate thousands combinations of unique full names.
You can choose whether you want to generate male or female full names or mix of them.

**Why it is useful tool?**
- Forget about inventing or manually typing names and surnames. This polish full name generator can generate you quickly thousands of full names.
- It can be useful when generating fake data or testing some applications.

**No dependencies** \
This package does not depend on other modules or packages that are not already included in standard Python distributions.

**Operating system** \
This package is written to work on Windows. There is no guarantee that it will work on other operating systems.


## Installation
The preferred channel is [PyPI](https://pypi.org/project/pfng/):
```
pip install pfng
```

Alternatively, you can clone GitHub [repository](https://github.com/JakubPrz/Polish-Full-Name-Generator):
```
git clone git@github.com:JakubPrz/Polish-Full-Name-Generator.git
```


## Usage
```python
from pfng import generate_full_names


people = generate_full_names(number=20, gender='M&F')

# Example 1: you can print them
for p in people:
    print(p)

# Example 2: save them to file for later use
with open("full_names.txt", mode="w", encoding="utf-8") as file:
    for f in people:
        file.write(f + "\n")
```

The ```gender``` parameter options:

| Option | Meaning                           |
|--------|-----------------------------------|
| M      | Only male full names              |
| F      | Only female full names            |
| M&F    | Mix of male and female full names |


## Generated full names sample
*['Waldemar Jastrząb', 'Marek Suliński', 'Nela Orawiec', 'Dagmara Czeczko', 'Aneta Makaruk', 'Laura Krężel', 'Janusz Gumułka', 'Iza Łuka', 'Ala Orzeł', 'Roksana Pilichowska', 'Nela Berus', 'Lila Gabryel', 'Mateusz Czopor', 'Alfred Dorsz', 'Anna Kanabus', 'Jerzy Bojek', 'Szymon Prędki', 'Adam Pondel', 'Julian Wichary', 'Sylwester Ogrodowczyk', 'Kajetan Parka', 'Witold Purtak', 'Urszula Opałka', 'Kazimiera Zawół', 'Ola Kuskowska', 'Szczepan Tokaj', 'Edward Pasierbek', 'Tymon Pielach', 'Maurycy Block', 'Remigiusz Wasiela']*

**Note:** There are only **Polish** full names because it's Polish Full Name Generator.


## Contributing
Contributions are welcome! \
If you would like to make any improvements to this generator, feel free to submit a pull request.


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.