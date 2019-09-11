package main

import "fmt"

type contactInfo struct {
	email string
	pobox int
}
type person struct {
	firstName string
	lastName  string
	contact   contactInfo
}

func main() {
	fmt.Println("structs in go")
	alex := person{firstName: "Alex", lastName: "Anderson"}
	fmt.Println(alex)
	var danny person
	danny.print()
	danny.firstName = "dan"
	danny.lastName = "wald"
	danny.print()
	moses := person{
		firstName: "moose",
		lastName:  "goose",
		contact: contactInfo{
			email: "moosegoose@gmail.com",
			pobox: 12345,
		},
	}
	moses.print()
	mosesPointer := &moses
	mosesPointer.updateFirstName("mosu")
	moses.print()
	danny.updateFirstName("dancha")
	danny.print()

}

func (pPerson *person) updateFirstName(fname string) {
	pPerson.firstName = fname
}

func (p person) print() {
	fmt.Printf("\n%+v", p)
}
