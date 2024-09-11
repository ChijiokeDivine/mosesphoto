$(document).ready(function(){

    $('.review-form').on('submit', function(e) {
        e.preventDefault();

        var reviewname = $('#reviewname').val();
        var reviewemail = $('#reviewemail').val();
        var review = $('#review').val();
        var errorMessage = $('#ContactErrorMessage');
        var isValid = true;

        // Validate full name
        if (reviewname.trim() === '') {
            errorMessage.text('Please enter your full name.');
            isValid = false;
        } 
        // Validate email address
        else if (reviewemail.trim() === '') {
            errorMessage.text('Please enter your email address.');
            isValid = false;
        } else if (!isValidEmailAddress(reviewemail)) {
            errorMessage.text('Please enter a valid email address.');
            isValid = false;
        } 

        // Validate message
        else if (review.trim() === '') {
            errorMessage.text('Please enter your message or enquiry.');
            isValid = false;
        }

        if (isValid) {
            $('#reviewSubmit').prop('disabled', true).html('Sending <span class="spinner-border spinner-border-sm" style="margin-left: 3px;" role="status" aria-hidden="true"></span> ');
            const path = window.location.pathname;
            const parts = path.split('/');
            const reviewID = parts[parts.length - 2];
            $.ajax({
                type: 'POST',
                url: '/submit_review/' + reviewID + '/', 
                data: $(this).serialize(),
                success: function(response) {
                    if (response.message === 'Booking successfully created!') {
                        showNotification();
                        $('.review-form')[0].reset(); // Reset the form after successful submission
                    } else {
                        // Handle server-side validation errors
                        errorMessage.text(response.message || 'An error occurred. Please try again.');
                        setTimeout(() => {
                            errorMessage.text("");
                        }, 4000);
                    }
                },
                error: function() {
                    // Handle AJAX errors
                    errorMessage.text('An error occurred while submitting the form.');
                    setTimeout(() => {
                        errorMessage.text("");
                    }, 4000);
                },
                complete: function() {
                    $('#reviewSubmit').prop('disabled', false).html('Send');
                }
            });
        }
    });

    function showNotification() {
        var notification = document.getElementById("notification");
        notification.style.display = "block";
        
        setTimeout(function() {
            notification.style.display = "none";
        }, 5000); 
    }

    function isValidEmailAddress(email) {
        // Regular expression for email validation
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});
