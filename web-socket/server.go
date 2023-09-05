package main

import (
	"fmt"
	"io"

	"golang.org/x/net/websocket"
	"net/http"
)

const port string = ":3000"

// Holds connections to the websocket
type Server struct {
	conns map[*websocket.Conn]bool
}

// Adds the connection to the server and runs the read loop
func (s *Server) handleWS(ws *websocket.Conn) {
	fmt.Printf("New incoming request from client: %v\n", ws.RemoteAddr())

	s.conns[ws] = true

	s.readLoop(ws)
}

// Creates a buffer of bytes, reads the data into it if no error, and writes a
// a confirmation message back to the client
func (s *Server) readLoop(ws *websocket.Conn) {
	buf := make([]byte, 1024)
	for {
		n, err := ws.Read(buf)
		if err != nil {
			if err == io.EOF {
				break
			}
			fmt.Println("Read error: ", err)
			continue
		}
		msg := buf[:n]
		fmt.Printf("Client said: %v\n", string(msg))
		ws.Write([]byte("Received the message"))
	}
}

// Creates a new server
func NewServer() *Server {
	return &Server{
		conns: make(map[*websocket.Conn]bool),
	}
}

func main() {
	server := NewServer()
	http.Handle("/chat", websocket.Handler(server.handleWS))
	fmt.Println("Listening on port: ", port)
	http.ListenAndServe(port, nil)
}
