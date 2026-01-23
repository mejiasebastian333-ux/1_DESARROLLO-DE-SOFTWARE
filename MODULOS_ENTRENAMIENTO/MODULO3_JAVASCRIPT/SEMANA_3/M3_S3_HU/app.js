// DOM element selection
const noteInput = document.getElementById("noteInput");
const addBtn = document.querySelector("#addBtn");
const notesList = document.getElementById("notesList");

// Check elements in console
console.log("Input:", noteInput);
console.log("Button:", addBtn);
console.log("UL:", notesList);

// In-memory notes array
let notes = [];

// Load notes from Local Storage
const storedNotes = localStorage.getItem("notes");

if (storedNotes) {
  notes = JSON.parse(storedNotes);
  notes.forEach(note => renderNote(note));
  console.log(`Loaded ${notes.length} notes from Local Storage`);
}

// Add note
addBtn.addEventListener("click", () => {
  const noteText = noteInput.value.trim();

  if (noteText === "") {
    alert("The note cannot be empty");
    return;
  }

  notes.push(noteText);
  saveNotes();
  renderNote(noteText);

  console.log("Note added:", noteText);

  noteInput.value = "";
  noteInput.focus();
});

// Render note in DOM
function renderNote(text) {
  const li = document.createElement("li");
  li.textContent = text;

  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "Delete";

  deleteBtn.addEventListener("click", () => {
    notesList.removeChild(li);
    notes = notes.filter(note => note !== text);
    saveNotes();
    console.log("Note deleted:", text);
  });

  li.appendChild(deleteBtn);
  notesList.appendChild(li);
}

// Save to Local Storage
function saveNotes() {
  localStorage.setItem("notes", JSON.stringify(notes));
  console.log("Notes saved:", notes);
}
