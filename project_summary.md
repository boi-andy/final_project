# Project Summary

I will be exploring the different types of planets in the Star Wars galaxy. Part of this research will include the planet's size, teerrain, and population. I will also be using data that show what characters are from each planet and the character's features, including type of species, height, weight, and home world.

## Introduction and Motivation

The story of how I came to this project can be found on my blog post [Data Collection for Star Wars](https://boi-andy.github.io/my-blog/2023/11/10/data-collection.html).

## Methods

The methods I used can also be found on the same blog post [Data Collection for Star Wars](https://boi-andy.github.io/my-blog/2023/11/10/data-collection.html). <br>

I The original publishers of the Star Wars used to use a website called swampi.co. After their API was abused, they shut down thee website and created a new one: [swampi.dev](https://swapi.dev/). This has data on all plaents, spaceships, vehicles, people, films, and species in each of the first 7 Star Wars films. 

## Results

I was most interested in the planets of the Star Wars Galaxy. I wanted to know how they compared to each other and how population size is related to planet size.  The process of finding these results can be found on my blog post [EDA for Star Wars Planets](https://boi-andy.github.io/my-blog/2023/11/14/EDA.html).

## Conclusion

The correlation coefficent of the realtionship between the diameter and population of a planet is 0.33 and has a R-squared value of 0.11. This tells us that the relationship between the two variables are quite weak. You can seee that most of the populations are low amongst the averaged sized planets. There are certain planets like Coruscant that has a population of 1 trillion inhabitants but an average diameter of just over 12,000 km. This is insufficent evidence to say that the size of a planet will have an effect on its population.

If you would like to play around with specific details of each planet and see the characters from each planet, visit my [Streamlit app](https://starwarsplanets.streamlit.app/).

