
function merge(intervals) {

  intervals.sort((a, b) => a[0] - b[0])

  if (intervals.length <= 1) {
    return intervals;
  }
  
  let res = [];

  for (let interval of intervals) {
    if (res.length === 0 || res[res.length - 1][1] < interval[0]) {
      res.push(interval)
    }
    else {
      res[res.length - 1][1] = Math.max(res[res.length - 1][1], interval[1])
    }
  }

  return res;
}
