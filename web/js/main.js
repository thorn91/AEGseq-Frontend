
function call_parse_input_file() 
{
	let f = document.getElementById('target-file-name').files[0];
	let t = document.getElementById('input-display');

	// Clear input display of any previous text
	t.value = " ";

	// Let Python parse the file
	eel.parse_input_file(f.name);

	// Update list of inputted files?
}


/**
 * Simple displays the contents of the input file in the display.
 * 
 * TODO: maybe we don't need all of the contents displayed?
 */
eel.expose(display_input_text);
function display_input_text(text)
{
	let t = document.getElementById('input-display');
	t.value += text;
}