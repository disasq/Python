# SpaceX Falcon 9 Landing Prediction

IBM Applied Data Science Capstone project by Dias Saqyp.

## Objective
Predict whether a SpaceX Falcon 9 first stage lands successfully using launch context.

## Workflow
1. Collect Falcon 9 launch records from the SpaceX REST API.
2. Parse launch-history tables with BeautifulSoup.
3. Clean payload, orbit, launch site, booster, and landing outcome fields.
4. Explore patterns with visualizations and SQL.
5. Build a Folium map and Plotly Dash dashboard.
6. Compare Logistic Regression, SVM, Decision Tree, and KNN classifiers.

## Results
The presentation reports 90 course-dataset launches. The tuned Decision Tree achieved 88.9% accuracy on the 18-record held-out test set. This estimate has uncertainty because the test set is small.

## Sources
- https://api.spacexdata.com/v4/launches/past
- https://www.coursera.org/learn/applied-data-science-capstone
- https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches
