// NOTE: THIS FILE DOES NOT CURRENTLY FUNCTION CORRECTLY AND SHOULD ONLY BE USED AS A BASELINE FOR WEBSITE.JS
// please edit whatever you think is neccessary for this file to work
// the comments describe what SHOULD be happening but isn't


function display(textString, onSuccess) {
	// ajax allows the function to take place without having to refresh webpage
    $.ajax({
	    // searches for string_return in app.py
	url: "string_return",
	data: {
	    text_string: textString
        },
	    // lets function know to return json data type and look for GET method
	dataType: "json",
        type: "GET",
	    // what this does is if the ajax request is successful, it executes the specified function in the parameter (in the below case, that's specifed as function(returnedString))
	success: function(response) {
	    onSuccess(response);
	}
    });
}
// if button with id "convert-button" is clicked...
$("#convert-button").on("click", function() {
	// textString is set to the value the user inputted in the text box
    let textString = $("#text-input").val();
	// display method from above is called 
    display(textString, function(returnedString) {
	$("#returned_string").text(returnedString);
    });
});
