function intersection(nums1, nums2) {

  let smaller = nums1.length < nums2.length ? nums1 : nums2;
  let larger = nums1.length > nums2.length ? nums1 : nums2;

  const set1 = new Set(smaller);
  const set2 = new Set(larger);

  let result = [];

  for (let e of set1.values()) {
    if (set2.has(e)) {
      result.push(e);
    }
  }

  return result;
 
}
