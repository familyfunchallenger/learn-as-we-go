package main

import "fmt"

func main() {
	var name = "go conference"
	const confTickets = 50
	var availableTickets = 50
	fmt.Printf("welcome to booking app - [%v]\n", name)
	fmt.Printf("get tickets here (available %v / %v)\n", availableTickets, confTickets)

	var bookings [50]string
	bookings[0] = "n1"
	bookings[1] = "n2"

	var userName string = "Tom"
	var userTickets int = -1
	fmt.Println("enter your name:")
	fmt.Scan(&userName)
	fmt.Println("entner number of tickets:")
	fmt.Scan(&userTickets)

	availableTickets = availableTickets - userTickets
	fmt.Println(userName, userTickets)
	fmt.Printf("remaining tickets: %v\n", availableTickets)

}
