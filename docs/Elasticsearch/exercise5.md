# Exercise 5: _Kibana_ visualizations

The purpose of this exercise is to use the data visualization capabilities of _Kibana_.

The following exercises will ask you to create visualizations, then export their Kibana description as JSON, as well as create a screenshot of the visualization itself. When creating the screenshot, make sure the entire visualization with the legend is visible.

## Create an Index pattern

Our first step is to tell _Kibana_ which indexes it should consider when creating the visualizations.

1. Click on the _Visualize_ tab on the left side menu.

   ![Kibana Visualize](./images/exercises/kibana-visualize.png)

   When opening this page the first time, you will be redirected to the _Management_ / _Index patterns_ configuration page to create a new _index pattern_.

1. Enter the index name — `salaries` — as the index pattern. Make sure _Kibana_ says _Success! Your pattern matches 1 index_, and click _Next step_.

   ![Kibana index pattern](./images/exercises/kibana-index-pattern-1.png)

1. Select _I don't want to use the Time Filter_ as _Time Filter field name_ since we are not going to use this function during the exercises. Click on _Create index pattern_.

   ![Kibana index pattern](./images/exercises/kibana-index-pattern-2.png)

1. Now click on the _Visualize_ tab again to see the following.

   ![Kibana create first visualization](./images/exercises/kibana-create-first-visualization.png)

## a) How many people did the companies hire each month between 2010 and 2016? (vertical bar chart)

1. Click on the _Create new visualization_ button on the _Visualize_ tab, and select _Vertical Bar_.

   ![Kibana vertical bar](./images/exercises/kibana-vertical-bar.png)

1. Select the previously created `salaries` index pattern as the search source.

   ![Kibana search source](./images/exercises/kibana-search-source.png)

1. Under the _Metrics_ setting set _People hired_ as the _Custom Label_. (Expand the _Y-axis_ label to get the configuration options.)

   ![Kibana Metrics](./images/exercises/kibana-a-metrics.png)

1. Under the _Buckets_ setting click _Add_ then select _X-Axis_, and set the following.

   - _Aggregation_ should be _Date Histogram_
   - _Field_ should be `hired`
   - _Minimum interval_ should be _Monthly_
   - _Custom Label_ should be _Month_.

   ![Kibana Buckets](./images/exercises/kibana-a-buckets.png)

1. In the top left corner click on the _Add a filter_ link and use the following settings to create the filter. Click on _Save_ to save the filter.

   ![Kibana filter](./images/exercises/kibana-a-filter.png)

1. The configuration of the visualization is now ready. You see the preview of the visualization to the right. Create a screenshot of the result and save it as `ex5-a.png`.

1. Click on the _Save_ button at the top right corner, and save the visualization as `5_a`.

   ![Kibana save visualization](./images/exercises/kibana-a-save.png)

1. Click on the _Management_ tab in the left side menu, and choose the _Saved Objects_ option. Select and export the visualization you just saved. No need to include related objects. Save the downloaded file as `ex5-a.ndjson`.

   ![Kibana export](./images/exercises/kibana-export.png)

## b) Show the gender and age distribution of the workers! (pie chart)

1. Go back to the _Visualize_ tab. It will likely load the last visualization. Click on the tab button again to get back to the landing page of all visualizations.

1. Click on the _Create visualization_ button on the _Visualize_ tab, and select _Pie_.

1. Select the previously created `salaries` index pattern as the search source.

1. Under the _Buckets_ setting click _Add_ and select _Split Slices_ and set a _Terms_ aggregation on the `gender` field. As _Custom Label_ set _Gender_.

   ![Kibana Buckets](./images/exercises/kibana-b-buckets-1.png)

1. Within the _Buckets_ configuration area click on the _Add_ button and select _Split Slices_ with a _Range_ aggregation on the `age` field with the following ranges. Also add a custom label _Age_.

   ![Kibana Buckets](./images/exercises/kibana-b-buckets-2.png)

1. Create a screenshot of the resulting visualization and save it as `ex5-b.png`. Use the previous method to save and export the visualization. Save the exported file as `ex5-b.ndjson`.

## c) Show the distribution of the workers' locations on a map!

1. Create a new visualization of type _Region Map_. Select the previously created `salaries` index pattern as the search source.

1. Under the _Buckets_ setting add a _Shape field_ with _Terms_ aggregation on the `address.state` field. Make sure to set the _Size_ value to at least 50.

   ![Kibana Buckets](./images/exercises/kibana-c-buckets.png)

1. Under _Options_ / _Layer Settings_ select _USA States_ as _Vector map_ and _FIPS 5-2 alpha code_ as _Join field_.

   ![Kibana Options](./images/exercises/kibana-c-options.png)

1. Create a screenshot of the result and save it as `ex5-c.png`. Save and export the visualization. Save the exported file as `ex5-c.ndjson`.

## Next exercise

Verify that you created 3 screenshots and also exported the 3 visualizations!

Next is [exercise 6](exercise6.md).
