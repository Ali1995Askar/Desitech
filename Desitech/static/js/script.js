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


const counters= document.querySelectorAll('.counter');
const speed = 200;
counters.forEach(counter => {
    const updcount = () =>{
        const target= counter.getAttribute('data-target');
        const count= +counter.innerText;
        const score= target / speed;
        if (count < target){
            counter.innerText = count + score;
            setTimeout(updcount, 2);
        } else{
            counter.innerText = target;
        };
    };
    updcount();
});

