"use strict";

var myChart = false

document.addEventListener('scroll', function () {
  var mainInformation = document.getElementById('main-information');
  var mainImage = document.getElementById('image')

  // Check if the user has scrolled beyond a certain threshold (e.g., 50 pixels)
  var scrollThreshold = 50;
  var isScrolled = window.scrollY > scrollThreshold;

  // Add or remove the 'scrolled' class based on the scroll position
  if (isScrolled) {
    mainInformation.classList.add('scrolled');
    mainImage.classList.add('scrolled')
  } else {
    mainInformation.classList.remove('scrolled');
    mainImage.classList.remove('scrolled')
  }
});

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


document.getElementById('type-a-coin').addEventListener('input', autoComplete);

function autoComplete() {
  document.getElementById("auto-complete-list").style.setProperty("display","block")

  var input = document.getElementById("type-a-coin")
  var filter = input.value.toLowerCase()
  var autoCompleteList = document.getElementById("auto-complete-list")
  var a = autoCompleteList.getElementsByTagName("a")

  for (var i = 0; i < a.length; i++) {
    var txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toLowerCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }

  document.addEventListener('click', function (event) {
    // Hide the dropdown when clicking outside the input and dropdown
    if (event.target !== input && event.target !== autoCompleteList) {
      autoCompleteList.style.display = 'none';
    }
  })
}

document.addEventListener('DOMContentLoaded', function () {
  var scrollLinks = document.querySelectorAll('.scroll-link');

  // Attach click event listener to each scroll link
  scrollLinks.forEach(function (link) {
    link.addEventListener('click', function (e) {
      e.preventDefault(); // Prevent the default link behavior

      var targetId = this.getAttribute('href').substring(1); // Get the target element's id

      // Find the target element
      var targetElement = document.getElementById(targetId);
      if (targetElement) {
        // Calculate the target scroll position (top - 90)
        var targetOffset = targetElement.offsetTop - 90;

        // Scroll to the target position
        window.scrollTo({
          top: targetOffset,
          behavior: 'smooth'
        });
      }
    });
  });
});

function searchOutcome(clickedSymbol) {
    var table = document.getElementById('coins');
  
    // Get all rows in the table
    var rows = table.getElementsByTagName('tr');
  
    // Iterate through rows
    for (var i = 1; i < rows.length; i++) {
      // Get the second <td> in the current row
      var zeroTd = rows[i].getElementsByTagName('td')[9];
  
      // Check if the value in the second <td> is "BTC"
      if (zeroTd.textContent === clickedSymbol) {
        // If found, get the value from the third <td>
        var currentPrice = rows[i].getElementsByTagName('td')[2].textContent;
        var currentPercentage = rows[i].getElementsByTagName('td')[3].textContent;
        var currentMin = rows[i].getElementsByTagName('td')[7].textContent;
        var currentMax = rows[i].getElementsByTagName('td')[8].textContent;
        var img = document.createElement("img")
        img.src = rows[i].getElementsByTagName('td')[10].innerHTML;
        img.id="search-icon"
        var currentCoinName = rows[i].getElementsByTagName('td')[11].textContent;
        var historyPrice = rows[i].getElementsByTagName('td')[12].textContent;
        historyPrice = historyPrice.split(",")
        historyPrice.pop()
        console.log(historyPrice)
        var uploadTime = rows[i].getElementsByTagName('td')[13].textContent;
        uploadTime = uploadTime.split(",")
        uploadTime.pop()
        console.log(uploadTime)
        
        document.getElementById("coin-name-p").textContent = ""
        document.getElementById("coin-name-p").append(img)
        document.getElementById("coin-name-p").append(`${currentCoinName} (${zeroTd.textContent.toUpperCase()})`)
        document.getElementById("value-p").innerHTML = currentPrice
        document.getElementById("percentage-p").innerHTML = currentPercentage
        document.getElementById("description-min").innerHTML = `Min: ${currentMin}`
        document.getElementById("description-max").innerHTML = `Max: ${currentMax}`
        document.getElementById("binance-href").href = `https://www.binance.com/pl/price/${currentCoinName.split(" ")[0]}`
        document.getElementById("coingecko-href").href = `https://www.coingecko.com/pl/waluty/${currentCoinName.split(" ").join("-").toLowerCase()}`
        document.getElementById("kucoin-href").href = `https://www.kucoin.com/pl/price/${zeroTd.textContent.toUpperCase()}`
        document.getElementById("bitbay-href").href = `https://www.coinbase.com/pl/price/arbitrum${currentCoinName.split(" ")[0]}`
        document.getElementById("news-href").href = `https://twitter.com/search?q=${zeroTd.textContent}%20coin&src=typed_query&f=top`
      }
    }
    if (myChart != false) {myChart.destroy()}
    var ctx = document.getElementById('myChart').getContext('2d');
    myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: uploadTime,
        datasets: [{
          label: "test",
          data: historyPrice,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)', 
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
        }
      },
        elements: {
          point: {
            radius: 0
          }
        }
      }
    });
    }

    
  

