package main
import "fmt"

func countDown(number int) {

  // display the number
  fmt.Println(number)

  // recursive call by decreasing number
  countDown(number - 1)

  }

func main() {
  countDown(3)
}
