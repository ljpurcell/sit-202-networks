package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

func main() {
    client := &http.Client{}
    resp, err := client.Get("http://localhost:8080/get-date-time")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    body, err := io.ReadAll(resp.Body)
    fmt.Println(string(body))
}
