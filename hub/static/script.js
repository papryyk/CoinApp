"use strict";

function sortTable(n) {
  var i,
    x,
    y,
    switching,
    switchingCount,
    dir,
    table,
    rows,
    sortFieldType = 0;

  table = document.getElementById("coins");
  rows = table.rows;
  switching = true;
  dir = rows[0].getElementsByTagName("TH")[n].value;
  sortFieldType = rows[0].getElementsByTagName("TH")[n].textContent;

  while (switching) {
    switchingCount = 0;
    for (i = 1; i < rows.length - 1; i++) {
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (sortFieldType == "Coin") {
        x = x.innerHTML;
        y = y.innerHTML;
      } else if (sortFieldType == "24h") {
        x = Number(x.textContent.substr(0, x.textContent.length - 8));
        y = Number(y.textContent.substr(0, y.textContent.length - 8));
      } else {
        x = Number(x.textContent);
        y = Number(y.textContent);
      }
      if (dir == "asc") {
        if (y < x) {
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switchingCount++;
        } else if (i == rows.length - 2 && switchingCount == 0) {
          switching = false;
          rows[0].getElementsByTagName("TH")[n].value = "desc";
        }
      } else {
        if (y > x) {
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switchingCount++;
        } else if (i == rows.length - 2 && switchingCount == 0) {
          switching = false;
          rows[0].getElementsByTagName("TH")[n].value = "asc";
        }
      }
    }
  }
}
