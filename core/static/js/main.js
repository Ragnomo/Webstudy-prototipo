document.addEventListener("DOMContentLoaded", () => {
    const btnRun = document.getElementById('btn-run');
    const btnClear = document.getElementById('btn-clear');
    const editor = document.getElementById('code-editor');
    const consoleOut = document.getElementById('console-output');
    const btnComplete = document.getElementById('btn-complete');
    const btnQuiz = document.getElementById('btn-check-quiz');

    if (btnRun) {
        btnRun.addEventListener('click', () => {
            const code = editor.value;
            consoleOut.innerHTML = ''; 

            const originalLog = console.log;
            console.log = function(...args) {
                const msg = args.map(a => typeof a === 'object' ? JSON.stringify(a) : a).join(' ');
                consoleOut.innerHTML += `<div>> ${msg}</div>`;
                originalLog.apply(console, args);
            };

            try {
                const execute = new Function(code);
                execute();
            } catch (error) {
                consoleOut.innerHTML += `<div class="error-msg">Erro: ${error.message}</div>`;
            } finally {
                console.log = originalLog;
            }
        });
    }

    if (btnClear) {
        btnClear.addEventListener('click', () => consoleOut.innerHTML = '');
    }

    if (btnComplete) {
        btnComplete.addEventListener('click', async () => {
            const lessonId = btnComplete.getAttribute('data-lesson-id');
            try {
                const response = await fetch('/api/complete/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ lesson_id: lessonId })
                });
                
                if (response.ok) {
                    btnComplete.innerText = "Aula Concluída ✓";
                    btnComplete.disabled = true;
                    btnComplete.classList.remove('btn-success');
                    btnComplete.classList.add('btn-secondary');
                }
            } catch (error) {
                alert("Erro ao salvar progresso.");
            }
        });
    }

    if (btnQuiz) {
        btnQuiz.addEventListener('click', () => {
            const questions = document.querySelectorAll('.question-block');
            let score = 0;
            let feedbackHTML = '';

            questions.forEach((q, index) => {
                const correct = q.getAttribute('data-correct');
                const selected = q.querySelector(`input[type="radio"]:checked`);
                
                if (selected) {
                    if (selected.value === correct) {
                        score++;
                        q.style.borderLeft = "4px solid #10B981";
                    } else {
                        q.style.borderLeft = "4px solid #EF4444";
                    }
                }
            });

            feedbackHTML = `<p>Você acertou ${score} de ${questions.length} questões!</p>`;
            document.getElementById('quiz-feedback').innerHTML = feedbackHTML;
        });
    }
});

