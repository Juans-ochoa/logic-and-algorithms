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
// function combine(arr1, arr2) {
//   let ans = [];
//   let i = 0,
//     j = 0;

//   while (i < arr1.length && j < arr2.length) {
//     if (arr1[i] < arr2[j]) {
//       ans.push(arr1[i]);
//       i++;
//     } else {
//       ans.push(arr2[j]);
//       j++;
//     }
//   }

//   while (i < arr1.length) {
//     ans.push(arr1[i]);
//     i++;
//   }

//   while (j < arr2.length) {
//     ans.push(arr2[j]);
//     j++;
//   }

//   return ans;
// }

// combine([1, 4, 7, 20], [3, 5, 6]);

/**
 * Example 4: 392. Is Subsequence.

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.
 */

// function isSubsequence(s, t) {
//   let i = 0,
//     j = 0;

//   while (i < s.length && j < t.length) {
//     if (s[i] === t[j]) {
//       i++;
//     }

//     j++;
//   }

//   return i === s.length;
// }

// console.log(isSubsequence("abcd", "abcdrere"));

/**
 * Revert a string using two pointers
 */
// function revertString(str) {
//   let left = 0,
//     right = str.length - 1;

//   const arr = str.split("");

//   while (left < right) {
//     [arr[left], arr[right]] = [arr[right], arr[left]];

//     left++;
//     right--;
//   }

//   return arr.join("");
// }

// console.log(revertString("HolaMundo"));

/**Hacer ejercicios en Python desde este punto */
/**Move all ceros at the end,  without additional array */
// function moveCerosAtEnd(arr = []) {
//   let left = 0;
//   let right = arr.length - 1;

//   while (left < right) {
//     if (arr[left] === 0) {
//       [arr[left], arr[right]] = [arr[right], arr[left]];
//       right--;
//     } else {
//       left++;
//     }
//   }

//   //   while (left < right) {
//   //     if (arr[left] === 0) {
//   //       [arr[left], arr[right]] = [arr[right], arr[left]];
//   //       right--;
//   //     }
//   //     left++;
//   //   }

//   console.log(arr);
// }

// moveCerosAtEnd([1, 2, 3, 0, 0, 4, 4]);

//Delete duplicate values, array arrangement
// function deleteDuplicates(arr = []) {
//   let slow = 0;

//   for (let fast = 1; fast < arr.length; fast++) {
//     if (arr[fast] !== arr[slow]) {
//       slow++;
//       arr[slow] = arr[fast];
//     }
//   }

//   arr.length = slow + 1;
//   return arr;
// }

// console.log(deleteDuplicates([4, 2, 4, 1, 4, 3, 2]));

/**
 * Triplete con suma cercana - Encuentra tres números en un array cuya suma sea la más cercana a un valor objetivo dado.
 */

// function threeNumbersTarget(arr = [], target) {
//   arr.sort((a, b) => a - b);

//   let closestSum = Infinity;

//   for (let i = 0; i < arr.length; i++) {
//     let left = i + 1;
//     let right = arr.length - 1;

//     while (left < right) {
//       const currentSum = arr[i] + arr[left] + arr[right];
//       const currentDif = Math.abs(target - currentSum);

//       if (currentDif < Math.abs(target - closestSum)) {
//         closestSum = currentSum;
//       }

//       if (currentDif === 0) return currentSum;

//       if (currentSum < target) {
//         left++;
//       } else {
//         right--;
//       }
//     }
//   }

//   return closestSum;
// }

// console.log(threeNumbersTarget([1, 2, 3, 4, 5, 6, 7, 34, 3], 12));

/**
 * Problema: Dado un array de enteros positivos y un entero positivo K, encuentra el número de subarrays contiguos cuyo producto es estrictamente menor que K.
 */

// function countSubArraysWithProductLessThanK(array = [], k) {
//   if (k <= 1) return 0;

//   let count = 0,
//     product = 1,
//     left = 0;

//   for (let right = 0; right < array.length; right++) {
//     product *= array[right];

//     // Contraer la ventana desde la izquierda mientras el producto sea >= k
//     while (product >= k) {
//       // Dividir el producto por el elemento que sale de la ventana
//       product /= array[left];
//       // Mover el puntero izquierdo
//       left++;
//     }

//     // En este punto, todos los subarrays que terminan en 'right' y
//     // comienzan en cualquier posición desde 'left' hasta 'right' tienen
//     // un producto menor que k
//     // El número de estos subarrays es (right - left + 1)
//     count += right - left + 1;
//     console.log(count);
//   }
// }

// countSubArraysWithProductLessThanK([10, 5, 2, 6], 100);

/**
 * El algoritmo del problema de la bandera nacional holandesa (Dutch National Flag Problem), propuesto por Edsger Dijkstra, es una forma eficiente de ordenar un arreglo que contiene solo tres tipos de elementos (en este caso, 0, 1 y 2). El objetivo es agrupar los elementos iguales juntos en una sola pasada del arreglo, logrando una complejidad temporal de O(n) y sin usar espacio adicional.
 */

// function sortColors(array = []) {
//   let low = 0,
//     mid = 0,
//     hight = array.length - 1;

//   while (mid <= hight) {
//     if (array[mid] === 0) {
//       [array[low], array[mid]] = [array[mid], array[low]];
//       mid++;
//       low++;
//     } else if (array[mid] === 1) {
//       mid++;
//     } else {
//       [array[hight], array[mid]] = [array[mid], array[hight]];
//       hight--;
//     }
//   }

//   return array;
// }

// console.log(sortColors([2, 0, 2, 0, 1, 1, 0]));
//Iteraciones
// 0 -> hight = 6-1, low=0, mid=0, array[mid=0] = 2
//result -> [0,0,2,0,1,1,2], height=5
// 1 -> hight = 5, low=0, mid=0, array[mid=0]=0
//result -> [0,0,2,0,1,1,2], mid=1, low=1,
// 2 -> hight = 5, low=1, mid=1, array[mid=1]=0
//result -> [0,0,2,0,1,1,2], mid=2, low=2,
// 3 -> hight=5, low=2, mid=2, array[mid=2]=2, [0,0,2,0,1,1,2]
//result -> [0,0,1,0,1,2,2], mid=2, low=2,height=4
// 4 -> hight=4, low=2, mid=2, array[mid=2]=1, [0,0,1,0,1,2,2]
//result -> [0,0,1,0,1,2,2], mid=3, low=2,height=4
// 5 -> hight=4, low=2, mid=3, array[mid=3]=0, [0,0,1,0,1,2,2]
//result -> [0,0,0,1,1,2,2], mid=4, low=3,height=4
// 6 -> hight=4, low=2, mid=3, array[mid=3]=0, [0,0,0,1,1,2,2] end
//result -> [0,0,0,1,1,2,2], mid=4, low=3,height=4

// 4. Cuadrados de un array ordenado
// Problema: Devuelve un nuevo array con los cuadrados ordenados.
// function sortedSquares(array = []) {
//   let result = new Array(array.length);
//   let left = 0,
//     right = array.length - 1,
//     index = array.length - 1;

//   while (left <= right) {
//     const leftSquare = array[left] ** 2;
//     const rightSquare = array[right] ** 2;

//     if (leftSquare > rightSquare) {
//       result[index] = leftSquare;
//       left++;
//     } else {
//       result[index] = rightSquare;
//       right--;
//     }

//     index--;
//   }

//   console.log(result);
// }

// sortedSquares([-4, -1, 0, 3, 10]);
