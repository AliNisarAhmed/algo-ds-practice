function intersection(nums1, nums2) {
  const set = new Set(nums1).add(...nums2);
  return [...set];
}
