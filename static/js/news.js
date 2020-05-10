$(document).ready(function() {
  $.getJSON(
    "https://cryptic-ravine-96718.herokuapp.com/",
    null,
    function(data) {
      var news = document.getElementById("news");
      var newcol = document.createElement("ul");
      newcol.setAttribute("class", "list-inline");
      news.appendChild(newcol);
      for (var i = 0; i < data.news.length-2; i++) {
        var li = document.createElement("li");
        li.setAttribute("class", "list-inline-item");
        var card = document.createElement("div");
        card.setAttribute("class", "card");
        card.style.width = "15rem";
        card.style.marginRight = "1rem";
        card.style.marginBottom = "2rem";
        // card.style.border="2px solid black";
        card.style.boxShadow = "none";
        var card_title = document.createElement("h5");
        card_title.innerHTML = data.news[i].title;
        card_title.setAttribute("classs", "card-title");
        var news_img = document.createElement("img");
        news_img.setAttribute("src", data.news[i].img);
        news_img.setAttribute("class", "card-img-top");
        var btntoart = document.createElement("a");
        btntoart.setAttribute("class", "btn btn-main");
        btntoart.style.color = "#fff";
        btntoart.style.background = "#000";
        btntoart.setAttribute("href", data.news[i].link);
        btntoart.innerHTML = "Read More";
        var card_body = document.createElement("div");
        card_body.setAttribute("class", "card-body");
        card_body.appendChild(card_title);
        card_body.appendChild(btntoart);
        card.appendChild(news_img);
        card.appendChild(card_body);
        li.appendChild(card);
        newcol.appendChild(li);
      }
    }
  );
});

