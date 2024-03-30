function getRecommendation() {
  var selectedLanguage = document.getElementById("language-select").value;
  var selectedDifficulty = document.getElementById("difficulty-select").value;

  fetch("/recommend", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      topic: selectedLanguage,
      difficulty_level: selectedDifficulty,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      displayRecommendation(data.solutions);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
function displayRecommendation(recommendations) {
  var recommendationContainer = document.getElementById("recommendation");
  recommendationContainer.innerHTML = '<h3 class="mt-3">Recommendations:</h3>';

  if (recommendations.length === 0) {
    recommendationContainer.innerHTML +=
      '<p class="text-muted">No recommendations found.</p>';
  } else {
    var listHTML =
      '<ul class="list-group list-group-flush recommendation-list">';
    recommendations.forEach((recommendation) => {
      listHTML += `<li class="list-group-item">${recommendation}</li>`;
    });
    listHTML += "</ul>";
    recommendationContainer.innerHTML += listHTML;
  }
}
