package main

import "fmt"

func main() {
	nums := []int{}
	for i := 0; i <= 10; i++ {
		nums = append(nums, i)
	}

	for _, num := range nums {
		oddeven := ""
		if num%2 == 0 {
			oddeven = "even"
		} else {
			oddeven = "odd"
		}
		fmt.Printf("%d is %s\n", num, oddeven)
	}
}
