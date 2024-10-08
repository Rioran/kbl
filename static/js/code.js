const api_url = 'http://localhost:5000/api/';
const message_element = document.getElementById('message_element');


function entry_point() {
    console.log('Hello! TODO: code everything.');
}


function print_message(text) {
	message_element.textContent = text;
}


async function call_api(url) {
	try {
		const response = await fetch(url);
		if (!response.ok) {
			print_message(`Response status: ${response.status}`);
		}
		const json = await response.json();
		print_message(json);
	} catch (error) {
		print_message(error.message);
	}
}


async function install_kbl(file_name) {
	const url = api_url + `install_kbl?file=${file_name}`;
	call_api(url);
}


async function toggle_layout(layout_id) {
	const url = api_url + `toggle_layout?layout_id=${layout_id}`;
	call_api(url);
}
