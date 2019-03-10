# Exercise 8: _Kibana_ visualizations — practice

The purpose of this exercise is to practice the data visualization capabilities of _Kibana_. Feel free to take inspiration from the solutions in [exercise 6](exercise6.md).

## a) What was the average age of the people hired in each year in the different companies? (vertical bar chart)

> :information_source: Note that you will have to use two aggregations to create this visualization. By default, _Kibana_ stacks the data for the different companies on top of each other. For our use-case it would be much better if these would be next to each other instead. Fortunately, you can set this if you choose the _Mode_ called _normal_ instead of _stacked_ under the _Mertics & Axes_ settings.

> :heavy_exclamation_mark: Make sure to set the _Metrics_ to _Average_ instead of _Count_!

> :memo: Create a screenshot of the visualization and save it as `exercise-8\a.png`.

> :memo: Save and export the visualization. Save the exported file as `exercise-8\a.json`.

## b) What is the distribution of the workers between the various companies in the state of New York (NY)? (pie chart)

> :memo: Create a screenshot of the visualization and save it as `exercise-8\b.png`.

> :memo: Save and export the visualization. Save the exported file as `exercise-8\b.json`.

## c) What is the average salary of the workers aged between 18 and 30 in the various states? (map)

> :heavy_exclamation_mark: Make sure to set the _Metrics_ to _Average_ instead of _Count_!

> :memo: Create a screenshot of the visualization and save it as `exercise-8\c.png`.

> :memo: Save and export the visualization. Save the exported file as `exercise-8\c.json`.