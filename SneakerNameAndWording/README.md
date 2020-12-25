<h1>Sneaker Name and Wording</h1>

- Splitting the names of shoes based on data and storing every word into a set (similar to array but without repetition)
    - For example, set = ("Air", "Jordan", "Force")
- Once set has been created, create array for each sneakers, with value for 1 if it contains that word and 0 if it does not. This would be stored as a NumPy array
    - For example, using a set above, a shoe called "Air Jordan" would be (1,1,0) and a shoe called "Air Force" would be (1,0,1)
- After creating arrays, create model to interpret each value to predict a price of the sneaker.

<h2>To Do</h2>

- [x] Try to get name of one sneaker and split it into an array
- [ ] Get multiple sneaker names and create many arrays
- [ ] Create model for determing sneaker price based on certain words e.g. Off-white, Supreme, Yeezy
- [ ] Test model
- [ ] Improve the model
