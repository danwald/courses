package main

import "fmt"
import "net/http"
import "time"

func main() {
	sites := []string{
		"http://google.com",
		"http://facebook.com",
		"http://golang.org",
		"http://amazon.com",
	}

	c := make(chan string)

	for _, site := range sites {
		go checkLink(site, c)
	}

	for s := range c {
		go func(link string) {
			time.Sleep(2 * time.Second)
			checkLink(link, c)
		}(s)
	}
}

func checkLink(site string, c chan string) {
	_, err := http.Get(site)
	if err != nil {
		fmt.Println(site, "might be down!")
		c <- site
		return
	}
	fmt.Println(site, "is up!")
	c <- site
}
