function canTwoMoviesFillFlight(movieLengths, flightLength) {

	const obj = {};

	for (let movie of movieLengths) {
		let diff = Math.abs(movie - flightLength);
		if (obj[diff]) {
			return true;
		} else {
			obj[movie] = true;
		}
	}

	return false;

}

