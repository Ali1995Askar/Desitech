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