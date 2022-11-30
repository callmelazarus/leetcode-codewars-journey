/*
https://leetcode.com/problems/invert-binary-tree/description/

11/30/2022

--- PROMPT ---
Given the root of a binary tree, invert the tree, and return its root.



--- LESSONS ---

--- QUESTIONS ---

--- PSEUDOCODE ---


*/

// --- MY SOLUTION ---
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
  if (root === null) {
    return null;
  }
  let temp = root.left;
  root.left = root.right;
  root.right = temp;
  invertTree(root.left);
  invertTree(root.right);

  return root;
};

// --- TEST ---

// --- ALT SOLN by others ---
