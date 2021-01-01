# Sneaker-Price-Predictor

A program which will predict of prices of reselling sneakers in the future. It will be based on 4 factors: Demand and supply, Name, Design of sneaker and Price.

<h2>Stages of development</h2>

1. Gather data for a reasonable amount of sneakers.
2. Create models for each individual factor and test until efficient.
3. Combine the four models to get one.
4. Create a search based system to allow user to search for sneaker and will return the result. Maybe create a bot on discord.

<h2>The Four Factors</h2>

<h3>Current resell price</h3>

- This is based on resell price history on websites such as StockX.
- Model will be created to predict prices based on these data.
- MAY NEED TO GATHER EXTRA DATA
- Use of release date because if it has not been released, price may still be high

<h3>Demand and Supply</h3>

- Supply will come from different sources such as IG, FB. Not all shoes will have a supply
- Demand will come from number of sales in the past (for older shoes) and for newer shoes, demand may not be a factor to determine as it has not gone through any reselling yet.

<h3>Sneaker Name and Wording</h3>

- Splitting the names of shoes based on data and storing every word into a set (similar to array but without repetition)
    - For example, set = ("Air", "Jordan", "Force")
- Once set has been created, create array for each sneakers, with value for 1 if it contains that word and 0 if it does not. This would be stored as a NumPy array
    - For example, using a set above, a shoe called "Air Jordan" would be (1,1,0) and a shoe called "Air Force" would be (1,0,1)
- After creating arrays, create model to interpret each value to predict a price of the sneaker.

<h3>Sneaker Design</h3>

- This will be based on the design of a sneaker, e.g. does it contain a certain feature such as the Yeezy shape, "AIR" logo or Off-White zipties etc.
- Use of CNN (Convolutional Neural Network) to decide whether the design is good or not.
- Maybe use OpenCV, Tensor flow, PILLOW etc.

<h2>Links to others who created sneaker price predictors</h2>

- https://medium.com/swlh/predicting-sneaker-resell-with-deep-learning-d3a78b144099
- https://repository.asu.edu/items/52272
- https://medium.com/swlh/predicting-stockx-sneaker-prices-with-machine-learning-ec9cb625bec0 * This link contains data about StockX already
