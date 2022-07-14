function registerInstallAppEvent(elem) {
	const installElem = document.getElementById("install");
	window.addEventListener("beforeinstallprompt", function (event) {
		event.preventDefault();
		elem.promptEvent = event;
		installElem.hidden = false;
		return false;
	});

	elem.addEventListener("click", 	function () {
		if (elem.promptEvent) {
			elem.promptEvent.prompt();
			installElem.hidden = false;
			elem.promptEvent.userChoice.then(function(choice) {
				elem.promptEvent = null;
			});
		}
	});
}
document.addEventListener("DOMContentLoaded", function() {
	registerInstallAppEvent(document.getElementById("installBtn"));
});