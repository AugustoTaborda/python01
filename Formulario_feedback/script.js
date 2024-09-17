
document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const feedback = document.getElementById('feedback').value.trim();

    
    if (nome === '' || email === '' || feedback === '') {
        alert('Todos os campos são obrigatórios!');
        return; 
    }

    
    document.getElementById('sucesso').classList.remove('hidden');

    
    document.getElementById('formulario').reset();
});
