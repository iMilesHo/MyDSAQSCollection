Learn from Excercise

1. Positive Negative Zero

```java
public class PositiveNegativeZero {
    // write code here
    public static void checkNumber(int number) {
        if (number > 0) {
            System.out.println("positive");
        } else if (number < 0) {
            System.out.println("negative");
        } else {
            System.out.println("zero");
        }
    }
}
```

2. speed converter

```java
class SpeedConverter {
    // write code here
    long toMilesPerHour(double kmPerHour) {
        if (kmPerHour < 0) {
            return -1;
        }
        return Math.round(kmPerHour/1.6);
    }
}
```

3. MegaBytes Converter

```java

```
