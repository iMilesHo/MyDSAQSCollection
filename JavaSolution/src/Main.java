/*
 * Implement a vector (mutable array with automatic resizing):
    - Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
    - New raw data array with allocated memory
    - can allocate int array under the hood, just not use its features
    - start with 16, or if the starting number is greater, use power of 2 - 16, 32, 64, 128
    - size() - number of items
    - capacity() - number of items it can hold
    - is_empty()
    - at(index) - returns the item at a given index, blows up if index out of bounds
    - push(item)
    - insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
    - prepend(item) - can use insert above at index 0
    - pop() - remove from end, return value
    - delete(index) - delete item at index, shifting all trailing elements left
    - remove(item) - looks for value and removes index holding it (even if in multiple places)
    - find(item) - looks for value and returns first index with that value, -1 if not found
    - resize(new_capacity) // private function
    - when you reach capacity, resize to double the size
    - when popping an item, if the size is 1/4 of capacity, resize to half
 */
public class Main {
    public static void main(String[] args) {
        int n = 5;
        int[][] pascal = new int[n][];
        for (int i = 0; i < n; i++) {
            pascal[i] = new int[i + 1]; // since java array is 0-based
            pascal[i][0] = 1;
            for(int j=1; j<i; j++) {
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
            }
            pascal[i][i] = 1;
        }
        System.out.println(pascal);
    }
}