function sandwichFactory(bread, protein, cheese, toppings) {
    var sandwich = {};
    sandwich.bread = bread;
    sandwich.protein = protein;
    sandwich.cheese = cheese;
    sandwich.toppings = toppings;
    return sandwich;
}

var s1 = sandwichFactory("wheat", "turkey", "provolone", ["mustard", "fried onions", "arugula"]);
console.log(s1);

console.log("_______________________________________________________________")

function pizzaOven(crust, sauce, cheeses, toppings) {
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

var p1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var p2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var p3 = pizzaOven("thin crust", "white sauce", ["parmesan"], ["chicken", "spinach"]);
var p4 = pizzaOven("stuffed crust", "bbq sauce", ["mozzarella", "cheddar"], ["bacon", "jalapenos"]);
console.log("pizza 1: ", p1);
console.log("pizza 2: ", p2);
console.log("pizza 3: ", p3);
console.log("pizza 4: ", p4);

console.log("_______________________________________________________________")

function getRandomPizza() {
    var randPizza = {};
    var crust = ["deep dish", "hand tossed", "thin crust", "stuffed crust"];
    var sauce = ["traditional", "marinara", "white sauce", "bbq sauce"];
    var cheeses = [["mozzarella"], ["mozzarella", "feta"], ["parmesan"], ["mozzarella", "cheddar"]];
    var toppings = [["pepperoni", "sausage"], ["mushrooms", "olives", "onions"], ["chicken", "spinach"], ["bacon", "jalapenos"]];

    function getRandomType(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    var randomCrust = getRandomType(crust);
    var randomSauce = getRandomType(sauce);
    var randomCheeses = getRandomType(cheeses);
    var randomToppings = getRandomType(toppings);

    randPizza = { randomCrust, randomSauce, randomCheeses, randomToppings }
    return randPizza;
}
console.log("The random pizza is: ", getRandomPizza())