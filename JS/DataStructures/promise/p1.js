const PENDING = 'pending';
const FULFILLED = 'fulfilled';
const REJECTED = 'rejected';

class MyPromise {
	constructor(handler) {
		this.status = PENDING;
		this.onFulfilledCallbacks = [];
		this.onRejectedCallbacks = [];
		this.value = null;

		const resolve = (value) => {
			if (this.status === PENDING) {
				this.status = FULFILLED;
				this.value = value;
				this.onFulfilledCallbacks.forEach((fn) => fn(value));
			}
		};

		const reject = (err) => {
			if (this.status === PENDING) {
				this.status = REJECTED;
				this.value = err;
				this.onFulfilledCallbacks.forEach((fn) => fn(err));
			}
		};

		try {
			handler(resolve, reject);
		} catch (error) {
			reject(error);
		}
	}

	then(onFulfilled, onRejected) {
		return new MyPromise((resolve, reject) => {
			if (this.status === PENDING) {
				this.onFulfilledCallbacks.push(() => {
					try {
						const fulfilledFromLastPromise = onFulfilled(this.value);

						if (fulfilledFromLastPromise instanceof MyPromise) {
							fulfilledFromLastPromise.then(resolve, reject);
						} else {
							resolve(fulfilledFromLastPromise);
						}
					} catch (error) {
						reject(error);
					}
				});

				this.onRejectedCallbacks.push(() => {
					try {
						const rejectedFromLastPromise = onRejected(this.value);
						if (rejectedFromLastPromise instanceof MyPromise) {
							rejectedFromLastPromise.then(resolve, reject);
						} else {
							reject(rejectedFromLastPromise);
						}
					} catch (error) {
						reject(error);
					}
				});
			}

			if (this.status === FULFILLED) {
				try {
					const fulfilledFromLastPromise = onFulfilled(this.value);
					if (fulfilledFromLastPromise instanceof MyPromise) {
						fulfilledFromLastPromise.then(resolve, reject);
					} else {
						resolve(fulfilledFromLastPromise);
					}
				} catch (error) {
					reject(error);
				}
			}

			if (this.status === 'rejected') {
				try {
					const rejectedFromLastPromise = onRejected(this.value);
					if (rejectedFromLastPromise instanceof MyPromise) {
						rejectedFromLastPromise.then(resolve, reject);
					} else {
						reject(rejectedFromLastPromise);
					}
				} catch (err) {
					reject(err);
				}
			}
		});

		// if (this.status === PENDING) {
		// 	this.onFulfilledCallbacks.push(onFulfilled);
		// 	this.onRejectedCallbacks.push(onRejected);
		// }

		// if (this.status === FULFILLED) {
		// 	onFulfilled(this.value);
		// }

		// if (this.status === REJECTED) {
		// 	onRejected(this.value);
		// }
	}
}

const p = new MyPromise((resolve, reject) => {
	setTimeout(() => resolve('resolved'), 4000);
});

p.then(
	(res) => console.log('Promise resolve result: ', res),
	(e) => console.log('Promise error result: ', e)
).then(
	(res) => console.log('Second then: ', res),
	(err) => console.log('second then error: ', err)
);
