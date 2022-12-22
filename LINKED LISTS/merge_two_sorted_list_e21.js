
/*
https://leetcode.com/problems/merge-two-sorted-lists/description/

11/28/2022

- while loop
- intializing dummy node for SLL
- SLL navigation

--- PROMPT ---
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



--- LESSONS ---
There are dummy initalized nodes that you need to make. This allows you keep track of the head of your SLL

Little video on usage of dummy node
https://www.youtube.com/watch?v=JI71sxtHTng

--- QUESTIONS ---

--- PSEUDOCODE ---


*/

// --- MY SOLUTION ---
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
 var mergeTwoLists = function(list1, list2) {
    // merging the two lists into one sorted lists.

    // edge cases -> empty list

    // instead increasing space complexity, let's use the lists that exist

    if (list1 == null && list2 == null)
    {return null}

    // if one list is empty, return the next list
    if (list1 == null) {return list2}
    if (list2 == null) {return list1}

    // start with the smaller of the two heads, and then iterate thru each loop, building our SLL with the next larger value (if equal, or larger)

    // create an instance of a list node

// why do I need to create this dummy node? I tried removing it, and the result is undesireable
let dummy = new ListNode()
let soln = dummy

// loop thru the lists, so long as they are not null
while (list1 && list2) {
    if (list1.val < list2.val){
        // start adding to the soln SLL with the smaller of the two values in l1, l2
        soln.next = list1
        list1 = list1.next
    } else
    {
        soln.next = list2
        list2 = list2.next
    }
    // advance the soln SLL
    soln = soln.next
}

// if one list is empty, append any remaining elements in the other list to soln SLL
if (list1 == null){
soln.next = list2
}
else if (list2 == null){
    soln.next = list1
}

// returning soln only has the end portion of list
// returning dummy will include the initalized node of val 0
// returning dummy.next will give you the solution
return dummy.next

};
// --- TEST ---


// --- ALT SOLN by others ---
