package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println()
	if len(os.Args) < 2 {
		fmt.Println("Please enter a filename")
		os.Exit(-1)
	}

	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println("Error opening file")
		os.Exit(-1)
	}

	data := make([]byte, 1024)
	for {
		count, err := file.Read(data)
		if count == 0 {
			file.Close()
			break
		}
		if err != nil {
			fmt.Println("Error reading file", err)
			break
		}
		fmt.Println(string(data))

	}
}
