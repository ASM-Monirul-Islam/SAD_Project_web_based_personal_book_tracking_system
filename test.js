var search_btn = document.getElementById("search_btn");

search_btn.addEventListener("click", function () {
    var search = document.getElementById("search").value;

    fetch("https://www.googleapis.com/books/v1/volumes?q=" + search)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {

            console.log(data);

            $(".card").empty(); // ✅ FIX: clear old results

            if (!data.items) return;

            for (var i = 0; i < data.items.length; i++) {

                var item = data.items[i].volumeInfo;

                var title = item.title || "No Title";
                var author = item.authors ? item.authors.join(", ") : "Unknown Author";
                var img = item.imageLinks ? item.imageLinks.thumbnail : "";

                var titleEl = $("<h5 class='p-2 bg-primary text-white'>" + title + "</h5>");
                var authorEl = $("<p class='p-1 bg-success text-white'>" + author + "</p>");
                var imgEl = img ? $("<img width='150' src='" + img + "'/>") : "";

                titleEl.appendTo(".card");
                imgEl.appendTo(".card");
                authorEl.appendTo(".card");
            }
        });
});