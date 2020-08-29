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


const counters = document.querySelectorAll('.counter');
const speed = 200;
counters.forEach(counter => {
    const updcount = () => {
        const target = counter.getAttribute('data-target');
        const count = +counter.innerText;
        const score = target / speed;
        if (count < target) {
            counter.innerText = count + score;
            setTimeout(updcount, 2);
        } else {
            counter.innerText = target;
        };
    };
    updcount();
});

// 

particlesJS('particles-js',

    {
        "particles": {
            "number": {
                "value": 30,
                "density": {
                    "enable": true,
                    "value_area": 800
                }
            },
            "color": {
                "value": ['#fff', '#a2d5f2', '#eb8f8f', ]
            },
            "shape": {
                "type": ["polygon", 'circle', 'triangle', "star"],
                "stroke": {
                    "width": 4,
                    "color": "#ddd"
                },
                "polygon": {
                    "nb_sides": 12
                },
                "image": {
                    "src": "",
                    "width": 100,
                    "height": 100
                }
            },
            "opacity": {
                "value": 0.8,
                "random": false,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {
                "value": 50,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 40,
                    "size_min": 0.1,
                    "sync": false
                }
            },
            "line_linked": {
                "enable": false,
                "distance": 150,
                "color": "#ffffff",
                "opacity": 0.4,
                "width": 1
            },
            "move": {
                "enable": true,
                "speed": 6,
                "direction": "none",
                "random": false,
                "straight": false,
                "out_mode": "out",
                "attract": {
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "canvas",
            "events": {
                "onhover": {
                    "enable": false,
                    "mode": "repulse"
                },
                "onclick": {
                    "enable": false,
                    "mode": "push"
                },
                "resize": true
            },
            "modes": {
                "grab": {
                    "distance": 400,
                    "line_linked": {
                        "opacity": 1
                    }
                },
                "bubble": {
                    "distance": 400,
                    "size": 40,
                    "duration": 2,
                    "opacity": 8,
                    "speed": 3
                },
                "repulse": {
                    "distance": 200
                },
                "push": {
                    "particles_nb": 4
                },
                "remove": {
                    "particles_nb": 2
                }
            }
        },
        "retina_detect": true,
        "config_demo": {
            "hide_card": false,
            "background_color": "#b61924",
            "background_image": "",
            "background_position": "50% 50%",
            "background_repeat": "no-repeat",
            "background_size": "cover"
        }
    }

);


var phoneNum = document.querySelector("#phoneNum");
window.intlTelInput(phoneNum, {
    separateDialCode: true,
    onlyCountries: ['eg', 'us', 'uk'],
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.min.js",
});

var mobileNum = document.querySelector("#mobileNum");
window.intlTelInput(mobileNum, {
    separateDialCode: true,
    onlyCountries: ['eg', 'us', 'uk'],
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.3/js/utils.min.js",
});