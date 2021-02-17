function mergeRanges(meetings) {

  const sorted = [...meetings].sort((a, b) => a.startTime - b.startTime);

  let results = [];

  for (let i = 0; i < sorted.length; i++) {
    let lastSlot = results[results.length - 1];
    let current = sorted[i];

    if (!lastSlot) {
      results.push(current);
    } else {

     if (current.startTime <= lastSlot.endTime) {
       lastSlot.endTime = Math.max(lastSlot.endTime, current.endTime);
     }

      else {
      	results.push(current);
      }

    }

  }

  return results;

}
