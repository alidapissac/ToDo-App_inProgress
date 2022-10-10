window.addEventListener('load', () => {
	const ip = document.querySelector("#plan");
	const listele = document.querySelector("#todos");

	document.getElementById("add").addEventListener("click", (e) => {
		e.preventDefault();
        const todo = ip.value;
        
        if(!todo){
            alert("please fill");
            return;
        }

		const todoelement= document.createElement('div');
		todoelement.classList.add('todo');

		const todoinput= document.createElement('input');
		todoinput.classList.add('text');
		todoinput.type = 'text';
		todoinput.value = todo;
		todoinput.setAttribute('readonly', true);
		todoelement.appendChild(todoinput);

		const todoactions = document.createElement('div');
		todoactions.classList.add('actions');
		
		const todoedit = document.createElement('button');
		todoedit.innerText= 'EDIT';
        todoactions.appendChild(todoedit);
        todoedit.addEventListener('click', (e) => {
			if (todoedit.innerText == 'EDIT') {
				todoedit.innerText = 'SAVE';
				todoinput.removeAttribute('readonly');
                todoinput.focus();
			} else {
				todoedit.innerText = 'EDIT';
				todoinput.setAttribute('readonly', true);
			}
        });

		const tododelete = document.createElement('button');
		tododelete.innerText = 'DELETE';
        todoactions.appendChild(tododelete);
        tododelete.addEventListener('click', (e) => {
			listele.removeChild(todoelement);
		});

		todoelement.appendChild(todoactions);
		listele.appendChild(todoelement);
		ip.value = '';			
	});
});