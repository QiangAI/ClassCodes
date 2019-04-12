var system = require('system');

function display(a, b) {
    console.log(a, b)
}

var args = system.args;

display(args[1], args[2]);

phantom.exit();

