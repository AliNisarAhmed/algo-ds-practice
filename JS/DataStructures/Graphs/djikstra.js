class City {
	constructor(name) {
		this.name = name;
		this.routes = new Map();
	}

	addRoute(city, price) {
		this.routes.set(city, price);
	}
}

let atlanta = new City('Atlanta'),
	boston = new City('Boston'),
	chicago = new City('Chicago'),
	denver = new City('Denver'),
	elPaso = new City('El Paso');

atlanta.addRoute(boston, 100);
atlanta.addRoute(denver, 160);
boston.addRoute(chicago, 120);
boston.addRoute(denver, 180);
chicago.addRoute(elPaso, 80);
denver.addRoute(chicago, 40);
denver.addRoute(elPaso, 140);

function djikstra(startingCity, destination) {
	let cheapestPricesTable = {};
	let cheapestPreviousStopOverCityTable = {};
	// We use an array here, but a PriorityQueue can also be used
	let unvisitedCities = [];
	let visitedCities = {};

	// We add the starting city's name as the first key inside the
	// cheapestPricesTable. It has a value of 0, since it costs nothing to get there from our current location

	cheapestPricesTable[startingCity.name] = 0;

	let currentCity = startingCity;

	// the main loop of the algorithm, it runs as long as we can visit a city that we haven't visited yet
	while (currentCity) {
		// we add the current city's name to the visitedCities hash to record that we've officially visited it, we also remove it from the list of unvisited cities
		visitedCities[currentCity.name] = true;
		unvisitedCities = unvisitedCities.filter(
			(c) => c.name !== currentCity.name
		);

		// we iterate over each of the currentCity's adjacent cities
		for (let [adjacentCity, price] of currentCity.routes.entries()) {
			if (!visitedCities[adjacentCity.name]) {
				unvisitedCities.push(adjacentCity);
			}

			// we calculate the price of getting from the STARTING city to the ADJACENT city using the CURRENT city as the second-to-last stop:
			let priceThroughCurrentCity = cheapestPricesTable[currentCity.name] + price;

			// if the price from the STARTING city to the ADJACENT city is the cheapest one we've found so far...
			if (!cheapestPricesTable[adjacentCity.name] || priceThroughCurrentCity < cheapestPricesTable[adjacentCity.name]) {
				cheapestPricesTable[adjacentCity.name] = priceThroughCurrentCity
				cheapestPreviousStopOverCityTable[adjacentCity.name] = currentCity.name;
			}
		}

		// we visit our next unvisited city. We choose the one that is cheapest to get to from the STARTING city:
		currentCity = findCheapestCity(unvisitedCities, cheapestPricesTable);
	}

	// we have compeleted the core algorithm. now to find the shotest and cheapest path
	let shortestPath = [];
	let currentCityName = destination.name;
	while (currentCityName !== startingCity.name) {
		shortestPath.push(currentCityName);
		currentCityName = cheapestPreviousStopOverCityTable[currentCityName];
	}

	shortestPath.push(startingCity.name);
	return shortestPath.reverse();
}

function findCheapestCity(unvisitedCities, cheapestPricesTable) {
	let min;

	for (let uvc of unvisitedCities) {
		if (!min) {
			min = uvc;
		} else if (cheapestPricesTable[uvc.name] && cheapestPricesTable[uvc.name] < min) {
			min = uvc;
		}
	}

	return min;
}

console.log(djikstra(atlanta, elPaso));