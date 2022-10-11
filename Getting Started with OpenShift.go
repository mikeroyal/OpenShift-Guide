Code samples & snippets coming soon!
This is a Work in Progress!

package main

import (
	"os"
	"fmt"
	"net/http"
)

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello!")
}

func main() {
	ip := os.Getenv("OPENSHIFT_INTERNAL_IP")
	http.HandleFunc("/", hello)
	http.ListenAndServe(fmt.Sprintf("%s: 8443", ip), nil)
}
