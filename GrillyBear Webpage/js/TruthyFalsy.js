function TruthyFalsy(){
	Check = prompt('Enter anything to check truthy or falsy');
	var CheckB = Boolean(`${Check}`)
	alert(`${CheckB}`); 
}