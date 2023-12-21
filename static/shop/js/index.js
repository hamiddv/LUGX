
//////////// our shop

// Create an instance of Isotope with the correct options
const list = new Isotope(document.getElementById("games-container"), {
    itemSelector: ".js-game",
    layoutMode: "fitRows",
});

// Add click event listeners to the filter buttons
const filterButtons = document.querySelectorAll(".js-filter-game")

filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
        filterGames(event.target.getAttribute("data-filter"))
        console.log(event.target.getAttribute("data-filter"))
    })
})

// Function to filter the games based on the category name
function filterGames(categoryName) {
    list.arrange({filter: `.${categoryName}`});
}
