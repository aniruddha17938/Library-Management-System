document.getElementById("add-category-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("category-name").value;
    const response = await fetch("/add-category", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
    });
    const result = await response.json();
    alert(result.message || result.error);
});

document.getElementById("add-book-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const title = document.getElementById("book-title").value;
    const author = document.getElementById("book-author").value;
    const category = document.getElementById("book-category").value;

    const response = await fetch("/add-book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, author, category }),
    });
    const result = await response.json();
    alert(result.message || result.error);
});

document.getElementById("list-books").addEventListener("click", async () => {
    const response = await fetch("/list-books");
    const books = await response.json();

    const tableBody = document.querySelector("#output-table tbody");
    tableBody.innerHTML = ""; // Clear previous rows

    for (const [category, bookList] of Object.entries(books)) {
        bookList.forEach((book) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${book.id}</td>
                <td>${book.title}</td>
                <td>${book.author}</td>
                <td>${category}</td>
                <td>${book.available ? "Available" : "Issued"}</td>
            `;
            tableBody.appendChild(row);
        });
    }
});
