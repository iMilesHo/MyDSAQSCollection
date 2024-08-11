import Foundation

func countIntegers(n: Int, val: Int, arr: [Int]) -> [Int] {
    let smaller = arr.filter { $0 < val }.count
    let equal = arr.filter { $0 == val }.count
    let greater = arr.filter { $0 > val }.count
    return [smaller, equal, greater]
}

if let n = readLine(), let val = readLine(), let input = readLine() {
    let arr = input.split(separator: " ").compactMap { Int($0) }
    let result = countIntegers(n: Int(n)!, val: Int(val)!, arr: arr)
    print(result.map { String($0) }.joined(separator: " "))
}