/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
function solution(isBadVersion) {
	/**
	 * @param {integer} n Total versions
	 * @return {integer} The first bad version
	 */
	return function (n) {
		return helper(0, n);
	};

	function helper(start, end) {
		if (start === end) {
			return start;
		}

		if (start - end === 1) {
			return start;
		}

		// let mid = Math.floor((start + end) / 2);

		// correct way to calculate midpoint to avoid overflow conditions in languages that have that possibility

		let mid = Math.floor(start + (end - start) / 2)

		if (isBadVersion(mid)) {
			return helper(start, mid);
		} else {
			return helper(mid + 1, end);
		}
	}
}
