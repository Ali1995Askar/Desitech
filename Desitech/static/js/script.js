// var phoneNum = document.querySelector("#id_phone_number");
// window.intlTelInput(phoneNum, {
//     utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.min.js",
// });





// var mobileNum = document.querySelector("#id_mobile_number");
// window.intlTelInput(mobileNum, {
//     initialCountry: "auto",
//     geoIpLookup: function(success) {
//         // Get your api-key at https://ipdata.co/
//         fetch("https://api.ipdata.co/?api-key=test")
//             .then(function(response) {
//                 if (!response.ok) return success("");
//                 return response.json();
//             })
//             .then(function(ipdata) {
//                 success(ipdata.country_code);
//             });
//     },
//     utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.min.js",
// });


$("#id_country").change(function() {
    var url = $("#Countries").attr("data-cities-url");
    var countryId = $(this).val();
    $.ajax({
        url: url,
        data: { 'country': countryId },
        success: function(cities) {
            $("#id_city").html(cities);
        }
    });
});