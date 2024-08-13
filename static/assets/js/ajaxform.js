
const form = document.getElementById("ajax-form");
const result = document.getElementById("result");

form.addEventListener("submit", function (e) {
	e.preventDefault();

	const formData = new FormData(form);
	const object = Object.fromEntries(formData);
	const json = JSON.stringify(object);

	result.innerHTML = "Please wait...";
	result.style.marginTop = '10px';

	fetch("https://api.web3forms.com/submit", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			Accept: "application/json",
		},
		body: json,
	})
		.then(async (response) => {
			let json = await response.json();
			if (response.status == 200) {
				result.innerHTML = json.message;
				result.classList.remove("text-gray-500");
				result.classList.add("text-green-500");
			} else {
				result.innerHTML = json.message;
				result.classList.remove("text-gray-500");
				result.classList.add("text-red-500");
			}
		})
		.catch((error) => {
			console.log(error);
			result.innerHTML = "Something went wrong!";
		})
		.then(function () {
			form.reset();
			setTimeout(() => {
				result.style.marginTop = '0';
				result.style.display = "none";
			}, 5000);
		});
});