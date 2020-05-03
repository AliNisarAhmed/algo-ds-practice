const PriorityQueue = require('./priorityQueue');

const values = [
	{
    value: 'seven',
    priority: 7,
	},
	{
    value: 'six',
    priority: 6,
	},
	{
    value: 'five',
    priority: 5,
	},
	{
    value: 'four',
    priority: 4,
	},
	{
    value: 'three',
    priority: 3,
	},
	{
    value: 'two',
    priority: 2,
	},
	{
    value: 'one',
    priority: 1,
	},
	{
    value: 'seven',
    priority: 7,
	},
	{
    value: 'six',
    priority: 6,
	},
	{
    value: 'five',
    priority: 5,
	},
	{
    value: 'four',
    priority: 4,
	},
	{
    value: 'seven',
    priority: 7,
	},
	{
    value: 'six',
    priority: 6,
	},
	{
    value: 'five',
    priority: 5,
	},
	{
    value: 'four',
    priority: 4,
	},
];

describe('Test Priority Queue', () => {
	let pq;

	beforeEach(() => {
		pq = new PriorityQueue();

		values.forEach(o => {
      pq.enqueue(o.value, o.priority);
    });
	});

	test('Tesing Priority Queue', () => {
    console.log(pq);

    const results = [];
    values.forEach(v => {
      results.push(pq.extractMax());
    });

    console.log('results', results);

    const sortedValues = [...values].sort((o1, o2) => o1.priority < o2.priority ? -1 : 1 );


    console.log('sortedValues', sortedValues)
    expect(results).toEqual(sortedValues)

	});
});
