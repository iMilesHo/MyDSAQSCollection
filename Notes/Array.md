# Array
## Summary
- Array uses a contiguous block of memory to store elements
- Array coonsists of equal-size elements indexed by contiguous integrs
- Array has constant-time access to elements
- Array has constant-time to remove or add elements at the end of the array
- Array has linear-time to remove or add elements at an arbitary location
- 2D Multi-dimensional arrays can be stored through row-major or column-major order
    - (1,1)|(1,2)|(1,3)|(2,1)|(2,2)|(2,3)|(3,1)|(3,2)|(3,3)
    - (1,1)|(2,1)|(3,1)|(1,2)|(2,2)|(3,2)|(1,3)|(2,3)|(3,3)


## Practice

### 1. Print a pascal triangle
```Java
// Java
public class PascalTriangle {
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
    }
}
```

```Python
# Python
def pascal_triangle(n):
    pascal = [[1] * (i+1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
```