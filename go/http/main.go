package main

import "fmt"
import "net/http"
import "os"
import "io"

type logWriter struct{}

func main() {
	resp, err := http.Get("http://google.com")
	if err != nil {
		fmt.Println("error:", err)
		os.Exit(1)
	}

	lw := logWriter{}
	io.Copy(lw, resp.Body)
}

func (logWriter) Write(bs []byte) (int, error) {
	fmt.Println("Wrote: ", len(bs), " bytes")
	return len(bs), nil
}
