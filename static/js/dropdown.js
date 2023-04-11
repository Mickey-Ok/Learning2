// Toggle dropdown menu
var dropdowns = document.getElementsByClassName("dropdown-menu");
for (var i = 0; i < dropdowns.length; i++) {
  dropdowns[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}
