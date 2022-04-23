let form = document.getElementById("form1");
form.addEventListener("submit", (e) => {
    e.preventDefault();

    if (document.getElementById('a') && document.getElementById('b')) {
        const a = document.getElementById('a');
        const b = document.getElementById('b');
        const ope = document.querySelectorAll('input[name="ope"]');
        let isTrue = false;
        let opeType = "";

        if (a.value.trim() == "") {
            alert("ERRO: Valor de (a) não foi informado");
            a.focus();
            return;
        }

        if (b.value.trim() == "") {
            alert("ERRO: Valor de (b) não foi informado");
            b.focus();
            return;
        }

        for (let index = 0; index < ope.length; index++) {
            const element = ope[index];

            if (element.checked == true) {
                isTrue = true;
                opeType = element.value;
                break;
            }
        }

        if (isTrue == false) {
            alert("ERRO: Operação não foi selecionada");
            return;
        }

        const URL_TO_FETCH = `http://127.0.0.1:5000/resultado?a=${a.value}&b=${b.value}&ope=${opeType}`;
        fetch(URL_TO_FETCH)
            .then(response => response.json()) // retorna uma promise
            .then(result => {
                let opeTypeOld = opeType;
                switch (opeType) {
                    case 'soma':
                        opeType = '+';
                        break;

                    case 'sub':
                        opeType = '-';
                        break;

                    case 'mult':
                        opeType = '*';
                        break;

                    case 'div':
                        opeType = '÷';
                        break;
                }
                const resul = document.getElementById("resultado");
                resul.classList.remove("none");
                if (result['result']) {
                
                    resul.innerHTML = `
                        <p>O resultado de ${a.value} ${opeType} ${b.value} = ${result['result']}</p>
                    `;

                    a.value = "";
                    b.value = "";
                    document.querySelector(`input[value="${opeTypeOld}"]`).checked = false;
                }else{
                    resul.innerHTML = `
                        <p class="error">${result['ERRO']}</p>
                    `;
                }

            })
            .catch(err => {
                // trata se alguma das promises falhar
                console.error('ERRO: ', err);
            });


    } else {
        alert("Inputs não encontrados com o nome definico como A e B");
    }

});