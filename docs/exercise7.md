# Exercise 7: _Kibana_ visualizations — practice

The purpose of this exercise is to practice the data visualization capabilities of _Kibana_. Feel free to take inspiration from the solutions in [exercise 5](exercise5.md).

## Create three visualizations to answer the following questions

- a) What was the _average_ age of the people hired in each year in the different companies?

  Use a _vertical bar chart_ for visualization.

  Tips:

  - You will have to use two aggregations to create this visualization. By default, Kibana stacks the data for the different companies on top of each other. For our use-case it would be much better if these would be next to each other instead. Fortunately, you can set this if you choose the _Mode_ called _normal_ instead of _stacked_ under the _Metrics & Axes_ settings.
  - Make sure to set the _Metrics_ to _Average_ of _age_ instead of _Count_!

- b) What is the distribution of the workers between the various companies in the state of New York (NY)?

  Use a _pie chart_ for visualization.

- c) What is the _average_ salary of the workers aged between 18 and 30 in the various states?

  Make sure to set the _Metrics_ to _Average_ of _salary_ instead of _Count_!

  Use a _region map_ for visualization.

## Create a dashboard

When all three visualizations are ready, create a new dashboard and add the visualizations onto this dashboard.

1. Click on the _Dashboard_ item on the left side menu.

1. Create a new dashboard here.

1. Use the _Add_ button on the dashboard to add existing visualizations. Add the three you created in this exercise.

1. You can drag and drop them on the dashboard to various places, change their size, etc.

1. Save the dashboard (just like you saved each visualization).

1. Create a screenshot of this dashboard and save it as `ex7.png`. The screenshot should show the entire dashboard with all three visualizations visible.

1. Export the dashboard _ndjson_ file as `ex7.ndjson`, as done previously, but this time also **include related objects** (this is a setting in Kibana when exporting).

## Submit your solution

See instructions in [exercise 1](exercise1.md) to submit your solution.
