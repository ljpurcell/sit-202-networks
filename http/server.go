package server

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
)

type server struct {
    port string
}

type myDateTime struct {
    weekday time.Weekday
    day int
    month time.Month
    year int
    yearDay int
}


func getDateTimeHandler(w http.ResponseWriter, r *http.Request) {
    now := time.Now()
    wd := now.Weekday()
    day := now.Day()
    mth := now.Month()
    yr := now.Year()
    yd := now.YearDay()

    dt := myDateTime{
        weekday: wd,
        day: day,
        month: mth,
        year: yr,
        yearDay: yd,
    }

    dateTimeResponse, err := json.Marshal(dt)
    if err != nil {
        fmt.Printf("Error encoding date-time response: %v", err)
    }

    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(dateTimeResponse)
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

