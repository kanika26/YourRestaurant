function multiplyBy()
{
      num1 = document.getElementById("price").value;
      num2 = document.getElementById("quantity").value;
      document.getElementById("result").innerHTML = num1 * num2;
}

console.log(multiplyBy());