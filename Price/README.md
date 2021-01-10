<h1>Price</h1>

- Obtain data (Sale history) from stockx from specific shoe
- Plot a graph
- Predict price

<h2>To Do</h2>

- [x] Get data
- [x] Create arrays and plot graph
- [ ] Try scikitlearn
- [ ] Allow arrays to be created as soon as data is drawn
- [ ] Try to let model predict price
- [ ] Maybe have to remove data that may cause prediction to be wierd
- [ ] Maybe try to use multiple regression so sizing can also be a factor - To do this, I would have to separate size, date and price into csv file.
  Example: https://www.w3schools.com/python/python_ml_multiple_regression.asp
- [ ] Merge everything to one file and allow user to search for sneaker

<h2>Issues</h2>

- For certain shoes, like the yeezy bred, resell price has been really high before but now went down. However, the model predicted that it will keep going down. Need to find a way to remove anomalous data. Maybe get data from past month only.