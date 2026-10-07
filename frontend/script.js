const API = '';

const sid = 'demo-session';

const form = document.getElementById('chat-form');
const input = document.getElementById('message');
const provider = document.getElementById('provider');
const box = document.getElementById('messages');

function add(role, text) {
    const d = document.createElement('div');

    d.className = 'message ' + role;

    d.textContent =
        (role === 'user' ? 'You: ' : 'Agent: ') + text;

    box.appendChild(d);
}

form.onsubmit = async e => {
    e.preventDefault();

    const message = input.value.trim();

    if (!message) {
        return;
    }

    add('user', message);

    input.value = '';

    try {
        const r = await fetch(API + '/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                session_id: sid,
                message,
                provider: provider.value
            })
        });

        const d = await r.json();

        if (!r.ok) {
            throw Error(d.error || 'Request failed');
        }

        add(
            'assistant',
            '[' + d.provider + '] ' + d.response
        );

    } catch (e) {
        add(
            'assistant',
            'Error: ' + e.message
        );
    }
};
