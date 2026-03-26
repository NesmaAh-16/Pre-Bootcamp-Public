
function reverseString(str) {
    var output = "";
    for (let i = str.length - 1; i >= 0; i--) {
        output = output + str[i];
    }
    return output;
}
console.log(reverseString("Bra"))


var vowels = "aeiouAEIOU";
function countVowels(str) {
    var count = 0;
    for (char of str) {
        if (vowels.includes(char))
            count++;
    }
    return count;
}
var input = countVowels("braa");
console.log(input);



var vowels = ["a", "e", "i", "u", "o", "A", "I", "O", "E", "U"];
function countVowels(str) {
    var count = 0;
    for (var i = 0; i <= str.length; i++) {
        if (vowels.includes(str[i]))
            count++;
    }
    return count;
}
console.log(countVowels("shaima"));



function isPalindrome(str) {
    let reversedStr = "";
    for (let i = str.length - 1; i >= 0; i--) {
        reversedStr += str[i];
    }
    if (str === reversedStr) {
        return true;
    } else {
        return false;
    }
}

console.log(isPalindrome("dad"));


function findLongestWord(statement = "I am not a Barcelona fan") {
  let words = statement.split(" ");
  let longest = words[0];
  for (let i = 1; i < words.length; i++) {
    if (words[i].length > longest.length) {
      longest = words[i];
    }
  }
  console.log("The longest word is: " + longest);
}

findLongestWord();


function findCases(str) {
    var output = {
        countVowels: 0,
        digits: 0,
        spaces: 0,
        others: 0
    };
    var vowels = "aeiouAEIOU";

    for (var char of str) {
        if (vowels.includes(char)) {
            output.countVowels++;
        }
        else if (char === " ") {
            output.spaces++;
        }
        else if (char >= '0' && char <= '9') {
            output.digits++;
        }
        else {
            output.others++;
        }
    }
    return output;
}

var result = findCases("shaimaa 1234");
console.log(result);


function feedback(str) {
  let msg = "";
  switch (str) {
    case ("A", "a"):
      msg = "Excellent";
      break;
    case ("B", "b"):
      msg = "Good";
      break;
    case ("C", "c"):
      msg = "You passed";
      break;
    case ("D", "d"):
      msg = "Need improvement";
      break;
    case ("F", "f"):
      msg = "Failed";
      break;
    default:
      msg = "Invalid grade";
  }
  console.log(msg);
}

feedback("d");

