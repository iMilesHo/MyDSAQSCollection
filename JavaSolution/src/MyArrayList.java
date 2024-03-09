/*
Implement a vector (mutable array with automatic resizing):
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

/**
 * MyArrayListInterface
 */
interface MyArrayListInterface<T> {
    int size();
    int capacity();
    boolean isEmpty();
    T at(int index);
    void push(T item);
    void insert(int index, T item);
    void prepend(T item);
    T pop();
    void delete(int index);
    void remove(T item);
    int find(T item);
}

public class MyArrayList<T> implements MyArrayListInterface<T> {
    private T[] items;
    private int size = 0; // Current size
    private int capacity = 16; // Initial capacity

    @SuppressWarnings("unchecked")
    public MyArrayList() {
        // Initialize items array with the capacity
        items = (T[]) new Object[capacity]; // Initialized with an Object array, then cast to generic array type T[]
    }

    public int size() {
        return size;
    }

    public int capacity() {
        return capacity;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public T at(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        return items[index];
    }

    public void push(T item) {
        if (size == capacity) {
            resize(capacity * 2); // Double the capacity
        }
        items[size++] = item;
    }

    public void insert(int index, T item) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        if (size == capacity) {
            resize(capacity * 2); // Double the capacity
        }
        System.arraycopy(items, index, items, index + 1, size - index);
        items[index] = item;
        size++;
    }

    public void prepend(T item) {
        insert(0, item);
    }

    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Cannot pop from an empty array");
        }
        T item = items[--size];
        items[size] = null; // Help GC
        // Resize down if necessary
        if (size > 0 && size == capacity / 4) {
            resize(capacity / 2);
        }
        return item;
    }

    public void delete(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        int moveCount = size - index - 1;
        if (moveCount > 0) {
            System.arraycopy(items, index + 1, items, index, moveCount);
        }
        items[--size] = null; // Help GC
        // Resize down if necessary
        if (size > 0 && size == capacity / 4) {
            resize(capacity / 2);
        }
    }

    public void remove(T item) {
        for (int i = 0; i < size; i++) {
            if (item.equals(items[i])) {
                delete(i);
                i--; // Adjust for shift
            }
        }
    }

    public int find(T item) {
        for (int i = 0; i < size; i++) {
            if (item.equals(items[i])) {
                return i;
            }
        }
        return -1;
    }

    @SuppressWarnings("unchecked")
    private void resize(int newCapacity) {
        // Create a new Object array with the new capacity
        Object[] newItems = new Object[newCapacity];
        
        // Copy the elements from the old array to the new array
        System.arraycopy(items, 0, newItems, 0, size);
        
        
        // Cast the new Object array to the array type T[] and assign it back to items
        items = (T[]) newItems;
        
        // Update the capacity to the new value
        capacity = newCapacity;

    }

}
