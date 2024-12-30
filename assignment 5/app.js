const express = require('express');
const app = express();

let counter = 0;
let switchState = "UNKNOWN";

app.get('/', (req, res) => {
    res.send(`<h1>Welcome to the Web App</h1>
    <p>Counter: ${counter}</p>
    <p>Switch State: ${switchState}</p>`);
});

app.get('/inc', (req, res) => {
    counter++;
    res.send(`Counter incremented: ${counter}`);
});

app.get('/switch', (req, res) => {
    switchState = switchState === "ON" ? "OFF" : switchState === "OFF" ? "UNKNOWN" : "ON";
    res.send(`Switch toggled to: ${switchState}`);
});

app.get('/metrics', (req, res) => {
    res.set('Content-Type', 'text/plain');
    res.send(`
        counter_value ${counter}
        switch_state{state="ON"} ${switchState === "ON" ? 1 : 0}
        switch_state{state="OFF"} ${switchState === "OFF" ? 1 : 0}
        switch_state{state="UNKNOWN"} ${switchState === "UNKNOWN" ? 1 : 0}
    `);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
