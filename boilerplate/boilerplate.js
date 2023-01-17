const fs = require("fs");

// 문자 하나만 입력받을 경우
let inputOneString = fs.readFileSync("/dev/stdin").toString()

// 한칸 띄어쓰기로 구분
// input[0], input[1] 배열에서 꺼내쓰면 된다.
let inputMultiString = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")

// 줄바꿈으로 구분
let inputSepertateByNewline = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")

// 만약 인풋값이 숫자라면
let inputMultiIntegter = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((el) => +el)