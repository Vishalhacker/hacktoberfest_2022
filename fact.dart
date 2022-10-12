import 'dart:io';

findFactorial(int no) {
  if (no == 1) {
    return 1;
  }
  return no * findFactorial(no - 1);
}

main() {
  print("Enter a number : ");
  var no = int.parse(stdin.readLineSync());
  print('Factorial of $no is ${findFactorial(no)}');
}
