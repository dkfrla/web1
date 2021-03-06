//https://stackoverflow.com/questions/55520415/how-to-filter-data-of-a-html-table-with-a-drop-down-menu-with-javascript

function filterTable(index) {
  // Variables
  let dropdown, table, rows, cells, country, filter;
  dropdown = document.getElementsByClassName("Dropdown");
  table = document.getElementById("myTable");
  rows = table.getElementsByTagName("tr");
  filter = dropdown[index].value;

  // Loops through rows and hides those with countries that don't match the filter
  for (let row of rows) { // `for...of` loops through the NodeList
    cells = row.getElementsByTagName("td");
    country = cells[index] || null; // gets the 2nd `td` or nothing
    // if the filter is set to 'All', or this is the header row, or 2nd `td` text matches filter
    if (filter === "All" || !country || (filter === country.textContent)) {
      row.style.display = ""; // shows this row
    }
    else {
      row.style.display = "none"; // hides this row
    }
  }
}
