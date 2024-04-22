function display(textString, onSuccess) {
    $.ajax({
	url: "string_return",
	data: {
	    text_string: textString
        },
	dataType: "json",
        type: "GET",
	success: function(response) {
	    onSuccess(response);
	}
    });
}

$("#convert-button").on("click", function() {
    let textString = $("#text-input").val();
    display(textString, function(returnedString) {
	$("#returned_string").text(returnedString);
    });
});
