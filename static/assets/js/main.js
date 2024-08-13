
$(function () {
    /**
     * ===============================================
     *      TABLE OF CONTENT
     * ===============================================
     * # Loader
     * # Real Time
     * # Real Time Weather
     * # Popup Menu
     * # Gsap Smooth Scroll
     * # Experience Popup
     * # Custom Cursor
     *
     */


    /* ===== Loader ===== */
    $(window).on('load', function () {
        setTimeout(() => {
            $('.preloader-wrap').delay('500').fadeOut(1000);
            $('#progress-bar-container1').delay('500').fadeOut(1000);
            scroll_animations();
        }, 200);
        setTimeout(() => {
            $('.hero-sec .hero-footer-wrap.scroll-from-bottom').addClass('animated');
        }, 800);
        
    });
    // Get the progress bar container and the progress bar elements
    const progressBarContainer = document.getElementById('progress-bar-container1');
    const progressBar = document.getElementById('progress-bar1');
    
    let progress = 0;
    
    // Update the progress bar based on the document's ready state
    function updateProgressBar() {
      switch (document.readyState) {
        case 'loading':
          progress = 0;
          break;
        case 'interactive':
          progress = 50;
          break;
        case 'complete':
          progress = 100;
          break;
      }
      progressBar.style.width = `${progress}%`;
    }
    
    // Add an event listener to the document's ready state change event
    document.addEventListener('readystatechange', updateProgressBar);
    
    // Update the progress bar initially
    updateProgressBar();



    /* ===== Real Time ===== */
    if ($('#realtime').length) {
        startTime();
    }
    function startTime() {
        var today = new Date();
        var h = today.getHours();
        var m = today.getMinutes();
        var s = today.getSeconds();
        m = checkTime(m);
        s = checkTime(s);
        document.getElementById('realtime').innerHTML =
            h + ":" + m + ":" + s;
        var t = setTimeout(startTime, 500);
    }
    function checkTime(i) {
        if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
        return i;
    }


    /* ===== Real Time Weather ===== */
    const apiKey = '1906ccd7aa6d7c3683f1b293ee212f01';
    const city = 'sylhet';
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const temperature = data.main.temp;
            const latitude = data.coord.lat;
            const longitude = data.coord.lon;

            // Format latitude
            const latDegrees = Math.floor(latitude);
            const latMinutes = Math.floor((latitude - latDegrees) * 60);
            const latSeconds = ((latitude - latDegrees) * 60 - latMinutes) * 60;

            // Format longitude
            const lonDegrees = Math.floor(longitude);
            const lonMinutes = Math.floor((longitude - lonDegrees) * 60);
            const lonSeconds = ((longitude - lonDegrees) * 60 - lonMinutes) * 60;

            // document.getElementById('temperature').textContent = `${temperature}°C`;
            document.getElementById('coordinates').textContent = `${latDegrees}° ${latMinutes}' ${latSeconds.toFixed(4)}" N`; //, ${lonDegrees}° ${lonMinutes}' ${lonSeconds.toFixed(4)}" E
        })
        .catch(error => {
            console.log('Error fetching data:', error);
        });



        /* ===== Popup Menu ===== */
        $(document).on('click', '.header-wrap .header-right .theme-btn', function (e) {
            e.preventDefault();
            $('.popup-menu-wrap').addClass('active');
        });

        $(document).on('click', '.popup-menu-close-btn .icon', function () {
            $('.popup-menu-wrap').removeClass('active');
        });



    window.addEventListener('scroll', {
        scroll_animations
    });



    /* ===== # Experience Popup ===== */
    $(document).on('click', '.experience-box .experience-button-box .experience-button', function (e) {
        e.preventDefault();
        $('.experience-popup').addClass('active');
    });
    $(document).on('click', '.experience-popup .experience-popup-content-wrap .close-experience-popup-btn', function () {
        $('.experience-popup').removeClass('active');
    });
        

    const movingElement = document.getElementById('movingElement');

    document.addEventListener('mousemove', (event) => {
    const { innerWidth: width, innerHeight: height } = window;
    gsap.to(movingElement, {
        x: (event.clientX - width / 2) * -0.015,
        y: (event.clientY - width / 2) * -0.015,
        duration: 0.4,
        ease: "power3.out"
    });
    });


    

    

});



function scroll_animations() {
    // var allow_on_mobile = !0;
    // if (typeof config_scroll_animation_on_mobile !== "undefined") allow_on_mobile = config_scroll_animation_on_mobile;
    // if (allow_on_mobile == !1 && is_mobile_device) return;
    var defaults = {
        ease: 0.05,
        animation: "fade_from_bottom",
        once: !1,
    };
    gsap.utils.toArray(".scroll-animation").forEach(function (box) {
        var gsap_obj = {};
        var settings = {
            // ease: box.dataset.animationEase || defaults.ease,
            duration: box.dataset.animationDuration || defaults.duration,
        };
        var animations = {
            slide_up: {
                y: -180,
            },
            slide_down: {
                y: 180,
            },
            slide_up2: {
                y: -100,
            },
            slide_down2: {
                y: 100,
            },
            fade_from_bottom: {
                y: 180,
                opacity: 0,
            },
            fade_from_top: {
                y: -180,
                opacity: 0,
            },
            fade_from_left: {
                x: -180,
                opacity: 0,
            },
            fade_from_right: {
                x: 180,
                opacity: 0,
            },
            fade_in: {
                opacity: 0,
            },
            rotate_up: {
                y: 180,
                rotation: 10,
                opacity: 0,
            },
            bronx_zoom_out: {
                scale: 2,
            },
            slide_and_scale: {
                // y: 180,
                scale: 1,
                opacity: 1
            },
        };
        var globalWidth = window.innerWidth;
        if (globalWidth > 809) {
            var transWidth = '10%';
        } else {
            var transWidth = '30%';
        }
        var scroll_trigger = {
            scrollTrigger: {
                trigger: box,
                once: defaults.once,
                // start: "top bottom+=20%",
                start: "top bottom+="+transWidth,
                toggleActions: "play none none reverse",
                markers: !1,
                onUpdate: function(self) {
                    // Get the current position of the box relative to the viewport
                    // var bounding = box.getBoundingClientRect();
                    // var offsetTopFromViewport = bounding.top;

                    
                    // if (box.dataset.animation == 'slide_and_scale') {
                    //     console.log("Offset from top:", offsetTopFromViewport);

                    //     // Example: Toggle opacity and scale based on offset
                    //     if (offsetTopFromViewport < 0) {
                    //         const replaceVal = Math.abs(offsetTopFromViewport);
                    //         console.log(replaceVal, 'if');
                    //         // box.style.transform = `translateY(${replaceVal}px)`;
                    //         gsap.to(box, { y: replaceVal, duration: 0.5 });
                    //     } else {
                    //         console.log('else');
                    //         // box.style.transform = `translateY(0px)`;
                    //         gsap.to(box, { y: 0, duration: 0.5 });
                    //     }
                    // }
                }
            },
        };
        if (box.dataset.animation == 'bronx_zoom_out') {
            scroll_trigger = {
                scrollTrigger: {
                    trigger: box,
                    once: defaults.once,
                    // start: "top bottom+=20%",
                    start: "top bottom",
                    toggleActions: "play none none reverse",
                    markers: !1,
                },
            };
        }
        jQuery.extend(gsap_obj, settings);
        jQuery.extend(gsap_obj, animations[box.dataset.animation || defaults.animation]);
        jQuery.extend(gsap_obj, scroll_trigger);
        gsap.from(box, gsap_obj);
    });
}

