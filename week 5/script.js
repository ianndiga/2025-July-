// Part 1: Variables & Conditionals
let userLoggedIn = true;
let userName = "Ian";

if (userLoggedIn) {
  console.log("Welcome back, " + userName + "!");
} else {
  console.log("Please log in to continue.");
}

// Part 2: Functions
function calculateTotal(a, b) {
  return a + b;
}

function greetUser(name) {
  console.log("Hello, " + name + "! Glad you're here.");
}
console.log("Total:", calculateTotal(5, 7));
greetUser("Ian");

// Part 3: Loops
let courses = ["Web Development", "Database Systems", "AI"];

// For loop
for (let i = 0; i < courses.length; i++) {
  console.log("Course " + (i+1) + ": " + courses[i]);
}

// While loop countdown
let count = 3;
while (count > 0) {
  console.log("Countdown: " + count);
  count--;
}


// Part 4: DOM Manipulation

// 1. Change header text dynamically
document.querySelector("header h1").textContent = "Enhanced HTML5 Page (with JS)";

// 2. Add a new course dynamically
let courseList = document.querySelector("ul");
let newCourse = document.createElement("li");
newCourse.textContent = "Machine Learning";
courseList.appendChild(newCourse);

// 3. Add event listener to the form submit
let form = document.querySelector("form");
form.addEventListener("submit", function(event) {
  event.preventDefault(); // stop actual form submit
  alert("Form submitted! Thank you, " + document.getElementById("fullname").value);
});
