$(document).ready(function () {

    // when menu icon is clicked, display a div containing nav links
    navMenu = document.getElementById('menuIcon');
    navMenu.addEventListener("click", function () {
        $("#navDisplay").removeClass("hidden");
    });

    // when closeButton is clicked, hide the div containing nav links
    $("#closeButton").click(function () {
        $("#navDisplay").addClass("hidden");
    });

    // Print contents of div
    document.getElementById("printButton").addEventListener("click", 
    function () {
        var printContents = document.getElementById('printContent').innerHTML;
        var originalContents = document.body.innerHTML;
        document.body.innerHTML = printContents;
        window.print();
        document.body.innerHTML = originalContents;

        /* NOTE: Webpage must be reloaded else JS will not load nor work after
            printButton has been clicked.
            'true' will force the page to reload from the server. 
            'false' will reload from cache, if available.
        */
        window.location.reload(false); 
    });

//     function printThis(divName) {
//         var printContents = document.getElementById(divName).innerHTML;
//         var originalContents = document.body.innerHTML;
   
//         document.body.innerHTML = printContents;
//         window.print();
//         document.body.innerHTML = originalContents;

//         console.log("print success")
//    }

//    $("#printButton").click(printThis("printContent"));
    // document.getElementById("printButton").addEventListener("click", 
    //     printThis("printContent"));

});