
function canJump(nums) {
  return helper(nums, 0);
}

function helper(nums, idx) {
  if (idx === nums.length - 1) {
    return true;
  }

  let furthestJump = Math.min(idx + nums[idx], nums.length - 1);

  for (let i = furthestJump; i > idx; i--) {
    if (helper(i, nums)) {
      return true;
    }
  }

  return false;
}

// --------------------------------------------------------

// Using Memoization

function canJump(nums) {
  const memo = [];
  for (let i = 0; i < nums.length; i++) {
    memo[i] = 'unknown'
  }
  memo[memo.length - 1] = 'good';
  return helper(nums, 0, memo)
}

function helper(nums, position, memo) {
  if (memo[position] !== 'unknown') {
    return memo[position] == 'good' ? true : false;
  }

  let furthestJump = Math.min(position + nums[position], nums.length - 1);

  for (let nextPos = position + 1; nextPos <= furthestJump; nextPos++) {
    if (helper(nextPos, nums, memo)) {
      memo[position] = 'good';
      return true;
    }
  }

  memo[position] = 'bad';
  return false;
}

// ------ Dynamic programming - bottom up


function canJump(nums) {
  const memo = [];
  for (let i = 0; i < nums.length - 1; i++) {
    memo[i] = 'unknown';
  }
  memo[memo.length - 1] = 'good';

  for (let i = nums.length - 2; i >= 0; i--) {
    let furthestJump = Math.min(i + nums[i], nums.length - 1);
    for (let j = i + 1; j <= furthestJump; j++) {
      if (memo[j] == 'good') {
        memo[i] = 'good';
        break;
      }
    }
  }

  return memo[0] === 'good';
}

// ---- GREEDY

function canJump(nums) {
  let lastPos = nums.length - 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    if (i + nums[i] >= lastPos) {
      lastPos = i;
    }
  }

  return lastPos === 0;
}
