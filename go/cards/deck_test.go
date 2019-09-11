package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	d := newDeck()
	expectedCount := 52
	expectedFirstCard := "Ace of Spades"
	if len(d) != expectedCount {
		t.Errorf("Expected Deck length of %d, but got %d", expectedCount, len(d))
	}

	if d[0] != expectedFirstCard {
		t.Errorf("Expected first card %s but got %s", expectedFirstCard, d[0])
	}
}

func TestSaveToDeckAndNewDeckTestFromFile(t *testing.T) {
	os.Remove("_decktesting")

	d := newDeck()
	d.saveToFile("_decktesting")
	loadedDeck := newDeckFromFile("_decktesting")

	if len(loadedDeck) != len(d) {
		t.Errorf("Expected deck lengths to be the same")
	}
	os.Remove("_decktesting")

}
