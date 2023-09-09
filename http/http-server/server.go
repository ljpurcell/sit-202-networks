package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

type server struct {
    port string
}

func getDateTimeHandler(w http.ResponseWriter, r *http.Request) {
    now := time.Now()
    min := now.Minute()
    hr := now.Hour()
    day := now.Day()
    mth := now.Month()
    yr := now.Year()
    yd := now.YearDay()


    fmt.Fprintf(w, "Time: It is %v:%v.\nDate: It is day %v of %v, which is the %v day of the year, in the year %v.", hr, min, day, mth, yd, yr)
}

func (s *server) listen() {
    http.HandleFunc("/get-date-time", getDateTimeHandler)
    if err := http.ListenAndServe(s.port, nil); err != nil {
        log.Fatal(err)
    }
}

func main() {
    s := server{port: ":8080"}
    s.listen()
}

