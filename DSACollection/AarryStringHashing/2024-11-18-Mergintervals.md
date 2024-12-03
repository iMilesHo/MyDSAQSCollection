```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int m;
    std::cin >> m;

    std::vector<std::pair<int, int>> intervals;
    for (int i = 0; i < m; i++) {
        int start, end;
        std::cin >> start >> end;
        intervals.push_back({start, end});
    }

    // Step 1: Sort intervals based on the start time
    std::sort(intervals.begin(), intervals.end());

    // Step 2: Merge intervals
    std::vector<std::pair<int, int>> merged;
    merged.push_back(intervals[0]);

    for (int i = 1; i < m; i++) {
        // Check if current interval overlaps with the last interval in merged
        if (intervals[i].first <= merged.back().second) {
            // Merge intervals by updating the end time of the last interval in merged
            merged.back().second = std::max(merged.back().second, intervals[i].second);
        } else {
            // If no overlap, add current interval to merged
            merged.push_back(intervals[i]);
        }
    }

    // Step 3: Calculate total length of merged intervals
    int totalLength = 0;
    for (auto &interval : merged) {
        totalLength += interval.second - interval.first;
    }

    // Output the total merged interval length
    std::cout << totalLength << std::endl;

    return 0;
}
```
