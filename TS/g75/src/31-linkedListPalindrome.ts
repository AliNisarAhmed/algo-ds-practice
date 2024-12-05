import type { ListNode } from "./00-ListNode";

function isPalindromeRec(head: ListNode | null): boolean {
  let frontPointer = head;
  return isPalindromeRecursive(head);

  function isPalindromeRecursive(currentNode: ListNode | null): boolean {
    if (currentNode !== null) {
      if (!isPalindromeRecursive(currentNode.next)) {
        return false;
      }

      if (currentNode.val !== frontPointer!.val) {
        return false;
      }

      frontPointer = frontPointer!.next;
    }
    return true;
  }
}

// ---------------------------------------------------------
// O(n) time, O(1) space solution
// ---------------------------------------------------------

function isPalindrome(head: ListNode | null): boolean {
  if (!head) {
    return true;
  }
  const firstHalfEnd = endOfFirstHalf(head);
  const secondHalfStart = reverseList(firstHalfEnd!.next!);

  let p1: ListNode | null = head;
  let p2 = secondHalfStart;
  let result = true;
  while (result && p1 !== null && p2 !== null) {
    if (p1.val !== p2.val) {
      result = false;
    }
    p1 = p1.next;
    p2 = p2.next;
  }

  firstHalfEnd!.next = reverseList(secondHalfStart!);
  return result;
}

function reverseList(head: ListNode) {
  let prev = null;
  let curr: ListNode | null = head;
  while (curr !== null) {
    let temp: ListNode | null = curr.next;
    curr.next = prev;
    prev = curr;
    curr = temp;
  }
  return prev;
}

function endOfFirstHalf(head: ListNode) {
  let fast = head;
  let slow: ListNode | null = head;

  while (fast.next !== null && fast.next.next !== null) {
    fast = fast.next.next;
    slow = slow!.next;
  }
  return slow;
}
