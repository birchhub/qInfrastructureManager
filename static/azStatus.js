
function addRow(vm) {
	let body = document.getElementById('vmTableBody');
	let row = body.insertRow();
	row.id = 'vmTableRow' + body.rows.length;

	let cell1 = row.insertCell(0);
	cell1.innerHTML = vm.name;
	cell1.className = "vmName";

	let cell2 = row.insertCell(1);
	cell2.innerHTML = vm.rg;
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
	} else if (vm.status === 'VM deallocated') {
		cell5.innerHTML = `\
		<button type="button" class="btnStartVM btn btn-primary"><i class="fa fa-play"></i></button> \
		<button type="button" class="btnStopVM disabled btn btn-success"><i class="fa fa-power-off"></i></button> \
		`
	} else {
		cell5.innerHTML = `\
		<button type="button" class="btnStartVM disabled btn btn-primary"><i class="fa fa-play"></i></button> \
		<button type="button" class="btnStopVM disabled btn btn-success"><i class="fa fa-power-off"></i></button> \
		`
	}
}

function loadVMs() {

	fetch('/vmstatus', {
		method: 'GET',
	})
	//.then(response => response.json());
	.then(function(e) {
		console.log(e)
		if (e.status !== 200) {
			alert(e.statusText)
		} else {
			e.json().then(function(respJson) {
				let vmArray = respJson.status;

				// clear table before adding new rows
				let body = document.getElementById('vmTableBody');
				for (let i=body.rows.length-1; i>=0; i--) {
					body.deleteRow(i)
				}

				for (i in vmArray) {
					addRow(vmArray[i])
				}

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
			});
		}

		showHideSpinner(false)
	});
}

function changeVmStatus(action, rowId) {
	let vmName = document.getElementById(rowId).querySelectorAll('.vmName')[0].innerHTML
	let rg = document.getElementById(rowId).querySelectorAll('.vmRg')[0].innerHTML

	showHideSpinner(true)
	fetch(`/${action}?rg=${encodeURIComponent(rg)}&vm=${encodeURIComponent(vmName)}`, {
		method: 'POST',
	}).then(function(response) {
		console.log(response);
		if (response.status == 200) {
			loadVMs()
			showHideSpinner(false)
		} else {
			showHideSpinner(false)
			loadVMs()
			alert(response.statusText);
		}
	});
}

function showHideSpinner(show) {
	let spinner = document.getElementById('spinner');
	if (show) {
		spinner.style.visibility = 'visible'
	} else {
		spinner.style.visibility = 'hidden'
	}
}

(function() {
	loadVMs()
})();
