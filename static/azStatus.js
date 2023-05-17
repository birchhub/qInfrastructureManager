
function addRow(vm) {
	let table = document.getElementById('vmTable');
	let row = table.insertRow();
	row.id = 'vmTableRow' + table.rows.length;

	let cell1 = row.insertCell(0);
	cell1.innerHTML = vm.name;
	cell1.className = "vmName";

	let cell2 = row.insertCell(1);
	cell2.innerHTML = vm.resourceGroup;
	cell2.className = "vmRg";

	let cell3 = row.insertCell(2);
	cell3.innerHTML = vm.extIp;

	let cell4 = row.insertCell(3);
	cell4.innerHTML = vm.status;

	let cell5 = row.insertCell(4);
	if (vm.status === 'VM running') {
		cell5.innerHTML = `\
		<button type="button" class="btnStartVM disabled btn btn-primary"><i class="fa fa-play"></i></button> \
		<button type="button" class="btnStopVM btn btn-success"><i class="fa fa-power-off"></i></button> \
		`
	} else {
		cell5.innerHTML = `\
		<button type="button" class="btnStartVM btn btn-primary"><i class="fa fa-play"></i></button> \
		<button type="button" class="btnStopVM disabled btn btn-success"><i class="fa fa-power-off"></i></button> \
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

			//let startButtons = document.getElementsByClassName('btnStartVM');
			let startButtons = document.querySelectorAll('.btnStartVM:not(disabled)');
			for (let i=0; i<startButtons.length; i++) {
				startButtons[i].addEventListener('click', function() {

					// get actual button (not the case when clicking on icon)
					let clickedButton = event.target.closest('button')

					let rowId = clickedButton.parentNode.parentNode.id;
					changeVmStatus('START', rowId)
				});
			}

			let stopButtons = document.querySelectorAll('.btnStopVM:not(disabled)');
			for (let i=0; i<stopButtons.length; i++) {
				stopButtons[i].addEventListener('click', function() {
					// get actual button (not the case when clicking on icon)
					let clickedButton = event.target.closest('button')

					let rowId = clickedButton.parentNode.parentNode.id;
					changeVmStatus('STOP', rowId)
				});
			}
        }
    }
    // Sending our request
    xhr.send();
}

function changeVmStatus(action, rowId) {
	let vmName = document.getElementById(rowId).querySelectorAll('.vmName')[0].innerHTML
	let rg = document.getElementById(rowId).querySelectorAll('.vmRg')[0].innerHTML

	fetch(`/${action}?rg=${encodeURIComponent(rg)}&vm=${encodeURIComponent(vmName)}`, {
		method: 'POST',
	}).then(function(response) {
		if (response.status == 200) {
		} else {
			// XXX proper fancy dialog
			alert(response.statusText);
		}
	});
}

(function() {
	loadVMs()
})();
