package main

import (
	"fmt"
	"net/http"
	"net/http/fcpgi"
)

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello world from go!")
}

func main() {
	http.HandleFunc("/", hello)
	fcgi.Serve(nil, nil)
}
