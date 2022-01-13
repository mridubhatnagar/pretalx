document.body.addEventListener('keydown', function(e) {
	if(!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;

	if(e.target.form) {
		e.target.form.submit();
	}
});
const editButton = document.querySelector("#edit-review")
if (editButton) {
  editButton.addEventListener("click", () => { document.querySelector("#own-review").classList.remove("d-none") })
}
