
function display(textString,keyString,modeString, onSuccess) {
	// ajax allows the function to take place without having to refresh webpage
    $.ajax({
	    // searches for string_return in app.py
	url: "string_return",
	data: {
	    text_string: textString,
		key_string : keyString,
		mode_string : modeString,
        },
	    // allows function know to return json data type and look for GET method
	dataType: "json",
        type: "GET",
	    // what this does is if the ajax request is successful, it executes the specified function in
		// the parameter (in the below case, that's specified as function(returnedString))
	success: function(response) {
	    onSuccess(response);
	}
    });
}
// if button with id "convert-button" is clicked...
$("#convert-button").on("click", function() {
	// textString is set to the value the user inputted in the text box
    let textString = $("#text-input").val();
	let key = $("#key").val();
	let mode = $("#mode").val();
	// display method from above is called
    display(textString, key, mode, function(returnedString) {
		$("#returned_string").text(returnedString);
    });
});
