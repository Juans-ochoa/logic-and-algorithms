/**
 * Example 1: Given a string s, return true if it is a palindrome, false otherwise.
A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".
 */

// function isPalindrome(string = "") {
//   let left = 0,
//     right = string.length - 1;
//   while (left < right) {
//     if (string[left] !== string[right]) return false;
//     left++;
//     right--;
//   }

//   return true;
// }

/**
 * Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
 */

// function checkForTarget(arr, target) {
//   let left = 0,
//     right = arr.length - 1;

//   while (left < right) {
//     let current = arr[left] + arr[right];

//     if (current === target) return true;

//     if (current > target) right--;
//     else left++;
//   }

//   return false;
// }

// console.log(checkForTarget([1, 2, 4, 6, 8, 9, 14, 15], 13));

/**
 * Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
 */
function combine(arr1, arr2) {
  let ans = [];
  let i = 0,
    j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      ans.push(arr1[i]);
      i++;
    } else {
      ans.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    ans.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    ans.push(arr2[j]);
    j++;
  }

  return ans;
}

combine([1, 4, 7, 20], [3, 5, 6]);
