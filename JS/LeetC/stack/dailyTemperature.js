/**
 * @param {number[]} temperatures
 * @return {number[]}
 */

function dailyTemperatures(temperatures) {
  let n = temperatures.length;
  let hottest = 0;
  let result = Array.from({ length: n }, () => 0);

  for (let currDay = n - 1; currDay >= 0; currDay--) {
    let currentTemp = temperatures[currDay];

    if (currentTemp >= hottest) {
      hottest = currentTemp;
      continue;
    }

    let days = 1;
    while (temperatures[currDay + days] <= currentTemp) {
      days += result[currDay + days];
    }

    result[currDay] = days;
  }

  return result;
}

// -------------------------------------------------
function dailyTemperatures(temperatures) {
  // This uses a Monotonic Stack
  let n = temperatures.length;
  const result = Array.from({ length: n }, () => 0);
  const stack = [];

  for (let [currentDay, currentTemp] of temperatures.entries()) {
    while (
      stack.length > 0 &&
      temperatures[stack[stack.length - 1]] < currentTemp
    ) {
      const prevDay = stack.pop();
      result[prevDay] = currentDay - prevDay;
    }

    stack.push(currentDay);
  }

  return result;
}

// ----------------------------------------------------
function dailyTemperatures(temperatures) {
  // this uses 2 stacks
  const stack = [];
  const tempStack = [];

  const result = [];

  for (let i = temperatures.length - 1; i >= 0; i--) {
    let current = temperatures[i];

    if (stack.length === 0) {
      stack.push(current);
      result[i] = 0;
      continue;
    }

    let count = 1;

    while (stack.length > 0 && stack[stack.length - 1] <= current) {
      count++;
      tempStack.push(stack.pop());
    }

    if (stack.length === 0) {
      // we ran out of items in tempStack
      // and could not find any higher
      result[i] = 0;
    } else {
      result[i] = count;
    }

    dumpStackIntoAnother(tempStack, stack);
    stack.push(current);
  }

  return result;
}

function dumpStackIntoAnother(stackA, stackB) {
  // dumps all values in stackA onto stackB
  while (stackA.length > 0) {
    stackB.push(stackA.pop());
  }
}

(() => {
  // let temps = [73, 74, 75, 71, 69, 72, 76, 73];
  let temps = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70];
  let result = dailyTemperatures(temps);
  console.log({ result });
})();
