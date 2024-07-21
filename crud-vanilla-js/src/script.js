let data = getBooks();
const tableBody = document.getElementById("books-body");
const submitButton = document.getElementById('submit-button');

document.addEventListener('DOMContentLoaded', () => {
    renderTable()
    // saveBooks(getSampleBooks());
});

function getBooks() {
    const storedBooks = localStorage.getItem('books') ? localStorage.getItem('books') : [];
    const books = JSON.parse(storedBooks);
    return books;
}

function saveBooks(books) {
    localStorage.setItem('books', JSON.stringify(books));
}

function sortBooks(sortBy) {
    data.sort((a, b) => a[sortBy].localeCompare(b[sortBy]));
    renderTable();
}

function renderTable() {
    tableBody.innerHTML = '';
    data.forEach(book => {
        const tr = document.createElement('tr')
        const id = book.id;
        const authorColumn = document.createElement('td');
        const titleColumn = document.createElement('td');

        tr.id = id;
        authorColumn.innerHTML = book.author;
        titleColumn.innerHTML = book.title;

        tr.appendChild(authorColumn);
        tr.appendChild(titleColumn);
        const buttons = crateActionButtons(id);
        tr.appendChild(buttons);
        tableBody.appendChild(tr);
    });
}

form.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const book = Object.fromEntries(formData.entries());
    book['id'] = new Date().getTime();
    data.push(book);
    saveBooks(data);
    resetInputs();
    renderTable();
});

function resetInputs() {
    document.getElementById('input-author').value = '';
    document.getElementById('input-title').value = '';
}

function onClickDelete(id) {
    data = data.filter(book => book.id !== id);
    saveBooks(data);
    const row = document.getElementById(id);
    row.remove();
}

function onClickEditConfirm(id) {
    const formData = new FormData(form);
    const updatedBook = Object.fromEntries(formData.entries());

    updatedBook['id'] = id;
    const index = data.findIndex(book => book.id === id);
    data[index] = updatedBook;

    saveBooks(data);
    resetInputs();
    renderTable();

    submitButton.innerText = 'Add';
    submitButton.onclick = undefined;
}

function onClickEdit(id) {
    const book = data.find(book => book.id === id);
    document.getElementById('input-author').value = book.author;
    document.getElementById('input-title').value = book.title;
    submitButton.innerText = 'Edit';
    submitButton.onclick = function () {
        onClickEditConfirm(id);
    }
    document.getElementById('cancel-button').style.display = 'inline-block';
}

function crateActionButtons(id) {
    const editButton = document.createElement('button');
    editButton.innerText = 'Edit';
    editButton.className = 'button';
    editButton.onclick = function () {
        onClickEdit(id);
    }

    const deleteButton = document.createElement('button');
    deleteButton.innerText = 'Delete';
    deleteButton.className = 'button';
    deleteButton.onclick = function () {
        onClickDelete(id);
    }

    const buttonsContainer = document.createElement('td');
    buttonsContainer.className = 'column-center';
    buttonsContainer.appendChild(deleteButton);
    buttonsContainer.appendChild(editButton);
    return buttonsContainer;
}

function cancelEdit() {
    document.getElementById('cancel-button').style.display = 'none';
    document.getElementById('submit-button').innerText = 'Add';
    submitButton.onclick = undefined;
    resetInputs();
}

function getSampleBooks() {
    const b = [
        ['George Orwell', '1984'],
        ['Jane Austen', 'Pride and Prejudice'],
        ['J.K. Rowling', 'Harry Potter and the Sorcerers Stone'],
        ['Harper Lee', 'To Kill a Mockingbird'],
        ['F. Scott Fitzgerald', 'The Great Gatsby'],
        ['J.R.R. Tolkien', 'The Hobbit'],
        ['Gabriel García Márquez', 'One Hundred Years of Solitude'],
        ['Ernest Hemingway', 'The Old Man and the Sea'],
        ['Mark Twain', 'Adventures of Huckleberry Finn'],
        ['Mary Shelley', 'Frankenstein']
    ];
    return b.map(([author, title], index) => {
        return {
            id: index,
            author,
            title,
        }
    })
}