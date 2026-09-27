const { exec } = require("node:child_process");

const password = "Admin123456!";

const input = process.argv[2];

exec(input);

eval(input);
