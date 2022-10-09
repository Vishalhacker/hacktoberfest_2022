package main
import "fmt"

// outer function
func greet(name string) {

  // inner function
  var displayName = func() {
    fmt.Println("Hi", name)
  }

  // call inner function
  displayName()

}

func main() {

  // call outer function
  greet("John")  // Hi John

}
