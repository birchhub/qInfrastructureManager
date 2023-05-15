
function addRow(vm) {
	let table = document.getElementById('vmTable');
	let row = table.insertRow();

	let cell1 = row.insertCell(0);
	cell1.innerHTML = vm.name;

	let cell2 = row.insertCell(1);
	cell2.innerHTML = vm.resourceGroup;

	let cell3 = row.insertCell(2);
	cell3.innerHTML = vm.extIp;

	let cell4 = row.insertCell(3);
	cell4.innerHTML = vm.status;

	let cell5 = row.insertCell(4);
	if (vm.status === 'VM running') {
		cell5.innerHTML = `\
		<button type="button" class="disabled btn btn-primary"><i class="fa fa-play"></i></button> \
		<button type="button" class="btn btn-success"><i class="fa fa-power-off"></i></button> \
		`
	} else {
		cell5.innerHTML = `\
		<button type="button" class="btn btn-primary"><i class="fa fa-play"></i></button> \
		<button type="button" class="disabled btn btn-success"><i class="fa fa-power-off"></i></button> \
		`
	}
}

function loadVMs() {
	// Creating Our XMLHttpRequest object
    let xhr = new XMLHttpRequest();
 
    // Making our connection 
    xhr.open('GET', '/vmstatus', true);
 
    // function execute after request is successful
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
			let vmArray = JSON.parse(this.responseText).status;
			for (i in vmArray) {
				addRow(vmArray[i])
			}
        }
    }
    // Sending our request
    xhr.send();
}

(function() {
	loadVMs()
})();
