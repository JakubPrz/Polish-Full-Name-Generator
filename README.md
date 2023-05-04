# Polish Full Names Generator
**Author:** Jakub Przepiórka \
**Version:** 1.0.0

## About
The generator is powered by thousands of Polish names and surnames, which allows you to create many thousands of combinations of unique full names.

You can choose whether you want to generate male or female full names or both of them.

This generator can help quickly insert thousands of users to database, rather than having to manually enter names for each person. It can also be useful when testing booking systems or other applications.

Programming language: Python

## Installation
~~Install it using pip:~~ \
~~> `pip3 install ...`~~

Or clone this repository:
> `git clone git@github.com:JakubPrz/Polish-Full-Names-Generator.git`

## Usage
```python
    from pfng import generator
    
    people = generator.generate_full_names(number=20, gender='M&F')
    
    # ex1: you can print them
    for p in people:
        print(p)
    
    # ex2: or save them to file
    with open("generated_full_names.txt", mode="w", encoding="utf-8") as file:
    for f in people:
        file.write(f + "\n")
```

## Generated people sample
*['Waldemar Jastrząb', 'Marek Suliński', 'Nela Orawiec', 'Dagmara Czeczko', 'Aneta Makaruk', 'Laura Krężel', 'Janusz Gumułka', 'Iza Łuka', 'Ala Orzeł', 'Roksana Pilichowska', 'Nela Berus', 'Lila Gabryel', 'Mateusz Czopor', 'Alfred Dorsz', 'Anna Kanabus', 'Jerzy Bojek', 'Szymon Prędki', 'Adam Pondel', 'Julian Wichary', 'Sylwester Ogrodowczyk', 'Kajetan Parka', 'Witold Purtak', 'Urszula Opałka', 'Kazimiera Zawół', 'Ola Kuskowska', 'Szczepan Tokaj', 'Edward Pasierbek', 'Tymon Pielach', 'Maurycy Block', 'Remigiusz Wasiela']*

## Contributing
Contributions are welcome! \
If you would like to make any improvements to this generator, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.