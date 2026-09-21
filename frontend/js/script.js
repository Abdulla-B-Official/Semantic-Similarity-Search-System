const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");
const resultsContainer = document.getElementById("resultsContainer");
const resultCount = document.getElementById("resultCount");
const statusMessage = document.getElementById("statusMessage");


searchButton.addEventListener("click", performSearch);


searchInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        performSearch();
    }
});


async function performSearch() {

    const searchQuery = searchInput.value.trim();

    if (!searchQuery) {
        statusMessage.textContent = "Please enter a search query.";
        return;
    }

    searchButton.disabled = true;
    searchButton.textContent = "Searching...";
    statusMessage.textContent = "Finding similar documents...";
    resultsContainer.innerHTML = "";
    resultCount.textContent = "";


    try {

        const response = await fetch("/api/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                query: searchQuery
            })
        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.error || "Search failed.");
        }


        displayResults(data.results);

        statusMessage.textContent = `Search completed for "${data.query}".`;

    } catch (error) {

        statusMessage.textContent = error.message;

        resultsContainer.innerHTML = `
            <div class="empty-state">
                Unable to complete the search.
            </div>
        `;

    } finally {

        searchButton.disabled = false;
        searchButton.textContent = "Search";
    }
}


function displayResults(results) {

    resultCount.textContent = `${results.length} results`;

    if (results.length === 0) {
        resultsContainer.innerHTML = `
            <div class="empty-state">
                No similar documents found.
            </div>
        `;
        return;
    }


    resultsContainer.innerHTML = results.map((result, index) => {

        const similarityPercentage =
            (result.similarity_score * 100).toFixed(2);

        return `
            <article class="result-card">

                <div class="result-meta">

                    <span class="badge">
                        Rank ${index + 1}
                    </span>

                    <span class="badge">
                        ID: ${result.document_id}
                    </span>

                    <span class="badge">
                        ${result.category}
                    </span>

                    <span class="badge similarity-score">
                        Similarity: ${similarityPercentage}%
                    </span>

                </div>

                <h3>${escapeHtml(result.title)}</h3>

                <p class="result-content">
                    ${escapeHtml(result.content)}
                </p>

            </article>
        `;

    }).join("");
}


function escapeHtml(text) {

    const element = document.createElement("div");

    element.textContent = text;

    return element.innerHTML;
}