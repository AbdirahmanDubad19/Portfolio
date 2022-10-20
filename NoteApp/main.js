const notesSection = document.getElementById('app');
const btnAddNote = notesSection.querySelector('.add-note');
 
//8 display notes 
getNotes().forEach(note => {
    const noteElement = createNotesE(note.noteId, note.content);
    notesSection.insertBefore(noteElement, btnAddNote)
}); 

function getNotes() {
//2. Display the notes held/stored in local storage
//                                              key
    return JSON.parse(localStorage.getItem("note") || "[]");
}
//7 btnAddnote listens for a click event and call the addNote function
btnAddNote.addEventListener("click", () => addNote());


function saveNotes(notes) {
// 1 set key value pairs for the local storage, using stringnify before it is saved
    //                      key         value
    localStorage.setItem("note", JSON.stringify(notes));
}
//4  The createNoteElement function with noteID an content passed in as parameter
function createNotesE(noteId, content) {
// element is js representation of textarea and is yet to be amended to the DOM
    const element = document.createElement("textarea");
    console.log("This is from the element", element)
    // text area
// placeholder with instrunction will be as default in the text area that is created
// when the note button is clicked

// the css rule for ".note" set in style.css is used to create the
// note using the properties and values
    element.classList.add("note");
    console.log("This is from the element and note", element)
    element.value = content; // captures the content/data in the textarea
    element.placeholder = "Click to Enter Note\nClick outside to save\nDouble Click to delete";
// 4a the addEventListener listens for a change event in the textarea(element) then
//save and/update the content inside the text area
//element = textarea
    element.addEventListener("change", () => {
        updateNote(noteId, element.value);
    }) ; 
//4b the addEventListener listens for a doubleClick event in the textarea(element) then
// perform a conditional check
    element.addEventListener("dblclick", () => {
        // notesSection.style.backgroundColor = "red";
        notesSection.getElementsByClassName('note').backgroundColor = "red";
        // myNote.style.backgroundColor = "blue";
        const doDelete = confirm("Do you want to delete this note?");
        if (doDelete) {
            
            console.log("note section",notesSection)
             //call the delete function
            deleteNote(noteId,element);
            console.log("From delete",noteId, element)
            element.style.backgroundColor = "blue";
            // console.log("my elementor", notesSection.getElementsByClassName('note'));
            console.log("my elementor", notesSection.getElementsByClassName('note'))
            
        }
    });
    //return the textarea with it's conent 
    return element;
}

function addNote() {
// 3. get all the notes that exists inside the local storage
// pass the getNotes() to the const variable "eNotes"
    const eNotes = getNotes();
//creates an auto generate number 
    const objNote = {
        noteId: Math.round(Math.random() * 100),
        content: ""
    }  // note element
    const noteElement = createNotesE(objNote.noteId, objNote.content);
    notesSection.insertBefore(noteElement, btnAddNote);
     //append notes to notes that exist
    eNotes.push(objNote);
    // save new notes to the localstorage
    saveNotes(eNotes);
}
//5 the updateNote function
function updateNote(noteId, newContent) {
     // create const variable to hold an exiting note and assign the getNotes function as a value 
    const eNotes = getNotes();
     //the filter methods allows a criteria to be use to filer an arry/items/string...etc 
    const noteToUpdate = eNotes.filter(note => note.noteId == noteId) [0];

    noteToUpdate.content = newContent;
    saveNotes(eNotes);
}

// 6  delete a note
function deleteNote(noteId, element ) {

    const eNotes = getNotes().filter(note => note.noteId != noteId);
    

        saveNotes(eNotes);
      
        notesSection.removeChild(element);
      
       

}

