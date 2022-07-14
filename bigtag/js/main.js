function registerInstallAppEvent(elem) {
	window.addEventListener("beforeinstallprompt", function (event) {
		//event.preventDefault();
		elem.promptEvent = event;
		console.log(elem.promptEvent);
		document.getElementById("install").hidden = false;
		//return false;
	});

	elem.addEventListener("click", 	function () {
		if (elem.promptEvent) {
			console.log("exec");
			elem.promptEvent.prompt();
			elem.promptEvent.userChoice.then(function(choice) {
				elem.promptEvent = null;
			});
		}
	});
}
document.addEventListener("DOMContentLoaded", function() {
	registerInstallAppEvent(document.getElementById("installBtn"));
});