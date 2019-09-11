package main

func main() {
	cards := newDeck()
	hand, _ := deal(cards, 5)
	hand.print()
	cards.saveToFile("foo.dat")
	d := newDeckFromFile("foo.dat")
	d.shuffle()
	d.print()
}
