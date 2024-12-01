package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

func read_from_file(filename string) ([]int, []int) {
	file, err := os.Open(filename)
	var text1 []int
	var text2 []int
	if err != nil {
		return nil, nil
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		text := strings.Fields(scanner.Text())
		first, _ := strconv.Atoi(text[0])
		sec, _ := strconv.Atoi(text[1])
		text1 = append(text1, first)
		text2 = append(text2, sec)
	}
	return text1, text2
}

func part1(text1 []int, text2 []int, ch chan int) {
	sort.Ints(text1)
	sort.Ints(text2)
	res := 0
	for i := 0; i < len(text1); i++ {
		diff := text1[i] - text2[i]
		if diff < 0 {
			diff = -diff
		}
		res += diff
	}
	ch <- res
}

func part2(text1 []int, text2 []int, ch chan int) {
	freq := make(map[int]int)
	res := 0
	for _, elem := range text2 {
		freq[elem] += 1
	}
	for _, elem := range text1 {
		res += elem * freq[elem]
	}
	ch <- res
}

func main() {
	text1, text2 := read_from_file("input.txt")
	chan1 := make(chan int)
	chan2 := make(chan int)
	go part1(text1, text2, chan1)
	go part2(text1, text2, chan2)
	<-chan1
	<-chan2
}
