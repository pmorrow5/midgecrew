var x = setInterval(function() {
    var oko_day = 20;
    var oko_month = 6;
    var oko_year;

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1;
    var yyyy = today.getFullYear();

    if (mm > oko_month || mm == oko_month && dd > oko_day){
        oko_year = yyyy + 1;
    } else {
        oko_year = yyyy
    }

    var distance = new Date(oko_year, oko_month, oko_day, 12, 0, 0, 0) - today

    var days = Math.floor(distance / (1000 * 60 * 60 * 24))
    var hours = Math.floor(distance % (1000 * 60 * 60 * 24) / (1000 * 60 * 60))
    var minutes = Math.floor(distance % (1000 * 60 * 60) / (1000 * 60))
    var seconds = Math.floor(distance % (1000 * 60) / (1000))

    document.getElementById("countdown").innerHTML = days + " days, " + hours + " hours, " + minutes + " minutes, and " + seconds + " seconds until Okoboji!"
}, 1000);