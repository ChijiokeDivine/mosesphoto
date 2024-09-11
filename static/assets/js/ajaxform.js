$(document).ready(function(){
    $('#ajax-form').on('submit', function(e) {
        e.preventDefault();

        var fullName = $('#fullName').val();
        var email = $('#email').val();
        var phone = $('#phone').val();
        var category = $('#category').val();
        var heardAboutUs = $('#heard_about_us').val();
        var message = $('#message').val();
        var errorMessage = $('#ContactErrorMessage');
        var isValid = true;

        // Validate full name
        if (fullName.trim() === '') {
            errorMessage.text('Please enter your full name.');
            isValid = false;
        } 
        // Validate email address
        else if (email.trim() === '') {
            errorMessage.text('Please enter your email address.');
            isValid = false;
        } else if (!isValidEmailAddress(email)) {
            errorMessage.text('Please enter a valid email address.');
            isValid = false;
        } 
        // Validate phone number
        else if (phone.trim() === '') {
            errorMessage.text('Please enter your phone number.');
            isValid = false;
        }
        // Validate category selection
        else if (category === '') {
            errorMessage.text('Please select a category.');
            isValid = false;
        }
        // Validate heard about us
        else if (heardAboutUs === '') {
            errorMessage.text('Please specify how you heard about us.');
            isValid = false;
        }
        // Validate message
        else if (message.trim() === '') {
            errorMessage.text('Please enter your message or enquiry.');
            isValid = false;
        }

        if (isValid) {
            $('#contactSubmit').prop('disabled', true).html('Sending <span class="spinner-border spinner-border-sm" style="margin-left: 3px;" role="status" aria-hidden="true"></span> ');

            $.ajax({
                type: 'POST',
                url: '/create-booking/', 
                data: $(this).serialize(),
                success: function(response) {
                    if (response.message === 'Booking successfully created!') {
                        showNotification();
                        $('#ajax-form')[0].reset(); // Reset the form after successful submission
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
                    $('#contactSubmit').prop('disabled', false).html('Send');
                }
            });
        }
    });

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
        } else if (!isValidEmailAddress(email)) {
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

            $.ajax({
                type: 'POST',
                url: '/create-booking/', 
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
