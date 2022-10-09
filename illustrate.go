// Program to illustrate local variables

package main
import "fmt"

func addNumbers() {

  // local variables
  var sum int
  
  sum = 5 + 9

}


func main() {

  addNumbers()

  // cannot access sum out of its local scope
  fmt.Println("Sum is", sum)


}
